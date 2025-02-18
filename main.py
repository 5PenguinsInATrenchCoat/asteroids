import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

asteroid_field = AsteroidField()

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	#Creates screen, matches the screen size from constants
	print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
	while True:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
		screen.fill((0, 0, 0))
		for object in drawable:
			object.draw(screen)
		updatable.update(dt)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		#FPS
		for asteroid in asteroids:
			if player.collision(asteroid) == True:
				print("Game over!")
				sys.exit()
		#Check for collision, close if True

if __name__ == "__main__":
    main()

