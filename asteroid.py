import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position,  self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        #immediatly destroys asteroid on hit
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            #does not continue if it is already at the smallest size
        
        new_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(new_angle) * 1.2
        vec2 = self.velocity.rotate(-new_angle) * 1.2
        #calculates a random angle, then assigns 2 variables to apply to the new asteroids
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        #creates 2 new asteroids at the same position, while reducing their sizes

        new_ast1.velocity = vec1
        new_ast2.velocity = vec2
        #sets the velocity and angle of the new asteroids


    
    
    