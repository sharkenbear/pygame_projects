import os
import json
import pygame
from icecream import ic
import time

import sprite_map_maker_essential2

pygame.init()

sprite_nums = {
    "a": (0, 0),
    "b": (1, 0),
    "c": (2, 0),
    "d": (3, 0),
    "e": (4, 0),
    "f": (5, 0),
    "g": (6, 0),
    "h": (7, 0),
    "i": (0, 1),
    "j": (1, 1),
    "k": (2, 1),
    "l": (3, 1),
    "m": (4, 1),
    "n": (5, 1),
    "o": (6, 1),
    "p": (7, 1),
    "q": (0, 2),
    "r": (1, 2),
    "s": (2, 2),
    "t": (3, 2),
    "u": (4, 2),
    "v": (5, 2),
    "w": (6, 2),
    "x": (7, 2),
    "y": (0, 3),
    "z": (1, 3),
    "!": (2, 3),
    ".": (3, 3),
    0: (4, 3),
    1: (5, 3),
    2: (6, 3),
    3: (7, 3),
    4: (0, 4),
    5: (1, 4),
    6: (2, 4),
    7: (3, 4),
    8: (4, 4),
    9: (5, 4),
    "_": (6, 4),
    "'open": (7, 4),
    "'close": (0, 5),
    ",": (1, 5),
    "not_brush": (2, 5),
    "not_colour_picker": (3, 5),
    "not_fill": (4, 5),
    "bin": (5, 5),
    "selected_arrow": (6, 5),
    "yes_brush": (7, 5),
    "yes_colour_picker": (0, 6),
    "yes_fill": (1, 6),
    "not_pen": (2, 6),
    "yes_pen": (3, 6),
}

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FULL_GRID_LENGTH = 64
SPRITE_LENGTH = int(FULL_GRID_LENGTH ** 0.5)

STARTING = 0
REDOING = 1
STOPPED = 2

FILL = 0
PEN = 1
COLOUR_PICKER = 2
BRUSH = 3
AUTO_FILL = 4

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

def access_sprite(grid, file_name, selected):
    if selected[0] < SPRITE_LENGTH and selected[1] < SPRITE_LENGTH:
        with open(file_name, 'r') as file:
            python_obj = json.load(file)
            for num in range(0, SPRITE_LENGTH):
                for num2 in range(0, SPRITE_LENGTH):
                    file_contents = python_obj['contents']
                    grid[num][num2] = file_contents[num + selected[0] * SPRITE_LENGTH][num2 + selected[1] * SPRITE_LENGTH]
    else:
        print("there has been an error. perhaps sprite map is too small")
    return grid

def draw_sprite(access_file_name, selected, x, y, pixel_length, background_colour = False):
    grid = [[(0, 0, 0)] * SPRITE_LENGTH for _ in range(0, SPRITE_LENGTH)]
    grid = access_sprite(grid, access_file_name, selected)
    for x2 in range(0, SPRITE_LENGTH):
        for y2 in range(0, SPRITE_LENGTH):
            if background_colour == False:
                draw_rect(x + x2*pixel_length, y + y2*pixel_length, grid[x2][y2], pixel_length, pixel_length)
            else:
                background_tuple0, background_tuple1, background_tuple2, = background_colour
                checked = 0

                for num0 in range(0, 5):
                    for num1 in range(0, 5):
                        for num2 in range(0, 5):

                            if background_tuple0 < 2:
                                background_tuple0 = 2
                            if background_tuple1 < 2:
                                background_tuple1 = 2
                            if background_tuple2 < 2:
                                background_tuple2 = 2

                            if grid[x2][y2] != [background_tuple0 - 2 + num0, background_tuple1 - 2 + num1, background_tuple2 - 2 + num2]:
                                checked = checked + 1

                if checked == 125:
                    draw_rect(x + x2*pixel_length, y + y2*pixel_length, grid[x2][y2], pixel_length, pixel_length)

def man_save_map(full_colour_grid, file_created, file_name, opacity, t, saved_text):
    possible_full_name, possible_name, possible_type = sprite_map_maker_essential2.set_file(full_colour_grid, file_created, file_name)

    if possible_full_name != "exit":
        opacity = 255
        t = 255
        saved_text = True
        return opacity, t, saved_text, possible_name, possible_type, possible_full_name
    else:
        print("exited")
    return opacity, t, saved_text, None, None, possible_full_name

def auto_save_map(full_colour_grid, file_created, file_name, opacity, t, saved_text):
    sprite_map_maker_essential2.set_file(full_colour_grid, file_created, file_name, "auto")
    return opacity, t, saved_text, None, None

