import pygame
from icecream import ic

pygame.init()

SIDE_GRID_LENGTH = 8
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

def display_side_grid(grid, grid_length, deepness, screen, steepness):
    for row in range(0, 8):
        for col in range(0, 8):
            # draws 20 by 20 rects
            draw_rect(screen, row*grid_length+deepness, col * grid_length + steepness, grid[row][col], grid_length, grid_length)

def draw_rect(screen, x, y, colour, size_x, size_y):
    square = pygame.Rect((x, y, size_x, size_y))
    pygame.draw.rect(screen, colour, square)

def draw_full_grid(screen, startposx, startposy, tile_size, full_colour_grid):

    for row in range(0, 8):
        for column in range(0, 8):
            if full_colour_grid[0] == 0:
                print("ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! ERROR!")
                print("")
            else:
                # print(full_colour_grid[0])
                # print("aojnf :)")
                draw_rect(screen, startposx + (row * (tile_size * 2) + tile_size), startposy + (column * (tile_size*2) + tile_size), full_colour_grid[row][column], tile_size * 2, tile_size * 2)

def display_full_grid(selected, grid_length, deepness, screen, steepness, full_colour_grid):
    for row in range(0, 8):
        for col in range(0, 8):
            # print(full_colour_grid[0])
            # print("am")
            draw_full_grid(screen, row*grid_length+deepness, col*grid_length+steepness, 5, full_colour_grid)

    draw_rect(screen, selected[0]*grid_length+deepness+2, selected[1] * grid_length + steepness +2, (255, 255, 255), grid_length + 6, grid_length + 6)
    draw_full_grid(screen, (selected[0])*grid_length+deepness, selected[1]*grid_length+steepness, 5, full_colour_grid[selected[0]][selected[1]])

def main():
    print()
    current_colour = (0, 0, 255)
    colour_side_grid = [[(0, 0, 0)] * SIDE_GRID_LENGTH for _ in range(0, SIDE_GRID_LENGTH)]
    full_grid_length = 64

    # full_colour_grid = [
    
    #     [
    #         [  (0, 0, 0)  ]
    #         * 8 
    #         for _ in range(0, full_grid_length)
    #     ]
    #     * full_grid_length 
    #     for _ in range(0, full_grid_length)
    # ]

    full_colour_grid = [ [( 0, 0, 0 )] * full_grid_length for _ in range(0, full_grid_length) ]

    selected = (0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    running = True
    while running:

        key = pygame.key.get_pressed()

        for event in pygame.event.get():

            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False

            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_pos[0] >= 25 and mouse_pos[0] <= 185) and (mouse_pos[1] >= 28 and mouse_pos[1] <= 180):

                    collider_row = int((mouse_pos[0] - 25) / 20)
                    collider_col = int((mouse_pos[1] - 28) / 20)

                    colour_side_grid[collider_row][collider_col] = current_colour
                    
                    print("O_o")

        screen.fill((45, 52, 92))

        draw_rect(screen, 75, 370, (244, 234, 87), 60, 60)
        draw_rect(screen, 80, 375, current_colour, 50, 50)


        display_full_grid(selected, full_grid_length * 10 / 8, 215, screen, 15, full_colour_grid)
        display_side_grid(colour_side_grid, SIDE_GRID_LENGTH * 2.5, 25, screen, 25)

        pygame.display.update()

    pygame.quit


main()