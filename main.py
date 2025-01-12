import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # creates gui window

    while 1:
        # checks to see if user used the close button on gui
        # if so, exits the game gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0)) # set screen to black
        pygame.display.flip() # update screen


if __name__ == "__main__":
    main()

    