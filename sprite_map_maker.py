import pygame
import random
from icecream import ic

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

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

SIDE_GRID_LENGTH = 8

def draw_full_grid2(screen, startposx, startposy, length, height, tile_size):
    for row in range(0, length):
        for column in range(0, height):
            draw_rect(screen, startposx + (row * (tile_size * 2.5) + tile_size), startposy + (column * (tile_size*2.5) + tile_size), (0, 0, 0), tile_size * 2, tile_size * 2)

def display_full_grid(grid_full, grid_length, deepness, screen, steepness):
    defined = False
    op = 0
    for row in range(0, 8):
        for col in range(0, 8):
            if grid_full[row][col] == False:
                if not defined:
                    true_rectxy = None
                # (screen, x, y, colour, size_x, size_y)
                # (screen, (0-8 * 20) + 25, 0-8 * 20 + 15, the colour black, 20, 20)
                # draws 80 p by 80 p rects
                draw_full_grid2(screen, row*grid_length+deepness, col * grid_length + steepness, 5, 5, 5)
                # for row2 in range (0, 5):   (random.randint(0, 120), random.randint(0, 120), random.randint(0, 120))
                #     for col2 in range(0, 5):
                #         op = op + 1
                #         print((row2*grid_length+deepness)*1.4)
                        # draw_rect(screen, (row2*grid_length+deepness)*1.4*int(row / 8), (col2 * grid_length + steepness) * 1.4, (random.randint(0, 120), random.randint(0, 120), random.randint(0, 120)), grid_length -50, grid_length -50)
                # draw_rect(screen, row*grid_length+deepness, col * grid_length + steepness, (0, 0, 0), grid_length, grid_length)
            
            else:
                # draws a box around the currently selected position
                defined = True
                true_rectxy = (row, col)

    # print(op)

    if true_rectxy != None:
        draw_rect(screen, true_rectxy[0]*grid_length+deepness-7.5, true_rectxy[1] * grid_length + steepness -7.5, (255, 255, 255), grid_length + 15, grid_length + 15)
        draw_rect(screen, true_rectxy[0]*grid_length+deepness, true_rectxy[1] * grid_length + steepness, (0, 0, 0), grid_length, grid_length)
    return true_rectxy

def display_side_grid(grid, grid_length, deepness, screen, steepness):
    for row in range(0, 8):
        for col in range(0, 8):
            # draws 20 by 20 rects
            draw_rect(screen, row*grid_length+deepness, col * grid_length + steepness, grid[row][col], grid_length, grid_length)

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
        
        current_colour = (get_slider_colour(slider_pos_red, (0, 255, 25, 180)), get_slider_colour(slider_pos_green, (0, 255, 25, 180)), get_slider_colour(slider_pos_blue, (0, 255, 25, 180)))
        
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
    brush_colour = (0, 0, 0)
    bucket_colour = (0, 0, 0)

    if False:
        # draws the brush and the fill bucket
        screen.blit(brush_png, (screen_width / 2 - 225, 0))
        screen.blit(bucket_png, (screen_width / 2 - 225, 0))

    if tool_selected == "brush":
        brush_colour = (136, 10, 232)
    elif tool_selected == "bucket":
        bucket_colour = (136, 10, 232)

    # draws the boxes around the brush
    draw_rect(screen, 25, 475, (244, 234, 87), 65, 65)
    draw_rect(screen, 30, 480, brush_colour, 55, 55)

    # draws the boxes around the bucket
    draw_rect(screen, 115, 475, (244, 234, 87), 65, 65)
    draw_rect(screen, 120, 480, bucket_colour, 55, 55)

    # draws the boxes of set colours
    # draws the 
    for row in range(20, 141, 60):
        for column in range(575, 636, 60):
            draw_rect(screen, row, column, (244, 234, 87), 45, 45)

    # red: 25x 580y to 60x 615y
    draw_rect(screen, 25, 580, (255, 0, 0), 35, 35)
    # green: 85x 580y to 110x 615y
    draw_rect(screen, 85, 580, (0, 255, 0), 35, 35)
    # blue: 145x 580y to 180x 615y
    draw_rect(screen, 145, 580, (0, 0, 255), 35, 35)

    # black: 25x 640y to 60x 675y
    draw_rect(screen, 25, 640, (0, 0, 0), 35, 35)
    # white: 85x 640y to 110x 675y
    draw_rect(screen, 85, 640, (255, 255, 255), 35, 35)
    # grey: 145x 640y to 180x 675y
    draw_rect(screen, 145, 640, (128, 128, 128), 35, 35)

def draw_line(screen, startx, starty, endx, endy, colour = (0, 0, 0), width = 1):
    pygame.draw.line(screen, colour, (startx, starty), (endx, endy), width)

def draw_polygon(screen, colour, square_brackets_points):
    pygame.draw.polygon(screen, colour, square_brackets_points)

# draws a coloured rectange on the screen
def draw_rect(screen, x, y, colour, size_x, size_y):
    square = pygame.Rect((x, y, size_x, size_y))
    pygame.draw.rect(screen, colour, square)

