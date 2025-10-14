import pygame
import random
from icecream import ic

import sprite_map_maker_essential

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

FILL = 0
BRUSH = 1

NO_COLOUR = 0
RED_COLOUR = 1
GREEN_COLOUR = 2
BLUE_COLOUR = 3

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

TERQOISE = (0, 170, 170)
ORANGE = (255, 135, 0)
PINK = (255, 164, 255)
YELLOW = (255, 255, 0)
PURPLE = (220, 0, 220)
CYAN = (0, 255, 255)

SIDE_GRID_LENGTH = 8

def save_map(full_colour_grid):
    sprite_map_maker_essential.set_file(full_colour_grid)
    print("saved to grid_file.json!")

def draw_opacity_text(screen, x, y, text, colour, font_size, opacity = 255):
    font = pygame.font.SysFont('arial', font_size)
    text = font.render(str(text), True, (255,0,0))
    surface = pygame.Surface(text.get_size(), pygame.SRCALPHA)
    surface.blit(text, (0,0))
    surface.fill((colour[0], colour[1], colour[2], opacity), None, pygame.BLEND_RGBA_MULT)
    screen.blit(surface, (x, y))

def draw_centered_text(screen, x, y, text, colour, font_size):
    font = pygame.font.SysFont('arial', font_size)
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

def get_grid_rects(grid, grid_length, deepness):
    for row in range(0, 8):
        for column in range(0, 8):
            grid[row][column] = pygame.Rect((row * grid_length + deepness, column * grid_length + 15, grid_length, grid_length))
    return grid

def draw_colour_bar(slider_pos_red, slider_pos_green, slider_pos_blue, current_colour, mouse_pos, slider_change, screen, colour_change):
    for row in range(25, 185):
        draw_rect(screen, row, 210, (row, 0, 0), 1, 30)
        draw_rect(screen, row, 270, (0, row, 0), 1, 30)
        draw_rect(screen, row, 330, (0, 0, row), 1, 30)

    red_in = ()
    green_in = ()
    blue_in = ()
    # sets the slider bar to wherver you press on it and the colour to where it is on the bar
    if colour_change != None:
        slider_pos_red = colour_change[0]
        slider_pos_green = colour_change[1]
        slider_pos_blue = colour_change[2]

        current_colour = (slider_pos_red, slider_pos_green, slider_pos_blue)

        red_in = 0, 255, 25, 180
        green_in = 0, 255, 25, 180
        blue_in = 0, 255, 25, 180
    elif slider_change != 0:
        # red
        if slider_change == 1:
            slider_pos_red = mouse_pos[0]
            current_colour = (get_slider_colour(slider_pos_red, (25, 180, 0, 255)), current_colour[1], current_colour[2])
        # green
        elif slider_change == 2:
            slider_pos_green = mouse_pos[0]
            current_colour = (current_colour[0], get_slider_colour(slider_pos_green, (25, 180, 0, 255)), current_colour[2])
        # blue
        elif slider_change == 3:
            slider_pos_blue = mouse_pos[0]
            current_colour = (current_colour[0], current_colour[1], get_slider_colour(slider_pos_blue, (25, 180, 0, 255)))
    
    draw_rect(screen, slider_pos_red - 3, 210 - 7.5, (255, 255, 255), 10, 45)
    draw_rect(screen, slider_pos_green - 3, 270 - 7.5, (255, 255, 255), 10, 45)
    draw_rect(screen, slider_pos_blue - 3, 330 - 7.5, (255, 255, 255), 10, 45)

    red_return = slider_pos_red
    green_return = slider_pos_green
    blue_return = slider_pos_blue

    if red_in != ():
        red_return = get_slider_colour(slider_pos_red, red_in)
    if green_in != ():
        green_return = get_slider_colour(slider_pos_green, green_in)
    if blue_in != ():
        blue_return = get_slider_colour(slider_pos_blue, blue_in)

    return red_return, green_return, blue_return, current_colour

