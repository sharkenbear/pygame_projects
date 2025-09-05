import pygame
import random
import sys
pygame.init()
class Block:
    def __init__(self, width, height):
        self.should_reset = False
        self.width = width
        self.height = height
        self.buf = [[0] * width for _ in range(height)]
    
    def draw_lines(self, screen):
            display_square(screen, 318, 25, (255, 0, 0), 25, 534)
            display_square(screen, 25, 25, (255, 0, 0), 25, 532)
            display_square(screen, 25, 534, (255, 0, 0), 319, 25)
            display_square(screen, 25, 25, (255, 0, 0), 318, 25)
            pygame.draw.line(screen, (0, 0, 0), (25, 558), (25, 25))
            pygame.draw.line(screen, (0, 0, 0), (343, 558), (343, 25))
            pygame.draw.line(screen, (0, 0, 0), (343, 558), (25, 558))
            pygame.draw.line(screen, (0, 0, 0), (25, 25), (343, 25))

            pygame.draw.line(screen, (0, 0, 0), (50, 533), (50, 50))
            pygame.draw.line(screen, (0, 0, 0), (318, 533), (318, 50))
            pygame.draw.line(screen, (0, 0, 0), (318, 533), (50, 533))

            pygame.draw.line(screen, (0, 0, 0), (50, 50), (318, 50))
            # pygame.draw.line(screen, colour, start_pos_x-y, end_posx-y, width = 1)
    
    def print(self, screen, tetrominoe_type_num, future_type_num, merge_total, level, font, tet = None):

        # draws it in the terminal
        if True:
            None
            # for y in range(0, 18):
            #     for x in range(0, 10):
            #         row = int(y) - tet.y
            #         col = int(x) - tet.x
            #         if tet != None and (row >= 0 and row < 4) and (col >= 0 and col < 4):
            #             if tet.tetrominoe[row][col] != 0:
            #                 print(tet.tetrominoe[row][col], end='|')
            #             else:
            #                 print(self.buf[int(y)][int(x)], end='|')
            #         else:
            #             print(self.buf[int(y)][int(x)], end='|')
            #     print('')
            # print("")
        
        # draws it in the screen
        if True:
            square_colour = self.find_colour(tetrominoe_type_num)
            future_square_colour = self.find_colour(future_type_num)

            # draws next tetrominoe
            x_num = -1
            for x1 in range(400, 520, 30):
                x_num = x_num + 1
                y_num = -1
                for y1 in range(400, 520, 30):
                    y_num = y_num + 1
                    if tet.future_tetrominoe[y_num][x_num] > 0:
                        display_square(screen, x1, y1, future_square_colour, 25, 25)
                    else:
                        display_square(screen, x1, y1, (255, 255, 255), 25, 25)
        
            # draws the current level
            type_msg(screen, font, 450, 250, "LEVEL", (255, 255, 255))
            type_msg(screen, font, 465, 280, level, (255, 255, 255))

            # draws the number of lines
            type_msg(screen, font, 450, 320, "LINES", (255, 255, 255))
            type_msg(screen, font, 465, 350, merge_total, (255, 255, 255))
            
            # draws the grid
            for y in range(0, 18):
                for x in range(0, 10):
                    row = y - tet.y
                    col = x - tet.x
                    if tet != None and (row >= 0 and row < 4) and (col >= 0 and col < 4):
                        if tet.tetrominoe[row][col] != 0:
                            display_square(screen, int((x * 27) + 50), (y * 27) + 50, square_colour, 25, 25)
                        else:
                            if self.buf[y][x] > 0:
                                grid_colour = self.find_colour(self.buf[y][x] - 1)
                                display_square(screen, int((x * 27) + 50), (y * 27) + 50, grid_colour, 25, 25)
                            else:
                                display_square(screen, int((x * 27) + 50), (y * 27) + 50, (255, 255, 255), 25, 25)
                    else:
                        if self.buf[y][x] > 0:
                            grid_colour = self.find_colour(self.buf[y][x] - 1)
                            display_square(screen, int((x * 27) + 50), (y * 27) + 50, grid_colour, 25, 25)
                        else:
                            display_square(screen, int((x * 27) + 50), (y * 27) + 50, (255, 255, 255), 25, 25)
            
            # draws the boxes around the grid
            self.draw_lines(screen)
    
    def find_colour(self, num):
        if num == 0:
            square_colour = (240, 240, 0)
        if num == 1:
            square_colour = (8, 240, 240)
        if num == 2:
            square_colour = (160, 0, 240)
        if num == 3:
            square_colour = (8, 240, 0)
        if num == 4:
            square_colour = (240, 0, 0)
        if num == 5:
            square_colour = (0, 0, 240)
        if num == 6:
            square_colour = (240, 160, 0)
        return square_colour
    
    def add_falling_grid(self, block1, ptrominoe, yp, xp):
        for y in range(0, 4):
            for x in range(0, 4):
                if ptrominoe[y][x] != 0:
                    block1.buf[yp + y][xp + x] = ptrominoe[y][x]
        return block1
    
    def merge(self, grid, width, merged_total):

        merge_happened = False
        merged = 0
        num = 0
        reset_num = False

        for row in grid:
            if reset_num:
                num = 0
                reset_num = False
            num = num + 1
            merged = 0
            if row.count(0) == 0:
                merge_happened = True
                grid[num - 1] = [0] * width
                merged = merged + 1
                merged_total = merged_total + 1
                for _ in range(0, merged):
                    for row2 in range(17, -1, -1):
                        if row2 == num - 1:
                            if row2 == 0:
                                grid[row2] = [0] * width
                            else:
                                grid[row2] = grid[row2 -1]
                            num = num - 1
                            reset_num = True

        return grid, merge_happened, merged_total

