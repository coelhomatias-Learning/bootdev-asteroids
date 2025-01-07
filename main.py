import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