def draw_opacity_text(x, y, text, colour, font_size, opacity = 255):
    font = pygame.font.SysFont('arial', font_size)
    text = font.render(str(text), True, (255,0,0))
    surface = pygame.Surface(text.get_size(), pygame.SRCALPHA)
    surface.blit(text, (0,0))
    surface.fill((colour[0], colour[1], colour[2], opacity), None, pygame.BLEND_RGBA_MULT)
    SCREEN.blit(surface, (x, y))

def draw_centered_text(x, y, text, colour, font_size):
    font = pygame.font.SysFont('arial', font_size)
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    SCREEN.blit(text, text_rect)

def draw_colour_bar(slider_pos_red, slider_pos_green, slider_pos_blue, current_colour, mouse_pos, slider_change, colour_change):
    for row in range(25, 185):
        draw_rect(row, 210, (row, 0, 0), 1, 30)
        draw_rect(row, 270, (0, row, 0), 1, 30)
        draw_rect(row, 330, (0, 0, row), 1, 30)

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
    
    draw_rect(slider_pos_red - 3, 210 - 7.5, (255, 255, 255), 10, 45)
    draw_rect(slider_pos_green - 3, 270 - 7.5, (255, 255, 255), 10, 45)
    draw_rect(slider_pos_blue - 3, 330 - 7.5, (255, 255, 255), 10, 45)

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

def draw_brushes_and_set_colours(access_file_name, tool_selected):

    pen_colour = (80, 109, 136)
    bucket_colour = (80, 109, 136)
    colour_picker_colour = (80, 109, 136)
    brush_colour = (80, 109, 136)

    if tool_selected == PEN:
        pen_colour = (136, 10, 232)

    elif tool_selected == AUTO_FILL:
        bucket_colour = (0, 192, 192)

    elif tool_selected == FILL:
        bucket_colour = (136, 10, 232)
    
    elif tool_selected == COLOUR_PICKER:
        colour_picker_colour = (136, 10, 232)

    elif tool_selected == BRUSH:
        brush_colour = (136, 10, 232)

    # draws the boxes around the tools
    draw_rect(25, 475, (244, 234, 87), 65, 65)
    draw_rect(30, 480, pen_colour, 55, 55)

    draw_rect(115, 475, (244, 234, 87), 65, 65)
    draw_rect(120, 480, bucket_colour, 55, 55)

    draw_rect(25, 565, (244, 234, 87), 65, 65)
    draw_rect(30, 570, colour_picker_colour, 55, 55)

    draw_rect(115, 565, (244, 234, 87), 65, 65)
    draw_rect(120, 570, brush_colour, 55, 55)

    # bin
    draw_rect(1060, 135, (244, 234, 87), 105, 105)
    draw_rect(1065, 140, (80, 109, 136), 95, 95)

    # save
    # draw_rect(1060, 135, (244, 234, 87), 65, 65)
    # draw_rect(1065, 140, (110, 139, 166), 55, 55)

    # draws the tool sprites
    # pen
    if tool_selected == PEN:
        draw_sprite(access_file_name, sprite_nums.get("yes_pen"), 35, 485, 6, (45, 52, 92))
    else:
        draw_sprite(access_file_name, sprite_nums.get("not_pen"), 35, 485, 6, (45, 52, 92))

    # fill
    if tool_selected == FILL or tool_selected == AUTO_FILL:
        draw_sprite(access_file_name, sprite_nums.get("yes_fill"), 125, 485, 6, (45, 52, 92))
    else:
        draw_sprite(access_file_name, sprite_nums.get("not_fill"), 125, 485, 6, (45, 52, 92))

    # colour picker
    if tool_selected == COLOUR_PICKER:
        draw_sprite(access_file_name, sprite_nums.get("yes_colour_picker"), 35, 575, 6, (45, 52, 92))
    else:
        draw_sprite(access_file_name, sprite_nums.get("not_colour_picker"), 35, 575, 6, (45, 52, 92))

    # brush
    if tool_selected == BRUSH:
        draw_sprite(access_file_name, sprite_nums.get("yes_brush"), 120, 570, 6, (45, 52, 92))
    else:
        draw_sprite(access_file_name, sprite_nums.get("not_brush"), 120, 570, 6, (45, 52, 92))

    # bin
    draw_sprite(access_file_name, sprite_nums.get("bin"), 1075, 150, 10, (45, 52, 92))

    # draws the boxes of set colours
    for row in range(1, 4):
        for column in range(1, 5):
            draw_rect(row * 100 + 790, column * 100 + 175, (174, 174, 174), 80, 80)
    
    # terqoise: 25x 580y to 60x 615y
    draw_rect(895, 480, (0, 170, 170), 70, 70)
    # orange: 85x 580y to 110x 615y
    draw_rect(995, 480, (255, 135, 0), 70, 70)
    # pink: 145x 580y to 180x 615y
    draw_rect(1095, 480, (255, 164, 255), 70, 70)
    
    # red: 25x 580y to 60x 615y
    draw_rect(895, 280, (255, 0, 0), 70, 70)
    # green: 85x 580y to 110x 615y
    draw_rect(995, 280, (0, 255, 0), 70, 70)
    # blue: 145x 580y to 180x 615y
    draw_rect(1095, 280, (0, 0, 255), 70, 70)

    # yellow: 25x 640y to 60x 675y
    draw_rect(895, 380, (255, 255, 0), 70, 70)
    # purple: 85x 640y to 110x 675y
    draw_rect(995, 380, (220, 0, 220), 70, 70)
    # cyan: 145x 640y to 180x 675y
    draw_rect(1095, 380, (0, 255, 255), 70, 70)

    # black: 25x 640y to 60x 675y
    draw_rect(895, 580, (0, 0, 0), 70, 70)
    # white: 85x 640y to 110x 675y
    draw_rect(995, 580, (255, 255, 255), 70, 70)
    # grey: 145x 640y to 180x 675y
    draw_rect(1095, 580, (128, 128, 128), 70, 70)