class Array:
    def __init__(self, tetroid_type_num, future_type_num, rotate, reset, d, a):
        self.future_tetrominoe = rotate_clockwise(future_type_num, 0)
        self.tetrominoe = rotate_clockwise(tetroid_type_num, rotate)
        if reset:
            self.y = 0
            self.x = 3
        else:
            self.y = d
            self.x = a
    
    def collision_check(self, falling_grid, px, py, tet_tetrominoe):
        for y in range(0, 4):
            for x in range(0, 4):
                row = py + y
                col = px + x
                if tet_tetrominoe[y][x] != 0:
                        if row < 0 or row >= 18 or col < 0 or col >= 10:
                            return True
                        if row < 18 and col >= 0 and col < 10 and falling_grid.buf[row][col] != 0:
                            return True
        return False
    
    def check_rotate(self, rotate, px2, grid, py2, tetroid_type_num):
        rotated_p = rotate_clockwise(tetroid_type_num, rotate)
        if not self.collision_check(grid, px2, py2, rotated_p):
            return True
        return False
    
    def move_down(self, falling_grid):
        if not self.collision_check(falling_grid, self.x, self.y + 1, self.tetrominoe):
            self.y = self.y + 1
            return True
        return False
    
    def move_left(self, falling_grid):
        if not self.collision_check(falling_grid, self.x - 1, self.y, self.tetrominoe):
            self.x = self.x - 1
            return True
        return False
    
    def move_right(self, falling_grid):
        if not self.collision_check(falling_grid, self.x + 1, self.y, self.tetrominoe):
            self.x = self.x + 1
            return True
        return False

def display_polygon(screen, colour, square_brackets_points):
    pygame.draw.polygon(screen, colour, square_brackets_points)

def type_msg(screen, font, x, y, text, colour):
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

def display_square(screen, x, y, colour, size_x, size_y):
    square = pygame.Rect((x, y, size_x, size_y))
    pygame.draw.rect(screen, colour, square)

def place_block(future_type_num):
    if future_type_num == -1:
        tetroid_type_num = random.randint(0, 6)
    else:
        tetroid_type_num = future_type_num
    future_type_num = random.randint(0, 6)
    # 0 = O
    # 1 = I
    # 2 = T
    # 3 = S
    # 4 = Z
    # 5 = J
    # 6 = L
    return tetroid_type_num, future_type_num