def draw_brushes_and_set_colours(screen, screen_width, brush_png, bucket_png, tool_selected):

    if False:
        # draws the brush and the fill bucket
        screen.blit(brush_png, (screen_width / 2 - 225, 0))
        screen.blit(bucket_png, (screen_width / 2 - 225, 0))

    if tool_selected == BRUSH:
        brush_colour = (136, 10, 232)
        bucket_colour = (0, 0, 0)

    elif tool_selected == FILL:
        bucket_colour = (136, 10, 232)
        brush_colour = (0, 0, 0)

    # draws the boxes around the tools
    draw_rect(screen, 25, 475, (244, 234, 87), 65, 65)
    draw_rect(screen, 30, 480, brush_colour, 55, 55)

    draw_rect(screen, 115, 475, (244, 234, 87), 65, 65)
    draw_rect(screen, 120, 480, bucket_colour, 55, 55)

    # draws the boxes of set colours
    for row in range(890, 1101, 100):
        for column in range(275, 576, 100):
            draw_rect(screen, row, column, (174, 174, 174), 80, 80)
    
    # terqoise: 25x 580y to 60x 615y
    draw_rect(screen, 895, 480, (0, 170, 170), 70, 70)
    # orange: 85x 580y to 110x 615y
    draw_rect(screen, 995, 480, (255, 135, 0), 70, 70)
    # pink: 145x 580y to 180x 615y
    draw_rect(screen, 1095, 480, (255, 164, 255), 70, 70)
    
    # red: 25x 580y to 60x 615y
    draw_rect(screen, 895, 280, (255, 0, 0), 70, 70)
    # green: 85x 580y to 110x 615y
    draw_rect(screen, 995, 280, (0, 255, 0), 70, 70)
    # blue: 145x 580y to 180x 615y
    draw_rect(screen, 1095, 280, (0, 0, 255), 70, 70)

    # yellow: 25x 640y to 60x 675y
    draw_rect(screen, 895, 380, (255, 255, 0), 70, 70)
    # purple: 85x 640y to 110x 675y
    draw_rect(screen, 995, 380, (220, 0, 220), 70, 70)
    # cyan: 145x 640y to 180x 675y
    draw_rect(screen, 1095, 380, (0, 255, 255), 70, 70)

    # black: 25x 640y to 60x 675y
    draw_rect(screen, 895, 580, (0, 0, 0), 70, 70)
    # white: 85x 640y to 110x 675y
    draw_rect(screen, 995, 580, (255, 255, 255), 70, 70)
    # grey: 145x 640y to 180x 675y
    draw_rect(screen, 1095, 580, (128, 128, 128), 70, 70)

def draw_line(screen, startx, starty, endx, endy, colour = (0, 0, 0), width = 1):
    pygame.draw.line(screen, colour, (startx, starty), (endx, endy), width)

def draw_polygon(screen, colour, square_brackets_points):
    pygame.draw.polygon(screen, colour, square_brackets_points)

def draw_rect(screen, x, y, colour, size_x, size_y):
    square = pygame.Rect((x, y, size_x, size_y))
    pygame.draw.rect(screen, colour, square)

