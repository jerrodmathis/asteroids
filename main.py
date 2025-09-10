import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.colliding(player):
                sys.exit("Game over!")

            for shot in shots:
                if asteroid.colliding(shot):
                    asteroid.kill()
                    shot.kill()
        for drawable in drawables:
            drawable.draw(screen)
        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
