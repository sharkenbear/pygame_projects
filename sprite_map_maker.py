import pygame
from icecream import ic

pygame.init()

def display_full_grid(grid, grid_length, deepness, screen, steepness):
    defined = False
    for row in range(0, 8):
        for col in range(0, 8):
            if grid[row][col] == False:
                if not defined:
                    true_rectxy = None
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
            draw_rect(screen, row*grid_length+deepness, col * grid_length + steepness, grid[row][col], grid_length, grid_length)

def get_grid_rects(grid, grid_length, deepness):
    ic(grid_length)
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

def draw_brushes(screen):
    # ((top left), (top right), (bottom right), (bottom left))
    draw_polygon(screen, (0, 0, 0), ((20, 400), (35, 415), (35, 435), (20, 420)))
    # draw_polygon(screen, (0, 0, 0), ((35, 427.5), (60, 447.5), (35, 427.5)))
    draw_line(screen, 35, 420, 60, 410, (0, 0, 0), 3)
    draw_line(screen, 35, 425, 62, 420, (0, 0, 0), 3)
    draw_line(screen, 35, 430, 65, 430, (0, 0, 0), 3)
    # draw_line(screen, 35, 420, 62, 410, (0, 0, 0), 3)
    # draw_line(screen, 35, 420, 60, 410, (0, 0, 0), 3)

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
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))

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

        NO_COLOUR = 0
        RED_COLOUR = 1
        GREEN_COLOUR = 2
        BLUE_COLOUR = 3
        colour_change = NO_COLOUR

        side_grid_length = 8

        colour_side_grid = [[(0, 0, 0)] * side_grid_length for _ in range(0, side_grid_length)]
    
        rect_side_grid = [[(0)] * side_grid_length for _ in range(0, side_grid_length)]
        rect_side_grid = get_grid_rects(rect_side_grid, side_grid_length * 2.5, 25)

    running = True
    while running:

        key = pygame.key.get_pressed()

        colour_change = NO_COLOUR

        for event in pygame.event.get():

            # if escape or quit, ends the while loop which leads to the game quiting
            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

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
                            if pygame.mouse.get_pressed()[0] and rect_side_grid[row][column].collidepoint(mouse_pos):
                                colour_side_grid[row][column] = current_colour

                # displays the colour bars
                # red
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 185) and (mouse_pos[1] >= 210 and mouse_pos[1] <= 240):
                    colour_change = RED_COLOUR
                    ic(mouse_pos, "red")
                # green
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 185) and (mouse_pos[1] >= 270 and mouse_pos[1] <= 300):
                    colour_change = GREEN_COLOUR
                    ic(mouse_pos, "green")
                # blue
                elif (mouse_pos[0] >= 25 and mouse_pos[0] <= 185) and (mouse_pos[1] >= 330 and mouse_pos[1] <= 360):
                    colour_change = BLUE_COLOUR
                    ic(mouse_pos, "blue")

        # screen.fill((0, 9, 141))
        screen.fill((45, 52, 92))

                                    # --display from here onward!--

        mouse_pos = pygame.mouse.get_pos()

        slider_red_pos, slider_green_pos, slider_blue_pos, current_colour = draw_colour_bar(slider_red_pos, slider_green_pos, slider_blue_pos, current_colour, mouse_pos, colour_change, screen)

        true_rectxy_tuple = display_full_grid(grid_full, full_grid_length * 9, 215, screen, 15)

        display_side_grid(colour_side_grid, side_grid_length * 2.5, 25, screen, 25)

        draw_brushes(screen)

        pygame.display.update()

    pygame.quit



main()