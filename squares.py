import pygame
import random
import math

pygame.init()

find_diagonal_num = {
    8: 7,
    9: 6,
    10: 5,
    11: 4,
    12: 3,
    13: 2,
    14: 1,
    15: 0,
}

rgb_flip = {
    0: 15,
    1: 14,
    2: 13,
    3: 12,
    4: 11,
    5: 10,
    6: 9,
    7: 8,
    8: 7,
    9: 6,
    10: 5,
    11: 4,
    12: 3,
    13: 2,
    14: 1,
    15: 0
}

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
NUM_WIDTH = SCREEN_WIDTH / 50 - 1
NUM_HEIGHT = SCREEN_HEIGHT / 50 - 1
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def is_even(num):
    num2 = num / 2
    num3 = int(num / 2)
    if num2 == num3:
        return True
    return False

def convert_range(original_num, in_tuple):
    in_min, in_max, out_min, out_max = in_tuple
    old_range = (in_max - in_min)
    NewRange = (out_max - out_min)

    return int((((original_num - in_min) * NewRange) / old_range) + out_min)

def draw_square(r_change, g_change, b_change):

    x = random.randint(0, 15)
    y = random.randint(0, 15)

    integer = int((x + y) / 2)

    r = random.randint(integer - 2, integer) * 16 + r_change
    g = random.randint(integer - 2, integer) * 16 + g_change
    b = random.randint(integer - 2, integer) * 16 + b_change

    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    
    if g < 0:
        g = 0
    elif g > 255:
        g = 255

    if b < 0:
        b = 0
    elif b > 255:
        b = 255

    draw_rect(x * 50, y * 50, 50, 50, (r, g, b))

def draw_rect(x, y, width, height, colour):
    square = pygame.Rect((x, y, width, height))
    pygame.draw.rect(SCREEN, (colour), square)

def main():

    clock = pygame.time.Clock()

    t = 0
    t2 = random.uniform(0, 2)

    print(convert_range(3, (0, 10, 10, 0)))

    r_change = 0
    g_change = 0
    b_change = 0

    rand_int = 0
    rand = False
    rand_run = True

    SCREEN.fill((255, 255, 255))

    running = True
    while running:
        if rand_run:
            rand_int = rand_int + 1
        #     if rand_int == 1800:
        #         rand = True
        #         rand_run = False

        t = t + 1
        if t < 15:
            new_square = False
        else:
            new_square = True
            t = 0

        t2 = t2 + 0.0001
        if t2 > 2 * math.pi:
            t2 = 0
            print(rand_int)

        key = pygame.key.get_pressed()

        # takes inputs
        for event in pygame.event.get():

            # quits the loop
            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False

        # display from here on out
        
        if (new_square and rand) or (True and not rand):

            r_change = 0
            g_change = 0
            b_change = 0

            blue = -3.1
            green = -1.5
            red = 0

            r_change = math.cos(t2+red) * 100
            g_change = math.cos(t2+green) * 100
            b_change = math.cos(t2+blue) * 100

            draw_square(r_change, g_change, b_change)

        # clock.tick(30)
        pygame.display.flip()
    pygame.quit

main()