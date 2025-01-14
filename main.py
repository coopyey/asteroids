import pygame
import sys

# typically should avoid wildcard imports and only import what you actually need
# but, alas, small project is small
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # creates gui window
    fpsClock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers  = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, shots, updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # initialize player in center of screen
    field = AsteroidField()

    while 1:
        # checks to see if user used the close button on gui
        # if so, exits the game gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0)) # set screen to black

        for update_obj in updatable:
            update_obj.update(dt)

        for ast_obj in asteroids:
            if ast_obj.collision(player) == True:
                print("Game over!")
                sys.exit()

        for draw_obj in drawable:
            draw_obj.draw(screen)

        pygame.display.flip() # update screen
        fpsClock.tick(60) # limits the frame rate to 60 fps
        dt = fpsClock.tick(60) / 1000 # calculates delta time


if __name__ == "__main__":
    main()

    