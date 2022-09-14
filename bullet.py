import pygame, math
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, size, mouse_pos):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("brown")
        self.rect = self.image.get_rect(center = pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.original_pos = pygame.math.Vector2(self.rect.center)

        self.mouse_pos = mouse_pos
        self.direction = self.calculate_distance()
    
    def calculate_distance(self) -> pygame.math.Vector2:
        distance = self.mouse_pos - self.pos
        return distance.normalize() * BULLET_SPEED
    
    def update(self, dt:float) -> None:
        self.pos.x += self.direction.x * dt
        self.pos.y += self.direction.y * dt
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y