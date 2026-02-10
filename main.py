import pygame
import constants
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))


if __name__ == "__main__":
    main()
