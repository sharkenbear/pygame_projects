import pygame
import random

pygame.init()

class Grid:
    def __init__(self, width, height):
        # defines the base grid variables
        self.width = width
        self.height = height
        self.buf = [[0] * width for _ in range(height)]
    
    def draw_grid(self, screen):
        # draws the whole grid, drawing green if its empty, blue if it has the snake(dark blue for the head) and red for the apples
        # if self.buf (the grid array) is 0, its an empty tile, if its 1 its the snakes body, if its 2 the head and if its 3 its a apple
        for row in range(0, 15):
            for column in range(0, 17):
                self.buf[1][4] = 1
                if self.buf[row][column] == 0:
                    draw_rect(screen, column * 45 + 15, row * 45 + 100, (255, 255, 0), 45, 45)
                elif self.buf[row][column] == 1:
                    draw_rect(screen, column * 45 + 15, row * 45 + 100, (0, 0, 255), 45, 45)

#  draws a rectange on the screen
def draw_rect(screen, x, y, colour, size_x, size_y):
    square = pygame.Rect((x, y, size_x, size_y))
    pygame.draw.rect(screen, colour, square)

# displays text on the screen
def type_msg(screen, font, x, y, text, colour):
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

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
        # "start" is whether the game will start or not
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

    # while loop
    running = True
    while running:
    
        # allows the code to take inputs simpler
        key = pygame.key.get_pressed()

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
                    if pygame.mouse.get_pressed()[0]:
                        if start_btn.collidepoint(mouse_pos):
                            state = PLAYING_STATE

            # takes inputs only if player is in the playing state
            if state == PLAYING_STATE:
                None

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
            g1.draw_grid(screen)
            # WORK IN PROGRESS!
        if state == LOSE_STATE:
            None
            # WORK IN PROGRESS!
        if state == WIN_STATE:
            None
            # WORK IN PROGRESS!

        pygame.display.update()
        clock.tick(30)

    pygame.QUIT



main()