def get_slider_colour(original_colour, in_tuple, anything = True):
    in_min, in_max, out_min, out_max = in_tuple
    if anything:
        return (original_colour - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    return original_colour

# displays coloured text on the screen
def type_msg(screen, font, x, y, text, colour):
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

def main():

    # foldable list of general variables
    if True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        out_of_range = False

        # defines the colour slider variables      
        current_colour = (255, 0, 0)
        
        slider_red_pos = 25
        slider_green_pos = 25
        slider_blue_pos = 25

        # defines the grids + rect grids

        selected = (0, 0)

        full_grid_length = 64
        # full_colour_grid = [[[[0, 0, 0]] * 8 for _ in range(0, 8)] * full_grid_length for _ in range(0, full_grid_length)]
        full_colour_grid = [ 
            [ ( 0, 0, 0 ) ]
            * full_grid_length
                for _ in range(0, full_grid_length) 
                ]
        selected = (0, 0)

        # which colour is currently selected to be changed and which colour it has been changed to
        slider_change = NO_COLOUR
        set_colour_change = None

        # width of the tiles in the side grid

        colour_side_grid = [[(0, 0, 0)] * SIDE_GRID_LENGTH for _ in range(0, SIDE_GRID_LENGTH)]

        # defines the brush variables & pngs
        tool_selected = BRUSH
        brush_png = None
        bucket_png = None
        trying_delete = False

        saved_text = False
        opacity = 255
        t = 255

        cmd = False

    running = True
    while running:

        mouse_pos = None
        set_colour_change = None

        key = pygame.key.get_pressed()

        for event in pygame.event.get():

            # if escape or quit, ends the while loop which leads to the game quiting
            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LMETA or event.key == pygame.K_RMETA:
                    cmd = True
                
                if cmd and event.key == pygame.K_s:
                    save_map(full_colour_grid)
                    opacity = 255
                    t = 255
                    saved_text = True
                
                if cmd and event.key == pygame.K_BACKSPACE and trying_delete:
                    full_colour_grid = [ [(0, 0, 0)] * full_grid_length for _ in range(0, full_grid_length)]
                
                if cmd and event.key == pygame.K_BACKSPACE:
                    trying_delete = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LMETA or event.key == pygame.K_RMETA:
                    cmd = False
                    trying_delete = False

            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN or out_of_range:

                # changes the selected sprite#

                if (mouse_pos[0] >= 221 and mouse_pos[0] <= 860) and (mouse_pos[1] >= 23 and mouse_pos[1] <= 660):
                    collider_row = int((mouse_pos[0] - 221) / 80)
                    collider_col = int((mouse_pos[1] - 23) / 80)

                    selected = collider_row, collider_col
                    print(mouse_pos)
                    for row in range(0, 8):
                        for col in range(0, 8):
                            grid_row = collider_row * 8 + row
                            grid_col = collider_col * 8 + col
                            colour_side_grid[row][col] = full_colour_grid[grid_row][grid_col]

                # changes the side grid when pressed
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 184) and (mouse_pos[1] >= 28 and mouse_pos[1] <= 186):

                    collider_row = int((mouse_pos[0] - 25) / 20)
                    collider_col = int((mouse_pos[1] - 28) / 20)

                    selec_row = collider_row + ((selected[0]) * 8)
                    selec_col = collider_col + ((selected[1]) * 8)

                    colour_side_grid[collider_row][collider_col] = current_colour
                    full_colour_grid[selec_row][selec_col] = current_colour

                # changes the colour in the colour bars
                # red
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 210 and mouse_pos[1] <= 240):
                    slider_change = RED_COLOUR
                # green
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 270 and mouse_pos[1] <= 300):
                    slider_change = GREEN_COLOUR
                # blue
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 330 and mouse_pos[1] <= 360):
                    slider_change = BLUE_COLOUR


                # changes the colour to one of the set colours if they are pressed
                # red
                elif (mouse_pos[0] >= 890 and mouse_pos[0] <= 970) and (mouse_pos[1] >= 275 and mouse_pos[1] <= 355):
                    current_colour = RED
                    set_colour_change = current_colour
                # green
                elif (mouse_pos[0] >= 990 and mouse_pos[0] <= 1070) and (mouse_pos[1] >= 275 and mouse_pos[1] <= 355):
                    current_colour = GREEN
                    set_colour_change = current_colour
                # blue
                elif (mouse_pos[0] >= 1090 and mouse_pos[0] <= 1170) and (mouse_pos[1] >= 275 and mouse_pos[1] <= 355):
                    current_colour = BLUE
                    set_colour_change = current_colour

                # terqoise
                elif (mouse_pos[0] >= 890 and mouse_pos[0] <= 970) and (mouse_pos[1] >= 475 and mouse_pos[1] <= 555):
                    current_colour = TERQOISE
                    set_colour_change = current_colour
                # orange
                elif (mouse_pos[0] >= 990 and mouse_pos[0] <= 1070) and (mouse_pos[1] >= 475 and mouse_pos[1] <= 555):
                    current_colour = ORANGE
                    set_colour_change = current_colour
                # pink
                elif (mouse_pos[0] >= 1090 and mouse_pos[0] <= 1170) and (mouse_pos[1] >= 475 and mouse_pos[1] <= 555):
                    current_colour = PINK
                    set_colour_change = current_colour

                # yellow
                elif (mouse_pos[0] >= 890 and mouse_pos[0] <= 970) and (mouse_pos[1] >= 375 and mouse_pos[1] <= 455):
                    current_colour = YELLOW
                    set_colour_change = current_colour
                # purple
                elif (mouse_pos[0] >= 990 and mouse_pos[0] <= 1070) and (mouse_pos[1] >= 375 and mouse_pos[1] <= 455):
                    current_colour = PURPLE
                    set_colour_change = current_colour
                # cyan
                elif (mouse_pos[0] >= 1090 and mouse_pos[0] <= 1170) and (mouse_pos[1] >= 375 and mouse_pos[1] <= 455):
                    current_colour = CYAN
                    set_colour_change = current_colour

                # black
                elif (mouse_pos[0] >= 890 and mouse_pos[0] <= 970) and (mouse_pos[1] >= 575 and mouse_pos[1] <= 655):
                    current_colour = BLACK
                    set_colour_change = current_colour
                # white
                elif (mouse_pos[0] >= 990 and mouse_pos[0] <= 1070) and (mouse_pos[1] >= 575 and mouse_pos[1] <= 655):
                    current_colour = WHITE
                    set_colour_change = current_colour
                # grey
                elif (mouse_pos[0] >= 1090 and mouse_pos[0] <= 1170) and (mouse_pos[1] >= 575 and mouse_pos[1] <= 655):
                    current_colour = GREY
                    set_colour_change = current_colour

                # changes the selected tool to whatever brush is clicked
                # fill/bucket tool
                elif (mouse_pos[0] >= 116 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 478 and mouse_pos[1] <= 541):
                    tool_selected = FILL
                # brush tool
                elif (mouse_pos[0] >= 26 and mouse_pos[0] <= 89) and (mouse_pos[1] >= 478 and mouse_pos[1] <= 541):
                    tool_selected = BRUSH

            if event.type == pygame.MOUSEBUTTONUP:
                slider_change = NO_COLOUR
                out_of_range = False
            if (mouse_pos[0] <= 25 or mouse_pos[0] > 180) and slider_change != NO_COLOUR:
                slider_change = NO_COLOUR
                out_of_range = True

        screen.fill((45, 52, 92))

        if mouse_pos == None:
            mouse_pos = pygame.mouse.get_pos()

                                                # --display from here onward!--

        if saved_text:
            t = t - 0.75

            if t < 128:
                opacity = int(t) + 55
            
            if t == -30:
                saved_text = False
                t = 255
            draw_opacity_text(screen, 900, 20, "saved!", (0, 0, 0), 40, opacity)
            

        if trying_delete and not saved_text:
            draw_centered_text(screen, 90, 560, "press command +", (0, 0, 0), 20)
            draw_centered_text(screen, 110, 580, "delete again to confirm", (0, 0, 0), 20)
            draw_centered_text(screen, 90, 600, "delete or let go of", (0, 0, 0), 20)
            draw_centered_text(screen, 95, 620, "command to cancel", (0, 0, 0), 20)

        # draws the currently selected colour in a box below the side grid
        draw_rect(screen, 75, 370, (244, 234, 87), 60, 60)
        draw_rect(screen, 80, 375, current_colour, 50, 50)

        # draws the colour bars
        slider_red_pos, slider_green_pos, slider_blue_pos, current_colour = draw_colour_bar(slider_red_pos, slider_green_pos, slider_blue_pos, current_colour, mouse_pos, slider_change, screen, set_colour_change)

        # draws the grids
        sprite_map_maker_essential.main(colour_side_grid, current_colour, full_colour_grid, full_grid_length, screen, selected, SIDE_GRID_LENGTH)

        draw_brushes_and_set_colours(screen, SCREEN_WIDTH, brush_png, bucket_png, tool_selected)

        pygame.display.update()

    pygame.quit



main()