import pygame, math, random
from settings import *
from src.weapon.bullet import Bullet
from src.timer import Timer

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        self.pos = pos
        self.w = w_size
        self.h = h_size
        self.color = color
        self.mouse_pos = mouse_pos

        self.bullets = pygame.sprite.Group()
        self.direction = pygame.math.Vector2(0, 0)

    def shoot(self, direction) -> None:
        self.bullets.add(Bullet(self.pos, self.w, self.h, self.color, direction))

    def update(self, dt) -> None:
        self.bullets.update(dt)
    
class Pistol(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)

    def calculate_direction(self) -> None:
        direction = self.mouse_pos - self.pos
        self.shoot(direction.normalize() * PISTOL_BULLET_SPEED)

class Shotgun(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)

    def calculate_direction(self) -> None:
        direction = self.mouse_pos - self.pos
        direction = direction.normalize()

        for step in range(-5, 5, 2):
            angle = math.atan2(direction.x + step / 20, direction.y + step / 20)

            self.shoot(pygame.math.Vector2(math.sin(angle) * SHOTGUN_BULLET_SPEED, math.cos(angle) * SHOTGUN_BULLET_SPEED))

class Machinegun(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)

    def calculate_direction(self) -> None:
        direction = self.mouse_pos - self.pos
        direction = direction.normalize()

        rnd = random.randint(-2, 3)
        angle = math.atan2(direction.x + rnd / 20, direction.y + rnd / 20)
        self.shoot(pygame.math.Vector2(math.sin(angle) * MACHINEGUN_BULLET_SPEED, math.cos(angle) * MACHINEGUN_BULLET_SPEED))

class Sniper(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)

    def calculate_direction(self) -> None:
        direction = self.mouse_pos - self.pos
        direction = direction.normalize()
        angle = math.atan2(direction.x, direction.y)
        self.shoot(pygame.math.Vector2(math.sin(angle) * SNIPER_BULLET_SPEED, math.cos(angle) * SNIPER_BULLET_SPEED))