import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position, radius):
        super().__init__(position.x, position.y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position,  self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
