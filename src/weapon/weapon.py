import pygame, math
from settings import *
from src.weapon.bullet import Bullet

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        self.pos = pos
        self.w = w_size
        self.h = h_size
        self.color = color
        self.mouse_pos = mouse_pos

        self.bullets = pygame.sprite.Group()
    
    def shoot(self, direction) -> None:
        self.bullets.add(Bullet(self.pos, self.w, self.h, self.color, direction))

    def update(self, dt) -> None:
        self.bullets.update(dt)
    
class Pistol(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)
        self.distance = pygame.math.Vector2(0, 0)

    def calculate_direction(self) -> pygame.math.Vector2:
        distance = self.mouse_pos - self.pos
        return distance.normalize() * PISTOL_BULLET_SPEED

class Shotgun(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)
        self.distance = pygame.math.Vector2(0, 0)

    def calculate_direction(self) -> pygame.math.Vector2:
        distance = self.mouse_pos - self.pos
        return distance.normalize() * PISTOL_BULLET_SPEED
