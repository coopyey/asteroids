import pygame

# typically should avoid wildcard imports and only import what you actually need
# but, alas, small project is small
from constants import *
from circleshape import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # creates gui window

    fpsClock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # initialize player in center of screen

    while 1:
        # checks to see if user used the close button on gui
        # if so, exits the game gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0)) # set screen to black
        player.draw(screen) # draw player

        player.update(dt) # takes keyboard input and updates player movement
        pygame.display.flip() # update screen
        fpsClock.tick(60) # limits the frame rate to 60 fps
        dt = fpsClock.tick(60) / 1000 # calculates delta time


if __name__ == "__main__":
    main()

    