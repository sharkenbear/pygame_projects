import pygame
import random

pygame.init()

global score
score = 0
START_STATE = 0
PLAYING_STATE = 1
WIN_BEGINNING_STATE = 2
WIN_END_STATE = 3
LOSE_STATE = 4
random_num = 0
screen_width = 625
screen_height = 625
screen = pygame.display.set_mode((screen_width, screen_height))
display_x = 0
display_y = 0
FONT = pygame.font.SysFont('arial', 40)
BIG_FONT = pygame.font.SysFont('arial', 50)

end = False

# colour list
RED = (255, 0, 0)
ORANGE = (255, 70, 70)
YELLOW = (255, 200, 0)
GREEN = (0, 200, 0)
LIGHT_BLUE = (125, 175, 200)
DARK_BLUE = (0, 0, 255)
PURPLE = (135, 0, 135)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

num_colours = {
    0: (PURPLE),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (0, 0, 0),
    8192: (0, 0, 0),
    16384: (0, 0, 0),
    32768: (0, 0, 0),
    65536: (0, 0, 0),
    131072: (0, 0, 0),
}
        
def display_text(screen, font, x, y, text, colour):
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

def draw_box(screen, x, y, colour):
    box = pygame.Rect((x, y, 125, 125))
    pygame.draw.rect(screen, (colour), box)

foo = True

def display_background(board):
    box_x = 25
    box_y = 25
    for y in range(0,4):
        for x in range(0,4):
            box_colour = num_colours.get(board[y][x], (60, 58, 50))
            if board[y][x] != 0:
                draw_box(screen, box_x + 150*x, box_y + 150*y, box_colour)
                display_text(screen, FONT, box_x + 62 + 150*x, box_y + 62 + 150*y, str(board[y][x]), BLACK)
            else:
                draw_box(screen, box_x + 150*x, box_y + 150*y, box_colour)

taken = ""
x_num = -1
y_num = -1
def find_num():
    x_num = random.randint(0, 3)
    y_num = random.randint(0, 3)
    return [x_num, y_num]

def place_num(board):
    empty_tiles = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_tiles:
        row, col = random.choice(empty_tiles)
        board[row][col] = 2 if random.random() < 0.9 else 4

def lose_game(board):
    for row in board:
        for column in row:
            if column == 0:
                return False
    return True

def win_game(board):
    for row in board:
        for column in row:
            if column == 2048:
                return True
    return False

# def move_left(board):
#     global place
#     place = 0
#     for row in enumerate(board):
#         can_merge = True
#         for four in range(0, 4):
#             r, rv = row
#             for column in enumerate(rv):
#                 c, cv = column
#                 if c - 1 != -1:
#                     cc = c - 1
#                 else:
#                     cc = c
#                 if board[cc][r] == board[c][r] and c - 1 != -1 and can_merge == True:
#                     board[cc][r] = board[cc][r]*2
#                     board[c][r] = 0
#                     if board[cc][r] != 0:
#                         place = place + 1
#                     can_merge = False
#                 if board[cc][r] == 0:
#                     board[cc][r] = board[c][r]
#                     board[c][r] = 0
#                     if board[cc][r] != 0:
#                         place = place + 1
#                         print(board[cc][r])
















def move(board, direction):
    place = False
    score = 0
    by = None

    if direction == "up":
        for x in range(0, 4):
            can_merge = True
            for _ in range(0, 4):
                for y in range(3, 0, -1):
                    if board[y][x] != 0:
                        if board[y-1][x] == 0:
                            board[y-1][x] = board[y][x]
                            board[y][x] = 0
                            place = True
                        elif board[y-1][x] == board[y][x] and can_merge:
                            board[y-1][x] = board[y][x] * 2
                            board[y][x] = 0
                            by = y - 1
                            bx = x

    elif direction == "down":
        for x in range(0, 4):
            can_merge = True
            for _ in range(0, 4):
                for y in range(0, 3, 1):
                    if board[y][x] != 0:
                        if board[y+1][x] == 0:
                            board[y+1][x] = board[y][x]
                            board[y][x] = 0
                            place = True
                        elif board[y+1][x] == board[y][x] and can_merge:
                            board[y+1][x] = board[y][x] * 2
                            board[y][x] = 0
                            by = y + 1
                            bx = x

    elif direction == "left":
        for y in range(0,4):
            can_merge = True
            for _ in range(0,4):
                for x in range(3,0, -1):
                    if board[y][x] != 0:
                        if board[y][x-1] == 0:
                            board[y][x-1] = board[y][x]
                            board[y][x] = 0
                            place = True
                        elif board[y][x-1] == board[y][x] and can_merge:
                            board[y][x-1] = board[y][x]*2
                            board[y][x] = 0
                            by = y
                            bx = x - 1

    elif direction == "right":
        for y in range(0,4):
            can_merge = True
            for _ in range(0,4):
                for x in range(0,3, 1):
                    if board[y][x] != 0:
                        if board[y][x+1] == 0:
                            board[y][x+1] = board[y][x]
                            board[y][x] = 0
                            place = True
                        elif board[y][x+1] == board[y][x] and can_merge:
                            board[y][x+1] = board[y][x]*2
                            board[y][x] = 0
                            by = y
                            bx = x + 1
    if by != None:
        can_merge = False
        place = True
        score = score + board[by][bx]

    return [place, score]




