import pygame
import random
import math

pygame.init()

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

    r_change = 0
    g_change = 0
    b_change = 0

    rand_int = 0
    rand = False
    rand_run = True

    clock_num = 1000

    SCREEN.fill((255, 255, 255))

    running = True
    while running:
        if rand_run:
            rand_int = rand_int + 1
            # if rand_int == 1800:
            #     clock_num = 30
            #     rand = True
            #     rand_run = False

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

            blue = -3.1
            green = -1.5
            red = 0

            r_change = math.cos(t2+red) * 100
            g_change = math.cos(t2+green) * 100
            b_change = math.cos(t2+blue) * 100

            draw_square(r_change, g_change, b_change)

        clock.tick(clock_num)
        pygame.display.flip()
    pygame.quit

main()