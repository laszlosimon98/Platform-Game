import math
import pygame
import random

from settings import *
from src.weapon.bullet import Bullet


class Weapon:
    def __init__(self, pos, w_size, h_size, color, group, mouse_pos=None):
        self.pos = pos
        self.w = w_size
        self.h = h_size
        self.color = color
        self.mouse_pos = mouse_pos
        self.group = group

        self.bullets = pygame.sprite.Group()

    def shoot(self, direction) -> None:
        self.bullets.add(Bullet(self.pos, self.w, self.h, self.color, direction, self.group))

    def update(self, dt) -> None:
        self.bullets.update(dt)


class Pistol(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)

    def calculate_direction(self) -> list[pygame.math.Vector2]:
        direction = (self.mouse_pos - self.pos + self.group.offset).normalize()
        angle = math.atan2(direction.x, direction.y)
        return [pygame.math.Vector2(math.sin(angle) * PISTOL_BULLET_SPEED, math.cos(angle) * PISTOL_BULLET_SPEED)]

class Shotgun(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)

    def calculate_direction(self) -> list[pygame.math.Vector2]:
        direction = (self.mouse_pos - self.pos + self.group.offset).normalize()
        dir_list = list()

        for step in range(-5, 5, 2):
            angle = math.atan2(direction.x + step / 20, direction.y + step / 20)
            dir_list.append(pygame.math.Vector2(math.sin(angle) * SHOTGUN_BULLET_SPEED,
                                                math.cos(angle) * SHOTGUN_BULLET_SPEED))
        return dir_list


class Machinegun(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)

    def calculate_direction(self) -> list[pygame.math.Vector2]:
        direction = (self.mouse_pos - self.pos + self.group.offset).normalize()
        rnd = random.randint(-2, 3)
        angle = math.atan2(direction.x + rnd / 20, direction.y + rnd / 20)
        return [pygame.math.Vector2(math.sin(angle) * MACHINEGUN_BULLET_SPEED,
                                    math.cos(angle) * MACHINEGUN_BULLET_SPEED)]


class Sniper(Weapon):
    def __init__(self, pos, w_size, h_size, color, mouse_pos=None):
        super().__init__(pos, w_size, h_size, color, mouse_pos)

    def calculate_direction(self) -> list[pygame.math.Vector2]:
        direction = (self.mouse_pos - self.pos + self.group.offset).normalize()
        angle = math.atan2(direction.x, direction.y)
        return [pygame.math.Vector2(math.sin(angle) * SNIPER_BULLET_SPEED, math.cos(angle) * SNIPER_BULLET_SPEED)]
