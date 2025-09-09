import pygame
from icecream import ic

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

NO_COLOUR = 0
RED_COLOUR = 1
GREEN_COLOUR = 2
BLUE_COLOUR = 3

SIDE_GRID_LENGTH = 8

def display_full_grid(grid_full, grid_length, deepness, screen, steepness):
    defined = False
    for row in range(0, 8):
        for col in range(0, 8):
            if grid_full[row][col] == False:
                if not defined:
                    true_rectxy = None
                    # (screen, (0-8 * 20) + 25, 0-8 * 20 + 15, the colour black, 20, 20)
                    # draws 80 p by 80 p rects
                draw_rect(screen, row*grid_length+deepness, col * grid_length + steepness, (0, 0, 0), grid_length, grid_length)
            
            else:
                # draws a box around the currently selected position
                defined = True
                true_rectxy = (row, col)

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

def draw_colour_bar(slider_pos_red, slider_pos_green, slider_pos_blue, current_colour, mouse_pos, colour_change, screen):
    for row in range(25, 185):
        draw_rect(screen, row, 210, (row, 0, 0), 1, 30)
        draw_rect(screen, row, 270, (0, row, 0), 1, 30)
        draw_rect(screen, row, 330, (0, 0, row), 1, 30)

    # sets the slider bar to wherver you press on it and the colour to where it is on the bar
    if colour_change != 0:
        # red
        if colour_change == 1:
            slider_pos_red = mouse_pos[0]
            colour_red = get_slider_colour(slider_pos_red)
            current_colour = (colour_red, current_colour[1], current_colour[2])
        # green
        elif colour_change == 2:
            slider_pos_green = mouse_pos[0]
            colour_green = get_slider_colour(slider_pos_green)
            current_colour = (current_colour[0], colour_green, current_colour[2])
        # blue
        elif colour_change == 3:
            slider_pos_blue = mouse_pos[0]
            colour_blue = get_slider_colour(slider_pos_blue)
            current_colour = (current_colour[0], current_colour[1], colour_blue)
    
    draw_rect(screen, slider_pos_red - 3, 210 - 7.5, (255, 255, 255), 10, 45)
    draw_rect(screen, slider_pos_green - 3, 270 - 7.5, (255, 255, 255), 10, 45)
    draw_rect(screen, slider_pos_blue - 3, 330 - 7.5, (255, 255, 255), 10, 45)

    return slider_pos_red, slider_pos_green, slider_pos_blue, current_colour

def draw_brushes(screen, screen_width, brush_png, bucket_png, tool_selected):
    # draws the brush and the fill bucket
    if tool_selected == "brush":
        None
        # draw_rect()
    elif tool_selected == "bucket":
        None
        # draw_rect()
    screen.blit(brush_png, (screen_width / 2 - 225, 0))
    screen.blit(bucket_png, (screen_width / 2 - 225, 0))

def draw_line(screen, startx, starty, endx, endy, colour = (0, 0, 0), width = 1):
    pygame.draw.line(screen, colour, (startx, starty), (endx, endy), width)

def draw_polygon(screen, colour, square_brackets_points):
    pygame.draw.polygon(screen, colour, square_brackets_points)

# draws a coloured rectange on the screen
def draw_rect(screen, x, y, colour, size_x, size_y):
    square = pygame.Rect((x, y, size_x, size_y))
    pygame.draw.rect(screen, colour, square)

def get_slider_colour(original_colour):
    new_colour = int((original_colour - 24) * 1.58)
    return new_colour

# displays coloured text on the screen
def type_msg(screen, font, x, y, text, colour):
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

def main():

    # foldable list of general variables
    if True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
        rect_grid = get_grid_rects(RECT_grid_full, RECT_full_grid_length * 9, 215)

        # which colour is currently selected to be changed
        colour_change = NO_COLOUR

        # width of the tiles in the side grid

        colour_side_grid = [[(0, 0, 0)] * SIDE_GRID_LENGTH for _ in range(0, SIDE_GRID_LENGTH)]

        # defines the brush variables & pngs
        tool_selected = "brush"
        brush_png = None
        bucket_png = None

    running = True
    while running:

        mouse_pos = None

        key = pygame.key.get_pressed()

        for event in pygame.event.get():

            # if escape or quit, ends the while loop which leads to the game quiting
            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False

            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse position is in range of the larger grid then it checks where in it,
                # sets that place to selected, and sets all other places to unselected
                ic(mouse_pos)
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

                # displays the colour bars
                # red
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 185) and (mouse_pos[1] >= 210 and mouse_pos[1] <= 240):
                    colour_change = RED_COLOUR
                # green
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 185) and (mouse_pos[1] >= 270 and mouse_pos[1] <= 300):
                    colour_change = GREEN_COLOUR
                # blue
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 185) and (mouse_pos[1] >= 330 and mouse_pos[1] <= 360):
                    colour_change = BLUE_COLOUR

            if event.type == pygame.MOUSEBUTTONUP or mouse_pos[0] <= 25 or mouse_pos[0] >= 185:
                colour_change = NO_COLOUR

        screen.fill((45, 52, 92))

                                    # --display from here onward!--

        if mouse_pos == None:
            mouse_pos = pygame.mouse.get_pos()

        # draws the currently selected colour in a box below the side grid
        draw_rect(screen, 75, 370, (244, 234, 87), 60, 60)
        draw_rect(screen, 80, 375, current_colour, 50, 50)

        # draws the colour bars
        slider_red_pos, slider_green_pos, slider_blue_pos, current_colour = draw_colour_bar(slider_red_pos, slider_green_pos, slider_blue_pos, current_colour, mouse_pos, colour_change, screen)

        # draws the main grid
        true_rectxy_tuple = display_full_grid(grid_full, full_grid_length * 10, 215, screen, 15)

        # draws the grid on the side of the screen
        display_side_grid(colour_side_grid, SIDE_GRID_LENGTH * 2.5, 25, screen, 25)
        # draw_brushes(screen, screen_width, brush_png, bucket_png, tool_selected)

        pygame.display.update()

    pygame.quit



main()