def rotate_clockwise(tetroid_type_num, rotate):
    array = []

    if tetroid_type_num == 0:
        array = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
            ]
    elif tetroid_type_num == 1:
        if rotate == 0 or rotate == 2:
            array = [
                [0, 0, 0, 0],
                [2, 2, 2, 2],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 1 or rotate == 3:
            array = [
                [0, 2, 0, 0],
                [0, 2, 0, 0],
                [0, 2, 0, 0],
                [0, 2, 0, 0]
                ]
    elif tetroid_type_num == 2:
        if rotate == 0:
            array = [
                [0, 3, 0, 0],
                [3, 3, 3, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 1:
            array = [
                [0, 3, 0, 0],
                [0, 3, 3, 0],
                [0, 3, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 2:
            array = [
                [0, 0, 0, 0],
                [3, 3, 3, 0],
                [0, 3, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 3:
            array = [
                [0, 3, 0, 0],
                [3, 3, 0, 0],
                [0, 3, 0, 0],
                [0, 0, 0, 0]
                ]
    elif tetroid_type_num == 3:
        if rotate == 0 or rotate == 2:
            array = [
                [0, 0, 0, 0],
                [0, 4, 4, 0],
                [4, 4, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 1 or rotate == 3:
            array = [
                [4, 0, 0, 0],
                [4, 4, 0, 0],
                [0, 4, 0, 0],
                [0, 0, 0, 0]
                ]
    elif tetroid_type_num == 4:
        if rotate == 0 or rotate == 2:
            array = [
                [0, 0, 0, 0],
                [5, 5, 0, 0],
                [0, 5, 5, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 1 or rotate == 3:
            array = [
                [0, 5, 0, 0],
                [5, 5, 0, 0],
                [5, 0, 0, 0],
                [0, 0, 0, 0]
                ]
    elif tetroid_type_num == 5:
        if rotate == 0:
            array = [
                [0, 0, 0, 0],
                [6 ,6, 6, 0],
                [0, 0, 6, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 1:
            array = [
                [0, 6, 0, 0],
                [0, 6, 0, 0],
                [6, 6, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 2:
            array = [
                [6, 0, 0, 0],
                [6, 6, 6, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 3:
            array = [
                [0, 6, 6, 0],
                [0, 6, 0, 0],
                [0, 6, 0, 0],
                [0, 0, 0, 0]
                ]
    elif tetroid_type_num == 6:
        if rotate == 0:
            array = [
                [0, 0, 0, 0],
                [7, 7, 7, 0],
                [7, 0, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 1:
            array = [
                [7, 7, 0, 0],
                [0, 7, 0, 0],
                [0, 7, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 2:
            array = [
                [0, 0, 7, 0],
                [7, 7, 7, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
                ]
        if rotate == 3:
            array = [
                [0, 7, 0, 0],
                [0, 7, 0, 0],
                [0, 7, 7, 0],
                [0, 0, 0, 0]
                ]

    return array

def add_array(tetroid_type_num, falling_grid, rotate, corner):

    array = rotate_clockwise(tetroid_type_num, rotate)

    falling = True

    if corner == 14:
        print("ajbfug0s08ufh0aufadfoauhfduabdfuhb0yebu1b08708374631807356018736508")
        corner = 13
        falling = False

    for y in range(corner + 1, corner + 5):
        z = y - corner
        for x in range(3, 7):
            falling_grid[y][x] = array[z - 1][x - 3]

    return falling_grid, corner, falling

def fall_grid(grid, falling_grid, fall, falling, corner):
    row = 17
    corner_add = False
    if falling:
        while row > 0:
            for column in range(0, 10):
                if falling_grid[row][column] > 0:
                    if fall:
                        corner_add = True
                        if row + 1 == 18 or falling_grid[row + 1][column] != 0:
                            falling = False
                            row = 0
                        else:
                            unfallen_value = falling_grid[row][column]
                            falling_grid[row][column] = 0
                            falling_grid[row + 1][column] = unfallen_value
            row = row - 1
    if corner_add:
        corner = corner + 1
    return grid, falling, corner

def main():

    # defines everything in main
    if True:
        level = 0
        merge_num = 0
        LOADING_STATE = 0
        START_BUTTON_STATE = 1
        SETTING_STATE_ONE = 2
        SETTING_STATE_TWO = 3
        PLAYING_STATE = 4
        LOSE_STATE = 5
        state = LOADING_STATE
        FONT = pygame.font.Font("./Grand9K Pixel.ttf", 18)
        LARGER_FONT = pygame.font.Font("./Grand9K Pixel.ttf", 25)
        KINDA_BIG_FONT = pygame.font.Font("./Grand9K Pixel.ttf", 50)
        REALLY_BIG_FONT = pygame.font.Font("./Grand9K Pixel.ttf", 75)
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        logo = pygame.image.load("./tetris_logo.png").convert()
        two_players = False
        clock = pygame.time.Clock()
        start = False
        falling = False
        t = -15
        rotate = 0
        b1 = Block(10, 18)
        show_screen = True
        rotate_bool = False
        timer_max = 30
        p = Array(1, 1, 0, True, 1, 3)
        merge_happened = False
        future_type_num = -1

        running = True

    # while loop
    while running:
        level = int(merge_num  / 10)
        return_pressed = False
        x_change = False
        rotate_bool = False

        key = pygame.key.get_pressed()

        # checks for the current state, and then checks for inputs
        for event in pygame.event.get():
            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False
            if key[pygame.K_RETURN]:
                start = True
            if state == START_BUTTON_STATE:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        state = SETTING_STATE_ONE
                    if event.key == pygame.K_RIGHT:
                        two_players = True
                    elif event.key == pygame.K_LEFT:
                        two_players = False
            if state == SETTING_STATE_ONE:
                if key[pygame.K_RETURN]:
                    state = SETTING_STATE_TWO
            if state == SETTING_STATE_TWO:
                if key[pygame.K_RETURN]:
                    state = PLAYING_STATE
                    grid = [[0] * 10 for _ in range(0, 18)]
            if state == PLAYING_STATE:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        new_rotate = rotate + 1
                        if new_rotate > 3:
                            new_rotate = 0
                        if p.check_rotate(new_rotate, p.x, b1, p.y, tetroid_type_num):
                            rotate = rotate + 1
                            rotate_bool = True
                            if rotate > 3:
                                rotate = 0
                    if event.key == pygame.K_x:
                        new_rotate = rotate - 1
                        if new_rotate < 0:
                            new_rotate = 3
                        if p.check_rotate(new_rotate, p.x, b1, p.y, tetroid_type_num):
                            rotate = rotate - 1
                            rotate_bool = True
                            if rotate < 0:
                                rotate = 3

                    if event.key == pygame.K_9:
                        state = LOSE_STATE

                    if event.key == pygame.K_LEFT:
                        if p.move_left(b1):
                            x_change = True
                    if event.key == pygame.K_RIGHT:
                        if p.move_right(b1):
                            x_change = True
                    if event.key == pygame.K_DOWN:
                        timer_max = 1
                else:
                    timer_max = 30
            if state == LOSE_STATE:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return_pressed = True
        if show_screen:
            screen.fill((196, 207, 161))
        if state == LOADING_STATE:
            type_msg(screen, FONT, screen_width / 2, screen_height / 3, "Tetris © 1985~2025 Tetris Holding.", (65, 65, 65))
            type_msg(screen, FONT, screen_width / 2, screen_height / 2.7, "Tetris logos, Tetris theme song and Tetriminos are trademarks of Tetris Holding.", (65, 65, 65))
            type_msg(screen, FONT, screen_width / 2, screen_height / 2.49, "The Tetris trade dress is owned by Tetris Holding.", (65, 65, 65))
            type_msg(screen, FONT, screen_width / 2, screen_height / 2.29, "Licensed to The Tetris Company.", (65, 65, 65))
            type_msg(screen, FONT, screen_width / 2, screen_height / 2.12, "Tetris Game Design by Alexey Pajitnov.", (65, 65, 65))
            type_msg(screen, FONT, screen_width / 2, screen_height / 1.95, "Tetris Logo Design by Roger Dean.", (65, 65, 65))
            type_msg(screen, FONT, screen_width / 2, screen_height / 1.1, "All Rights Reserved.", (65, 65, 65))
            if start:
                state = START_BUTTON_STATE
        elif state == START_BUTTON_STATE:
            screen.fill((196, 207, 161))
            screen.blit(logo, (screen_width / 2 - 225, 0))
            display_square(screen, 0, screen_height / 1.5, (255, 255, 255), screen_width, screen_height / 3)
            display_square(screen, screen_width / 4 - 80, screen_height / 1.2 + 14, (164, 162, 165), 163, 4)
            display_square(screen, screen_width / 1.33 - 80, screen_height / 1.2 + 14, (164, 162, 165), 163, 4)
            type_msg(screen, LARGER_FONT, screen_width / 4, screen_height / 1.2, "1 PLAYER", (0, 0, 0))
            type_msg(screen, LARGER_FONT, screen_width / 1.33, screen_height / 1.2, "2 PLAYER", (0, 0, 0))
            if not two_players:
                display_polygon(screen, (0, 0, 0), [(80, 485), (80, 515), (105, 500)])
            else:
                display_polygon(screen, (0, 0, 0), [(480, 485), (480, 515), (505, 500)])
        elif state == SETTING_STATE_ONE:
            if not two_players:
                type_msg(screen, LARGER_FONT, 400, 300, "One player!", (0, 0, 0))
            else:
                type_msg(screen, LARGER_FONT, 400, 300, "Two players!", (0, 0, 0))
        elif state == SETTING_STATE_TWO:
            if not two_players:
                type_msg(screen, LARGER_FONT, 400, 300, "One player!", (0, 0, 0))
            else:
                type_msg(screen, LARGER_FONT, 400, 300, "Two players!", (0, 0, 0))
        elif state == PLAYING_STATE:
            show_screen = False
            if not two_players:
                None
                # type_msg(screen, LARGER_FONT, 400, 300, "One player!", (0, 0, 0))
            else:
                None
                # type_msg(screen, LARGER_FONT, 400, 300, "Two players!", (0, 0, 0))
            if not falling:
                tetroid_type_num, future_type_num = place_block(future_type_num)
                rotate = 0
                rotate_bool = True
                falling = True
                p = Array(tetroid_type_num, future_type_num, rotate, True, 0, 3)
            p = Array(tetroid_type_num, future_type_num, rotate, False, p.y, p.x)
            t = t + 1
            if t > timer_max:
                t = 0
            # moves tries to move current tetroid down, if its at the bottom resets
            # refresh the screen
            if t == timer_max or rotate_bool or x_change or merge_happened:
                if t == timer_max:
                    if not p.move_down(b1):
                        b1 = b1.add_falling_grid(b1, p.tetrominoe, p.y, p.x)
                        falling = False
                screen.fill((0, 0, 0))
                b1.print(screen, tetroid_type_num, future_type_num, merge_num, level, LARGER_FONT, p)
                merge_happened = False
            
            b1.buf, merge_happened, merge_num = b1.merge(b1.buf, 10, merge_num)
        elif state == LOSE_STATE:
            screen.fill((255, 255, 255))
            type_msg(screen, REALLY_BIG_FONT, 400, 150, "GAME OVER", (0, 0, 0))
            type_msg(screen, KINDA_BIG_FONT, 300, 350, "PLEASE", (0, 0, 0))
            type_msg(screen, KINDA_BIG_FONT, 350, 420, "TRY", (0, 0, 0))
            type_msg(screen, KINDA_BIG_FONT, 400, 490, "AGAIN", (0, 0, 0))
            if return_pressed:
                state = START_BUTTON_STATE

        pygame.display.flip()
        clock.tick(30)
    pygame.QUIT
main()