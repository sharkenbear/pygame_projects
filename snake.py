import pygame
import random

pygame.init()

class Grid:
    def __init__(self, width, height):
        # defines the base grid variables
        self.width = width
        self.height = height
        self.buf = [[0] * width for _ in range(height)]
        # sets the initial snake and apple position
        # self.buf[y][x] y is how far down, x is how far along
        self.buf[7][2] = 1
        self.buf[7][3] = 2
        self.buf[7][4] = -2
        self.buf[7][12] = -3
    
    def draw_grid(self, screen):
        # draws the whole grid, drawing green if its empty, blue if it has the snake(dark blue for the head) and red for the apples
        # if self.buf (the grid array) is 0 its an empty tile, if its > 0 its the snakes body, if its -2 its the head and if its -3 its a apple
        for row in range(0, 15):
            for column in range(0, 17):

                # draws the base tiles, in a criss cross patern
                if self.buf[row][column] == 0:
                    if (row % 2 != 0 and column % 2 != 0) or (row % 2 == 0 and column % 2 == 0):
                        draw_rect(screen, column * 45 + 15, row * 45 + 100, (170, 215, 80), 45, 45)
                    else:
                        draw_rect(screen, column * 45 + 15, row * 45 + 100, (162, 209, 72), 45, 45)
                
                # draws the snakes body
                elif self.buf[row][column] > 0:
                    draw_rect(screen, column * 45 + 15, row * 45 + 100, (65, 111, 228), 45, 45)
                
                # draws the snakes head
                elif self.buf[row][column] == -2:
                    draw_rect(screen, column * 45 + 15, row * 45 + 100, (77, 124, 246), 45, 45)
                
                # draws the apples
                elif self.buf[row][column] == -3:
                    draw_rect(screen, column * 45 + 15, row * 45 + 100, (231, 71, 29), 45, 45)

    # decreases the number of all snake body parts in the grid
    def decrease_grid(self, grid1):
        for row in range(0, 15):
            for column in range(0, 17):
                if grid1[row][column] > 0:
                    grid1[row][column] = grid1[row][column] - 1

    # moves the snek along
    def move_along(self, direction, grid1, num_eaten, t, input_):
        if t == 4:
            # returns grid, then if it has eaten, then if it has crashed
            NOWHERE_DIRECTION = 0
            RIGHT_DIRECTION = 1
            LEFT_DIRECTION = 2
            DOWN_DIRECTION = 3
            UP_DIRECTION = 4
            has_eaten = False

            if input_ == UP_DIRECTION and direction != DOWN_DIRECTION:
                direction = UP_DIRECTION
            elif input_ == DOWN_DIRECTION and direction != UP_DIRECTION:
                direction = DOWN_DIRECTION
            elif input_ == RIGHT_DIRECTION and direction != LEFT_DIRECTION:
                direction = RIGHT_DIRECTION
            elif input_ == LEFT_DIRECTION and direction != RIGHT_DIRECTION:
                direction = LEFT_DIRECTION

            if direction != NOWHERE_DIRECTION:
                for row in range (0, 15):
                    for col in range(0, 17):
                        if direction == RIGHT_DIRECTION:
                            # if snake head is not at the end, or one ahead of snake is not an apple or an empty tile, returns that snake has crashed
                            if grid1.buf[row][col] == -2:
                                if col == 16 or (grid1.buf[row][col + 1] != 0 and grid1.buf[row][col + 1] != -3):
                                    return grid1, has_eaten, True, direction
                                elif grid1.buf[row][col + 1] == 0:
                                    self.decrease_grid(grid1.buf)
                                    grid1.buf[row][col + 1] = -2
                                    grid1.buf[row][col] = num_eaten + 2
                                    return grid1, has_eaten, False, direction
                                elif grid1.buf[row][col + 1] == -3:
                                    print("apple")

                        elif direction == LEFT_DIRECTION:
                            # if snake head is not at the end, or one ahead of snake is not an apple or an empty tile, returns that snake has crashed
                            if grid1.buf[row][col] == -2:
                                if  col == 0 or (grid1.buf[row][col - 1] != 0 and grid1.buf[row][col - 1] != -3):
                                    return grid1, has_eaten, True, direction
                                elif grid1.buf[row][col - 1] == 0:
                                    self.decrease_grid(grid1.buf)
                                    grid1.buf[row][col - 1] = -2
                                    grid1.buf[row][col] = num_eaten - 2
                                    return grid1, has_eaten, False, direction
                                elif grid1.buf[row][col - 1] == -3:
                                    print("apple")

                        elif direction == DOWN_DIRECTION:
                            # if snake head is not at the end, or one ahead of snake is not an apple or an empty tile, returns that snake has crashed
                            if grid1.buf[row][col] == -2:
                                if row == 14 or (grid1.buf[row + 1][col] != 0 and grid1.buf[row + 1][col] != -3):
                                    return grid1, has_eaten, True, direction
                                elif grid1.buf[row + 1][col] == 0:
                                    self.decrease_grid(grid1.buf)
                                    grid1.buf[row + 1][col] = -2
                                    grid1.buf[row][col] = num_eaten + 2
                                    return grid1, has_eaten, False, direction
                                elif grid1.buf[row + 1][col] == -3:
                                    print("apple")
                        elif direction == UP_DIRECTION:
                            # if snake head is not at the end, or one ahead of snake is not an apple or an empty tile, returns that snake has crashed
                            if grid1.buf[row][col] == -2:
                                if row == 0 or (grid1.buf[row - 1][col] != 0 and grid1.buf[row - 1][col] != -3):
                                    return grid1, has_eaten, True, direction
                                elif grid1.buf[row - 1][col] == 0:
                                    self.decrease_grid(grid1.buf)
                                    grid1.buf[row - 1][col] = -2
                                    grid1.buf[row][col] = num_eaten + 2
                                    return grid1, has_eaten, False, direction
                                elif grid1.buf[row - 1][col] == -3:
                                    print("apple")

        return grid1, False, False, direction