# def get_slider_colour(original_colour, changeing = False):
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

    # foldable list of general variables (244, 234, 87)
    if True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        out_of_range = False

        # defines the colour slider variables      
        current_colour = (0, 0, 0)
        
        slider_red_pos = 25
        slider_green_pos = 25
        slider_blue_pos = 25

        # defines the grids + rect grids

        full_grid_length = 8
        grid_full = [[False] * full_grid_length for _ in range(0, full_grid_length)]
        grid_full[0][0] = True

        RECT_full_grid_length = 8
        RECT_grid_full = [[False] * RECT_full_grid_length for _ in range(0, RECT_full_grid_length)]
        RECT_grid_full[0][0] = True
        rect_grid = get_grid_rects(RECT_grid_full, RECT_full_grid_length * 10, 215)

        # which colour is currently selected to be changed and which colour it has been changed to
        slider_change = NO_COLOUR
        set_colour_change = None

        # width of the tiles in the side grid

        colour_side_grid = [[(0, 0, 0)] * SIDE_GRID_LENGTH for _ in range(0, SIDE_GRID_LENGTH)]

        # defines the brush variables & pngs
        tool_selected = "brush"
        brush_png = None
        bucket_png = None

    running = True
    while running:

        mouse_pos = None
        set_colour_change = None

        key = pygame.key.get_pressed()

        for event in pygame.event.get():

            # if escape or quit, ends the while loop which leads to the game quiting
            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False

            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN or out_of_range:

                # if the mouse position is in range of the larger grid then it checks where in it,
                # sets that place to selected, and sets all other places to unselected

                if (mouse_pos[0] >= 215 and mouse_pos[0] <= 790) and (mouse_pos[1] >= 20 and mouse_pos[1] <= 590):
                    for row in range(0, 8):
                        for column in range(0, 8):
                            if pygame.mouse.get_pressed()[0] and rect_grid[row][column].collidepoint(mouse_pos):
                                grid_full[row][column] = True
                            else:
                                grid_full[row][column] = False

                # changes the side grid when pressed
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 185) and (mouse_pos[1] >= 28 and mouse_pos[1] <= 184):
                    for row in range(0, 8):
                        for column in range(0, 8):
                            collider_row = int((mouse_pos[0] - 25) / 20)
                            collider_col = int((mouse_pos[1] - 28) / 20)

                            colour_side_grid[collider_row][collider_col] = current_colour

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
                # red: 25x 580y to 60x 615y
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 60) and (mouse_pos[1] >= 580 and mouse_pos[1] <= 615):
                    current_colour = RED
                    set_colour_change = current_colour

                # green: 85x 580y to 110x 615y
                elif (mouse_pos[0] >= 85 and mouse_pos[0] <= 110) and (mouse_pos[1] >= 580 and mouse_pos[1] <= 615):
                    current_colour = GREEN
                    set_colour_change = current_colour

                # blue: 145x 580y to 180x 615y
                elif (mouse_pos[0] >= 145 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 580 and mouse_pos[1] <= 615):
                    current_colour = BLUE
                    set_colour_change = current_colour

                # black: 25x 640y to 60x 675y
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 60) and (mouse_pos[1] >= 640 and mouse_pos[1] <= 675):
                    current_colour = BLACK
                    set_colour_change = current_colour

                # white: 85x 640y to 110x 675y
                elif (mouse_pos[0] >= 85 and mouse_pos[0] <= 110) and (mouse_pos[1] >= 640 and mouse_pos[1] <= 675):
                    current_colour = WHITE
                    set_colour_change = current_colour
            
                # grey: 145x 640y to 180x 675y
                elif (mouse_pos[0] >= 145 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 640 and mouse_pos[1] <= 675):
                    current_colour = GREY
                    set_colour_change = current_colour

            if event.type == pygame.MOUSEBUTTONUP:
                slider_change = NO_COLOUR
                out_of_range = False
            if (mouse_pos[0] <= 25 or mouse_pos[0] > 180) and slider_change != NO_COLOUR:
                slider_change = NO_COLOUR
                out_of_range = True

        screen.fill((45, 52, 92))

                                    # --display from here onward!--

        if mouse_pos == None:
            mouse_pos = pygame.mouse.get_pos()

        # draws the currently selected colour in a box below the side grid
        draw_rect(screen, 75, 370, (244, 234, 87), 60, 60)
        draw_rect(screen, 80, 375, current_colour, 50, 50)

        # draws the colour bars
        slider_red_pos, slider_green_pos, slider_blue_pos, current_colour = draw_colour_bar(slider_red_pos, slider_green_pos, slider_blue_pos, current_colour, mouse_pos, slider_change, screen, set_colour_change)

        # draws the main grid
        true_rectxy_tuple = display_full_grid(grid_full, full_grid_length * 10, 215, screen, 15)

        # draws the grid on the side of the screen
        display_side_grid(colour_side_grid, SIDE_GRID_LENGTH * 2.5, 25, screen, 25)
        draw_brushes_and_set_colours(screen, SCREEN_WIDTH, brush_png, bucket_png, tool_selected)

        pygame.display.update()

    pygame.quit



main()