# def move_up(board):
#     place = False
#     score = 0
    # for x in range(0, 4):
    #     can_merge = True
    #     for _ in range(0, 4):
    #         for y in range(3, 0, -1):
    #             if board[y][x] != 0:
    #                 if board[y-1][x] == 0:
    #                     board[y-1][x] = board[y][x]
    #                     board[y][x] = 0
    #                     place = True
    #                 elif board[y-1][x] == board[y][x] and can_merge:
    #                     board[y-1][x] = board[y][x] * 2
    #                     board[y][x] = 0
#                         can_merge = False
#                         place = True
#                         score = score + board[y-1][x]
#     return [place, score]

# def move_down(board):
    # place = False
    # score = 0
    # for x in range(0, 4):
    #     can_merge = True
    #     for _ in range(0, 4):
    #         for y in range(0, 3, 1):
    #             if board[y][x] != 0:
    #                 if board[y+1][x] == 0:
    #                     board[y+1][x] = board[y][x]
    #                     board[y][x] = 0
    #                     place = True
    #                 elif board[y+1][x] == board[y][x] and can_merge:
    #                     board[y+1][x] = board[y][x] * 2
    #                     board[y][x] = 0
#                         can_merge = False
#                         place = True
#                         score = score + board[y+1][x]
#     return [place, score]

# def move_left(board):
#     place = False
#     score = 0
#     for y in range(0,4):
#         can_merge = True
#         for _ in range(0,4):
#             for x in range(3,0, -1):
#                 if board[y][x] != 0:
#                     if board[y][x-1] == 0:
#                         board[y][x-1] = board[y][x]
#                         board[y][x] = 0
#                         place = True
#                     elif board[y][x-1] == board[y][x] and can_merge:
#                         board[y][x-1] = board[y][x]*2
#                         board[y][x] = 0
#                         can_merge = False
#                         place = True
#                         score = score + board[y][x-1]

#     return [place, score]

# def move_right(board):
#     place = False
#     score = 0
#     for y in range(0,4):
#         can_merge = True
#         for _ in range(0,4):
#             for x in range(0,3, 1):
#                 if board[y][x] != 0:
#                     if board[y][x+1] == 0:
#                         board[y][x+1] = board[y][x]
#                         board[y][x] = 0
#                         place = True
#                     elif board[y][x+1] == board[y][x] and can_merge:
#                         board[y][x+1] = board[y][x]*2
#                         board[y][x] = 0
#                         can_merge = False
#                         place = True
#                         score = score + board[y][x+1]
#     return [place, score]

def main():
    background_colour = 0, 0, 50

    direction = None

    chose_continue = False
    end = False
    state = START_STATE

    board = [
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
    ]

    score = 0
    run = True
    while run:

        key = pygame.key.get_pressed()

    #    checks for all different key inputs
        for event in pygame.event.get():
            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                end = False
                run = False
            if key[pygame.K_t]:
                state = PLAYING_STATE
                
                board = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
                ]
                place_num(board)
                place_num(board)
                end = False
                if score > 0:
                    print("score:" + str(score))
                    score = 0
            if not end:
                if key[pygame.K_w] or key[pygame.K_UP]:
                    moved = True
                    direction = "up"

                elif key[pygame.K_a] or key[pygame.K_LEFT]:
                    moved = True
                    direction = "left"
                
                elif key[pygame.K_s] or key[pygame.K_DOWN]:
                    moved = True
                    direction = "down"
                
                elif key[pygame.K_d] or key[pygame.K_RIGHT]:
                    moved = True
                    direction = "right"

                # if key[pygame.K_w] or key[pygame.K_UP]:
                #     p, s = move_up(board)
                #     if p:
                #         place_num(board)
                #     score = score + s
                # elif key[pygame.K_a] or key[pygame.K_LEFT]:
                #     p, s = move_left(board)
                #     if p:
                #         place_num(board)
                #     score = score + s

                # if key[pygame.K_d] or key[pygame.K_RIGHT]:
                #     p, s = move_right(board)
                #     if p:
                #         place_num(board)
                #     score = score + s
                # if key[pygame.K_s] or key[pygame.K_DOWN]:
                #     p, s = move_down(board)
                #     if p:
                #         place_num(board)
                #     score = score + s

                if direction != None:
                    p, s = move(board, direction)

                    if p:
                        place_num(board)
                    score = score + s

                    direction = None

#       checks if it needs to change the state
        if win_game(board) and state != WIN_END_STATE and not chose_continue:
            state = WIN_BEGINNING_STATE

        elif lose_game(board) and state != WIN_END_STATE:
            state = LOSE_STATE

        screen.fill(background_colour)

#       does different things depending on the current state
        if state == START_STATE:
            display_text(screen, BIG_FONT, screen_width/2, screen_height/2, "Press \"T\" to start/restart!", WHITE)

        elif state == PLAYING_STATE:
            display_background(board)
        
        elif state == LOSE_STATE:
            end = True
            display_text(screen, BIG_FONT, screen_width/2, screen_height/2, "You lose! press t to try again", WHITE)

        elif state == WIN_BEGINNING_STATE:
            print("🎉🎉🎉🥳")
            state = WIN_END_STATE

        elif state == WIN_END_STATE:
            end = True
            display_text(screen, FONT, 300, screen_height/2, "You won! press t to try again", WHITE)
            display_text(screen, FONT, 300, 500, "or y, to continue...", RED)
            if key[pygame.K_y]:
                state = PLAYING_STATE
                end = False
                chose_continue = True

        pygame.display.update()

    if end != True:
        pygame.quit()


main()