import pygame
import random

pygame.init()

def display_text(screen, font, x, y, text, colour):
    text = font.render(str(text), True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

def main():

    width = 800
    height = 600
    background_colour = (128, 0, 0)

    real_number = random.randint(1, 99)

    num_input = -1
    digits = ""

    allow_digits = True

    screen = pygame.display.set_mode((width, height))

    FONT_COLOR = (128, 255, 255)
    FONT = pygame.font.SysFont('arial', 40)

    attempts = 0

    fullscreen = False

    t = 0
    pause = False

    finished = False
    finished2 = False
    finished3 = False

    running = True
    while running:

        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE]:
            running  = False

        if key[pygame.K_TAB] and not pause:
            pause = True
            if fullscreen:
                width = 800
                height = 600
                fullscreen = False
            else:
                width = 1510
                height = 900
                fullscreen = True
            screen = pygame.display.set_mode((width, height))

        if pause:
            t = t + 1
            if t > 200:
                t = 0
                pause = False

        screen.fill(background_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key < 11000:
                    if chr(event.key).isdigit() and allow_digits:
                        digits = digits + str(chr(event.key))


                        if len(digits) == 2:
                            allow_digits = False
                    elif event.key == pygame.K_BACKSPACE:
                        digits = digits[0:len(digits)-1]
                        allow_digits = True

                    elif event.key == pygame.K_RETURN and len(digits) > 0:
                        num_input = int(digits)
                        digits = ""
                        allow_digits = True

                    if pygame.K_RETURN and len(digits) > 0:
                        attempts = attempts + 1

        display_x = width / 2
        main_display_y = height / 2
        digits_display_y = height / 1.6

                    
        display_text(screen, FONT, display_x, digits_display_y, digits, FONT_COLOR)

        if int(real_number) == int(num_input):
            display_text(screen, FONT, display_x, main_display_y, "You Win!", FONT_COLOR)
            finished = True
            allow_digits = False
        elif int(real_number) < int(num_input):
            display_text(screen, FONT, display_x, main_display_y, "Too High", FONT_COLOR)
        elif int(real_number) > int(num_input) and num_input != -1:
            display_text(screen, FONT, display_x, main_display_y, "Too low", FONT_COLOR)
        elif int(num_input) == -1:
            display_text(screen, FONT, display_x, main_display_y, "Guess a  2 digit number to start", FONT_COLOR)

        if not finished2 and finished:
            finished2 = True
            attempts = attempts / 2
            finished3 = True
        if finished3:
            display_text(screen, FONT, display_x, digits_display_y, "attempts: " + str(int(attempts)), FONT_COLOR)

        pygame.display.update()

    pygame.quit()


main()