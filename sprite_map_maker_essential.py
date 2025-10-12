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

def draw_full_grid(screen, startposx, startposy, tile_size, full_colour_grid, row2, col2, wowow = False):

    for row in range(0, 8):
        for col in range(0, 8):
            # print (full_colour_grid[0])
            # print("")
            if wowow:
                draw_rect(screen, startposx + (row * (tile_size * 2) + tile_size), startposy + (col * (tile_size*2) + tile_size), full_colour_grid[row][col], tile_size * 2, tile_size * 2)
            else:
                colrow = row2 * 8 + row
                colcol = col2 * 8 + col
                draw_rect(screen, startposx + (row * (tile_size * 2) + tile_size), startposy + (col * (tile_size*2) + tile_size), full_colour_grid[colrow][colcol], tile_size * 2, tile_size * 2)

def display_full_grid(selected, grid_length, deepness, screen, steepness, full_colour_grid):
    for row in range(0, 8):
        for col in range(0, 8):
            draw_full_grid(screen, row*grid_length+deepness, col*grid_length+steepness, 5, full_colour_grid, row, col)

        draw_rect(screen, selected[0]*grid_length+deepness+2, selected[1] * grid_length + steepness +2, (255, 255, 255), grid_length + 6, grid_length + 6)
        draw_full_grid(screen, (selected[0])*grid_length+deepness, selected[1]*grid_length+steepness, 5, full_colour_grid, selected[0], selected[1])

def main(colour_side_grid, current_colour, full_colour_grid, full_grid_length, screen, selected):
    
    draw_rect(screen, 75, 370, (244, 234, 87), 60, 60)
    draw_rect(screen, 80, 375, current_colour, 50, 50)

    display_full_grid(selected, full_grid_length * 10 / 8, 215, screen, 15, full_colour_grid)
    display_side_grid(colour_side_grid, SIDE_GRID_LENGTH * 2.5, 25, screen, 25)