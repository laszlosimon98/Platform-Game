import math
import random

import pygame

from settings import *
from src.weapon.bullet import Bullet
from src.other.timer import Timer


class Weapon:
    def __init__(self, pos: pygame.math.Vector2, w_size: int, h_size: int, color: str,
                 group: pygame.sprite.Group, mouse_pos=None):
        self.pos = pos
        self.w = w_size
        self.h = h_size
        self.color = color
        self.mouse_pos = mouse_pos
        self.group = group

        self.bullets = pygame.sprite.Group()

        # reloading
        self.ammo = 0
        self.default_ammo = 0
        self.reload_time = 0
        self.is_reloading = False
        self.timer = Timer()

    def shoot(self, direction: pygame.math.Vector2) -> None:
        if self.ammo > 0:
            self.bullets.add(Bullet(self.pos, self.w, self.h, self.color, direction, self.group))
            self.ammo -= 1

    def check_ammo(self):
        if not self.timer.is_active and self.ammo == 0 and not self.is_reloading:
            self.timer = Timer(self.reload_time)
            self.timer.activate()
            self.is_reloading = True

        if not self.timer.is_active and self.is_reloading:
            self.ammo = self.default_ammo
            self.is_reloading = False

    def update(self, dt: float) -> None:
        self.bullets.update(dt)
        self.timer.update()


class Pistol(Weapon):
    def __init__(self, pos: pygame.math.Vector2, w_size: int, h_size: int, color: str,
                 group: pygame.sprite.Group, mouse_pos=None):
        super(Pistol, self).__init__(pos, w_size, h_size, color, group, mouse_pos)
        self.ammo = PISTOL_AMMO_CAPACITY
        self.default_ammo = self.ammo
        self.reload_time = PISTOL_RELOAD_TIME

    def calculate_direction(self) -> list[pygame.math.Vector2]:
        direction = (self.mouse_pos - self.pos + self.group.offset).normalize()
        angle = math.atan2(direction.x, direction.y)
        return [pygame.math.Vector2(math.sin(angle) * PISTOL_BULLET_SPEED, math.cos(angle) * PISTOL_BULLET_SPEED)]


class Shotgun(Weapon):
    def __init__(self, pos: pygame.math.Vector2, w_size: int, h_size: int, color: str,
                 group: pygame.sprite.Group, mouse_pos=None):
        super(Shotgun, self).__init__(pos, w_size, h_size, color, group, mouse_pos)
        self.ammo = SHOTGUN_AMMO_CAPACITY * 5
        self.default_ammo = self.ammo
        self.reload_time = SHOTGUN_RELOAD_TIME

    def calculate_direction(self) -> list[pygame.math.Vector2]:
        direction = (self.mouse_pos - self.pos + self.group.offset).normalize()
        dir_list = list()

        for step in range(-5, 5, 2):
            angle = math.atan2(direction.x + step / 20, direction.y + step / 20)
            dir_list.append(pygame.math.Vector2(math.sin(angle) * SHOTGUN_BULLET_SPEED,
                                                math.cos(angle) * SHOTGUN_BULLET_SPEED))
        return dir_list


class Machinegun(Weapon):
    def __init__(self, pos: pygame.math.Vector2, w_size: int, h_size: int, color: str,
                 group: pygame.sprite.Group, mouse_pos=None):
        super(Machinegun, self).__init__(pos, w_size, h_size, color, group, mouse_pos)
        self.ammo = MACHINEGUN_AMMO_CAPACITY
        self.default_ammo = self.ammo
        self.reload_time = MACHINEGUN_RELOAD_TIME

    def calculate_direction(self) -> list[pygame.math.Vector2]:
        direction = (self.mouse_pos - self.pos + self.group.offset).normalize()
        rnd = random.randint(-2, 3)
        angle = math.atan2(direction.x + rnd / 20, direction.y + rnd / 20)
        return [pygame.math.Vector2(math.sin(angle) * MACHINEGUN_BULLET_SPEED,
                                    math.cos(angle) * MACHINEGUN_BULLET_SPEED)]


class Sniper(Weapon):
    def __init__(self, pos: pygame.math.Vector2, w_size: int, h_size: int, color: str,
                 group: pygame.sprite.Group, mouse_pos=None):
        super(Sniper, self).__init__(pos, w_size, h_size, color, group, mouse_pos)
        self.ammo = SNIPER_AMMO_CAPACITY
        self.default_ammo = self.ammo
        self.reload_time = SNIPER_RELOAD_TIME

    def calculate_direction(self) -> list[pygame.math.Vector2]:
        direction = (self.mouse_pos - self.pos + self.group.offset).normalize()
        angle = math.atan2(direction.x, direction.y)
        return [pygame.math.Vector2(math.sin(angle) * SNIPER_BULLET_SPEED, math.cos(angle) * SNIPER_BULLET_SPEED)]