def draw_line(startx, starty, endx, endy, colour = (0, 0, 0), width = 1):
    pygame.draw.line(SCREEN, colour, (startx, starty), (endx, endy), width)

def draw_polygon(colour, square_brackets_points):
    pygame.draw.polygon(SCREEN, colour, square_brackets_points)

def draw_rect(x, y, colour, size_x, size_y):
    square = pygame.Rect((x, y, size_x, size_y))
    pygame.draw.rect(SCREEN, colour, square)

def get_slider_colour(original_num, in_tuple, anything = True):
    in_min, in_max, out_min, out_max = in_tuple
    if anything:
        return (original_num - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    return original_num

def type_msg(font, x, y, text, colour):
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    SCREEN.blit(text, text_rect)

def main():

    # foldable list of general variables
    if True:

        clock = pygame.time.Clock()

        t2 = 0

        out_of_range = NO_COLOUR

        # defines the colour slider variables      
        current_colour = (255, 0, 0)
        
        slider_red_pos = 180
        slider_green_pos = 25
        slider_blue_pos = 25

        # defines the grids + rect grids
        selected = (0, 0)

        # full_colour_grid = [[[[0, 0, 0]] * 8 for _ in range(0, 8)] * full_grid_length for _ in range(0, full_grid_length)]
        full_colour_grid = [ 
            [ ( 0, 0, 0 ) ]
            * FULL_GRID_LENGTH
                for _ in range(0, FULL_GRID_LENGTH) 
                ]
        
        # width of the tiles in the side grid

        colour_side_grid = [[(0, 0, 0)] * SIDE_GRID_LENGTH for _ in range(0, SIDE_GRID_LENGTH)]

        access_file_name = 'sprite_map_maker_essential1.json'

        loading = STARTING
        resolved = False

        # which colour is currently selected to be changed and which colour it has been changed to
        slider_change = NO_COLOUR
        slider_change2 = NO_COLOUR
        has_happened = False
        set_colour_change = None

        # defines the brush variables & pngs
        tool_selected = BRUSH
        trying_delete = False

        saved_text = False
        opacity = 255
        t = 255

        cmd = False

        drawing = False

    running = True
    while running:

        if loading != STOPPED:
            resolved = False
            while not resolved:
                if loading == STARTING:
                    file_name = input("if you wish to load a file enter its name, such as 'file.json'. otherwise enter 'new file'\n")
                else:
                    file_name = input("if you wish to load a file enter its name, such as 'file.json'.\n")
                if os.path.exists(file_name):
                    resolved = True
                    # if loading == STARTING:
                    file_created = True
                elif file_name == "new file":
                    resolved = True
                    if loading == STARTING:
                        file_created = False
                elif file_name == "exit" and loading == REDOING:
                    resolved = True
                elif file_name == "exit" and loading == STARTING:
                    running = False
                    resolved = True
                    file_created = False
                else:
                    print("error, please try again")
            if file_created:
                with open(file_name, 'r') as file:
                    python_obj = json.load(file)
                    full_colour_grid = python_obj['contents']
                for num in range(0, 8):
                    for num2 in range(0, 8):
                        colour_side_grid[num][num2] = full_colour_grid[num][num2]
            loading = STOPPED
        if running:
            t2 = t2 + 1
            if t2 == 1500:
                auto_save_map(full_colour_grid, file_created, file_name, opacity, t, saved_text)
                t2 = 0
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
                        opacity, t, saved_text, possible_name, possible_type, possible_full_name = man_save_map(full_colour_grid, file_created, file_name, opacity, t, saved_text)
                        if possible_type != None and possible_name != None:
                            file_name = possible_name
                            print("saved to ", sprite_map_maker_essential2.remove_imperfections(possible_full_name), "!", sep="")

                    if cmd and event.key == pygame.K_l:
                        loading = REDOING

                    if cmd and event.key == pygame.K_BACKSPACE and trying_delete:
                        full_colour_grid = [ [(0, 0, 0)] * FULL_GRID_LENGTH for _ in range(0, FULL_GRID_LENGTH)]
                    
                    if cmd and event.key == pygame.K_BACKSPACE:
                        trying_delete = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LMETA or event.key == pygame.K_RMETA:
                        cmd = False
                        trying_delete = False

                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN or out_of_range != NO_COLOUR or drawing:

                        # changes the colour in the colour bars
                        if out_of_range == RED_COLOUR or event.type == pygame.MOUSEBUTTONDOWN:
                            # red
                            if (mouse_pos[0] >= 25 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 210 and mouse_pos[1] <= 240):
                                slider_change = RED_COLOUR
                        if out_of_range == GREEN_COLOUR or event.type == pygame.MOUSEBUTTONDOWN:
                            # green
                            if (mouse_pos[0] >= 25 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 270 and mouse_pos[1] <= 300):
                                slider_change = GREEN_COLOUR
                        if out_of_range == BLUE_COLOUR or event.type == pygame.MOUSEBUTTONDOWN:
                            # blue
                            if (mouse_pos[0] >= 25 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 330 and mouse_pos[1] <= 360):
                                slider_change = BLUE_COLOUR
                        
                        
                        if out_of_range == NO_COLOUR:

                            # changes the side grid using whatever tool is selected
                            if (mouse_pos[0] >= 25 and mouse_pos[0] <= 184) and (mouse_pos[1] >= 28 and mouse_pos[1] <= 186):
                                collider_row = int((mouse_pos[0] - 25) / 20)
                                collider_col = int((mouse_pos[1] - 28) / 20)

                                if tool_selected == PEN or tool_selected == BRUSH:
                                    selec_row = int(collider_row + (selected[0]) * SPRITE_LENGTH)
                                    selec_col = int(collider_col + (selected[1]) * SPRITE_LENGTH)

                                    colour_side_grid[collider_row][collider_col] = current_colour
                                    full_colour_grid[selec_row][selec_col] = current_colour

                                    if tool_selected == BRUSH:
                                        drawing = True

                                elif tool_selected == COLOUR_PICKER:
                                    current_colour = colour_side_grid[collider_row][collider_col]
                                    slider_red_pos = get_slider_colour(current_colour[0], (0, 255, 25, 180), True)
                                    slider_green_pos = get_slider_colour(current_colour[1], (0, 255, 25, 180), True)
                                    slider_blue_pos = get_slider_colour(current_colour[2], (0, 255, 25, 180), True)
                                    tool_selected = BRUSH

                                elif tool_selected == FILL:
                                    colour_side_grid = [[current_colour] * SIDE_GRID_LENGTH for _ in range(0, SIDE_GRID_LENGTH)]
                                    selec_row = selected[0] * SPRITE_LENGTH
                                    selec_col = selected[1] * SPRITE_LENGTH
                                    for num in range(0, SPRITE_LENGTH):
                                        for num2 in range(0, SPRITE_LENGTH):
                                            full_colour_grid[selec_row + num][selec_col + num2] = current_colour
                            
                            if not drawing:
                                # changes the current sprite selected
                                if (mouse_pos[0] >= 221 and mouse_pos[0] <= 860) and (mouse_pos[1] >= 23 and mouse_pos[1] <= 660):
                                    collider_row = int((mouse_pos[0] - 221) / 80)
                                    collider_col = int((mouse_pos[1] - 23) / 80)

                                    selected = collider_row, collider_col
                                    for row in range(0, 8):
                                        for col in range(0, 8):
                                            grid_row = collider_row * 8 + row
                                            grid_col = collider_col * 8 + col
                                            if tool_selected == AUTO_FILL:
                                                full_colour_grid[grid_row][grid_col] = current_colour
                                            colour_side_grid[row][col] = full_colour_grid[grid_row][grid_col]

                                # deletes the current sprite selected if the bin is clicked
                                elif mouse_pos[0] >= 1061 and mouse_pos[0] < 1164 and mouse_pos[1] > 138 and mouse_pos[1] < 241:
                                    colour_side_grid = [[(0, 0, 0)] * SIDE_GRID_LENGTH for _ in range(0, SIDE_GRID_LENGTH)]
                                    selec_row = selected[0] * SPRITE_LENGTH
                                    selec_col = selected[1] * SPRITE_LENGTH
                                    for num in range(0, SPRITE_LENGTH):
                                        for num2 in range(0, SPRITE_LENGTH):
                                            full_colour_grid[selec_row + num][selec_col + num2] = (0, 0, 0)
                                
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

                                # changes the selected tool to whatever tool is pressed
                                # fill/bucket tool
                                elif (mouse_pos[0] >= 116 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 478 and mouse_pos[1] <= 541):
                                    if tool_selected == FILL:
                                        tool_selected = AUTO_FILL
                                    else:
                                        tool_selected = FILL
                                # pen tool
                                elif (mouse_pos[0] >= 26 and mouse_pos[0] <= 89) and (mouse_pos[1] >= 478 and mouse_pos[1] <= 541):
                                    tool_selected = PEN
                                # colour picker tool
                                elif (mouse_pos[0] >= 26 and mouse_pos[0] <= 89) and (mouse_pos[1] >= 567 and mouse_pos[1] <= 631):
                                    tool_selected = COLOUR_PICKER
                                # brush tool
                                elif (mouse_pos[0] >= 116 and mouse_pos[0] <= 180) and (mouse_pos[1] >= 567 and mouse_pos[1] <= 631):
                                    tool_selected = BRUSH

                if event.type == pygame.MOUSEBUTTONUP:
                    slider_change2 = NO_COLOUR
                    slider_change = NO_COLOUR
                    out_of_range = NO_COLOUR
                    has_happened = False
                    drawing = False

                if (mouse_pos[0] < 25 or mouse_pos[0] > 180) and slider_change != NO_COLOUR:
                    if mouse_pos[0] < 25:
                        if slider_change == RED_COLOUR:
                            slider_red_pos = 25
                        elif slider_change == GREEN_COLOUR:
                            slider_green_pos = 25
                        elif slider_change == BLUE_COLOUR:
                            slider_blue_pos = 25
                    else:
                        if slider_change == RED_COLOUR:
                            slider_red_pos = 180
                        elif slider_change == GREEN_COLOUR:
                            slider_green_pos = 180
                        elif slider_change == BLUE_COLOUR:
                            slider_blue_pos = 180

                    if has_happened:
                        slider_change2 = slider_change
                    has_happened = True
                    slider_change = NO_COLOUR
                    out_of_range = slider_change2

            SCREEN.fill((45, 52, 92))
            pygame.display.set_caption('Sprite Map Maker')

            if mouse_pos == None:
                mouse_pos = pygame.mouse.get_pos()
            
            # --display from here onward!--                                                 # --display from here onward!--                                                  # --display from here onward!--

            if saved_text:
                t = t - 1.5

                if t < 128:
                    opacity = int(t) + 55
                
                if t == -30:
                    saved_text = False
                    t = 255
                draw_opacity_text(900, 20, "saved!", (0, 0, 0), 40, opacity)
            
            print

            if trying_delete and not saved_text:
                draw_centered_text(1000, 20, "press command +", (0, 0, 0), 20)
                draw_centered_text(1000, 40, "delete again to confirm", (0, 0, 0), 20)
                draw_centered_text(1000, 60, "delete or let go of", (0, 0, 0), 20)
                draw_centered_text(1000, 80, "command to cancel", (0, 0, 0), 20)

            # draws the currently selected colour in a box below the side grid
            draw_rect(75, 370, (244, 234, 87), 60, 60)
            draw_rect(80, 375, current_colour, 50, 50)

            # draws the colour bars
            slider_red_pos, slider_green_pos, slider_blue_pos, current_colour = draw_colour_bar(slider_red_pos, slider_green_pos, slider_blue_pos, current_colour, mouse_pos, slider_change, set_colour_change)

            # draws the grids
            sprite_map_maker_essential2.main(colour_side_grid, current_colour, full_colour_grid, FULL_GRID_LENGTH, SCREEN, selected, SIDE_GRID_LENGTH)

            draw_brushes_and_set_colours(access_file_name, tool_selected)
            clock.tick(30)
            pygame.display.update()
            
        pygame.quit


main()