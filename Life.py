import pygame

pygame.init()

def draw_square(screen, x, y, width, height, colour):
    square = pygame.Rect((x, y, width, height))
    pygame.draw.rect(screen, (colour), square)

def draw_entities(screen_length, ecosystem, screen):
    for y in range(0, screen_length):
        for x in range(0, screen_length):
            if ecosystem[y][x]:
                entitie_colour = (255, 255, 0)
            else:
                entitie_colour = (128, 128, 128)
            draw_square(screen, x * 10, y * 10, 10, 10, entitie_colour)

def draw_lines(screen, screen_length, colour):
    screen_range = int(screen_length * 10)
    distance = int(screen_length / 8)
    for x in range(0, screen_range, distance):
        pygame.draw.line(screen, colour, (x, 0), (x, screen_range))
        for y in range(0, screen_range, 10):
            pygame.draw.line(screen, colour, (0, y), (screen_range, y))

# def draw_lines(screen, screen_length, screen_length2, z_range, colour):
#     screen_range = int(screen_length2 * screen_length / 8)
#     x_range = int(z_range * 10)
#     print (x_range)
#     distance = int(screen_length / 8)
#     for x in range(0, x_range, distance):
#         for y in range(x_range, 0, -distance):
#             pygame.draw.lines(screen, colour, False, [(0, y / screen_range * 800), (screen_range, y / screen_range * 800)])
#             pygame.draw.lines(screen, colour, False, [(x / screen_range * 800, 0), (x / screen_range * 800, screen_range)])

def check_neighbours(screen, eco_x, eco_y, ecosystem, screen_length):
    abc = []
    for ecosys_y in range(-1, 2):
        ecosys_y = ecosys_y + eco_y
        for ecosys_x in range(-1, 2):
            ecosys_x = ecosys_x + eco_x
            if ecosys_y >= 0 and ecosys_y < screen_length and ecosys_x >= 0 and ecosys_x < screen_length:
                if ecosys_x != eco_x or ecosys_y != eco_y:
                    abc.append(ecosystem[ecosys_y][ecosys_x])
                    # print("cords: " + str(ecosys_x) + ", " + str(ecosys_y))
                    # print([ecosystem[ecosys_y][ecosys_x]])
    return abc

def main():
    t = 0
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    LIGHT_GREY = (160, 160, 160)
    GREY = (128, 128, 128)
    screen_length = 80
    screen_length2 = 80
    z_length = 80
    screen = pygame.display.set_mode((screen_length2 * 10, screen_length2 * 10))
    ecosystem = [[False] * screen_length for _ in range(False, screen_length)]

    game_run = False

    def check_all_tiles(ecosystem, screen_length, screen):
        the_core = [[False] * screen_length for _ in range(False, screen_length)]
        for y in range(0, screen_length):
            for x in range(0, screen_length):
                alive_neighbours = check_neighbours(screen, x, y, ecosystem, screen_length).count(True)
                the_core[y][x] = ecosystem[y][x]
                if ecosystem[y][x] == True:
                    if alive_neighbours < 2 or alive_neighbours > 3:
                        the_core[y][x] = False
                else:
                    if alive_neighbours == 3:
                        the_core[y][x] = True
        return the_core

    def mouse_click(ecosystem):
        pos = pygame.mouse.get_pos()
        pos_x, pos_y = pos
        pos_x = int(pos_x / 10)
        pos_y = int(pos_y / 10)
        ecosystem[pos_y][pos_x] = not ecosystem[pos_y][pos_x]

    speed = 5
    min = 0
    toggle = False
    temp = False
    running = True
    while running:

        if speed < 0:
            speed = 0
        elif speed > 30:
            speed = 30
        if min > 0:
            min = min + 1
            if min > speed:
                min = 0

        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click(ecosystem)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    toggle = not toggle
                if event.key == pygame.K_t:
                    temp = True
                if event.key == pygame.K_RIGHT:
                    ecosystem = check_all_tiles(ecosystem, screen_length, screen)
                if event.key == pygame.K_c:
                    ecosystem  = [[False] * screen_length for _ in range(False, screen_length)]
                if event.key == pygame.K_UP:
                    speed = speed - 1
                if event.key == pygame.K_DOWN:
                    speed = speed + 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_t:
                    temp = False

        screen.fill(BLACK)

        if (temp or toggle) and min == 0:
            ecosystem = check_all_tiles(ecosystem, screen_length, screen)
            min = min + 1

        draw_entities(screen_length, ecosystem, screen)
        # draw_lines(screen, screen_length, screen_length2, z_length, LIGHT_GREY)
        draw_lines(screen, screen_length, LIGHT_GREY)

        pygame.display.update()
    pygame.quit


main()