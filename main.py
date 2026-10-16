import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH 
from logger import log_state

print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    black = (0, 0, 0)

    while running:
        log_state()

        for event in pygame.event.get():
            pass

        screen.fill(black)
        pygame.display.flip()


if __name__ == "__main__":
    main()