#  draws a rectange on the screen
def draw_rect(screen, x, y, colour, size_x, size_y):
    square = pygame.Rect((x, y, size_x, size_y))
    pygame.draw.rect(screen, colour, square)

# displays text on the screen
def type_msg(screen, font, x, y, text, colour):
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

# main
def main():

    # foldable list of all general variables
    if True:
        # clock is to set fps
        clock = pygame.time.Clock()
        # sets all state variables
        START_STATE = 0
        PLAYING_STATE = 1
        WIN_STATE = 2
        LOSE_STATE = 3
        state = START_STATE
        # "start" is whether the game will start yet or not
        start = False
        # grid is the array of tiles that the snake can move in: 15 high, 17 wide
        grid = [[0] * 17 for _ in range(15)]
        # defines the screen, where all things get displayed
        screen_length = 800
        screen = pygame.display.set_mode((screen_length, screen_length))
        # defines the font
        FONT = pygame.font.SysFont("arial", 35)
        # defines the rectangle that is the start button
        start_btn = pygame.Rect((325, 475, 150, 50))
        # defines the grid
        g1 = Grid(17, 15)
        # defines the direction variables, aka which way the snake is going
        NOWHERE_DIRECTION = 0
        RIGHT_DIRECTION = 1
        LEFT_DIRECTION = 2
        DOWN_DIRECTION = 3
        UP_DIRECTION = 4
        direction = NOWHERE_DIRECTION
        input_ = NOWHERE_DIRECTION
        # whether the snake has crashed yet
        did_crash = False
        # number of apples currently eaten
        num_eaten = 0
        t = 0

    # while loop
    running = True
    while running:
    
        # allows the code to take inputs simpler
        key = pygame.key.get_pressed()

        # makes sure it doesnt continue to eat after it has eaten for that frame
        has_eaten = False

        # takes inputs
        for event in pygame.event.get():
            
            # takes inputs no matter what

            # if escape or quit, ends the while loop which leads to the game quiting
            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False
            
            # takes inputs only if player is in the starting state
            if state == START_STATE:
                # starts if the left mouse key is being held and the mouse position collides with the start btn
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] and start_btn.collidepoint(mouse_pos):
                            state = PLAYING_STATE

            # takes inputs only if player is in the playing state
            if state == PLAYING_STATE:
                # sets the direction variable to different things depending on what keys are pressed
                if key[pygame.K_DOWN] and direction != UP_DIRECTION:
                    input_ = DOWN_DIRECTION
                
                if key[pygame.K_UP] and direction != DOWN_DIRECTION:
                    input_ = UP_DIRECTION

                if key[pygame.K_RIGHT] and direction != LEFT_DIRECTION:
                    input_ = RIGHT_DIRECTION

                if key[pygame.K_LEFT] and direction != RIGHT_DIRECTION and direction != NOWHERE_DIRECTION:
                    input_ = LEFT_DIRECTION

            # takes inputs only if player is in the lost state
            if state == LOSE_STATE:
                None

            # takes inputs only if player is in the won state
            if state == WIN_STATE:
                None

# ------------------------------------DISPLAY-------------------------------------
        
        screen.fill((29, 144, 255))

        # does a variety of different things, depending on the state
        if state == START_STATE:
            # draws the start button and the fruit
            draw_rect(screen, 325, 475, (1, 43, 85), 150, 50)
            draw_rect(screen, 362.5, 300, (231, 71, 29), 75, 75)
            type_msg(screen, FONT, 400, 500, "PLAY", (255, 255, 255,))
            # WORK IN PROGRESS!
        if state == PLAYING_STATE:
            # timer for when to move
            if True:
                t = t + 1
                if t > 4:
                    t = 0
            g1, has_eaten, did_crash, direction = g1.move_along(direction, g1, num_eaten, t, input_)    
            if did_crash:
                state = LOSE_STATE
            elif has_eaten:
                num_eaten = num_eaten + 1
            g1.draw_grid(screen)
            
            # WORK IN PROGRESS!
        if state == LOSE_STATE:
            print("you lose...")
            g1 = Grid(17, 15)
            direction = NOWHERE_DIRECTION
            input_ = NOWHERE_DIRECTION
            state = START_STATE
            # WORK IN PROGRESS!
        if state == WIN_STATE:
            None
            # WORK IN PROGRESS!

        pygame.display.update()
        clock.tick(30)

    pygame.QUIT



main()