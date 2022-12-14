import math
import random

import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.math.Vector2, size: int, group: pygame.sprite.Group):
        super(Tile, self).__init__(group)
        self.animation = random.random()

        # Init
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def start(self, start_pos: pygame.math.Vector2) -> None:
        self.pos.x -= start_pos
        self.rect.x = round(self.pos.x)


class Solid(Tile):
    def __init__(self, pos: pygame.math.Vector2, size: int, group: pygame.sprite.Group):
        super(Solid, self).__init__(pos, size, group)


class ShapeLess(Tile):
    def __init__(self, pos: pygame.math.Vector2, size: int, group: pygame.sprite.Group):
        super(ShapeLess, self).__init__(pos, size, group)

    def wave(self, dt: float) -> None:
        self.pos.y += math.sin(self.animation) * 20 * dt
        self.rect.y = round(self.pos.y)
        self.animation += 0.05

    def update(self, dt: float) -> None:
        self.wave(dt)


class Ground(Solid):
    def __init__(self, pos: pygame.math.Vector2, size: int, group: pygame.sprite.Group):
        super(Ground, self).__init__(pos, size, group)
        # image = pygame.image.load("imgs/wall.jpg").convert_alpha()
        # self.image.blit(image, (0, 0))
        self.image.fill("gray")


class Ice(Solid):
    def __init__(self, pos: pygame.math.Vector2, size: int, group: pygame.sprite.Group):
        super(Ice, self).__init__(pos, size, group)
        self.image.fill('lightblue')


class Water(ShapeLess):
    def __init__(self, pos: pygame.math.Vector2, size: int, group: pygame.sprite.Group):
        super(Water, self).__init__(pos, size, group)
        self.image.fill("blue")


class Lava(ShapeLess):
    def __init__(self, pos: pygame.math.Vector2, size: int, group: pygame.sprite.Group):
        super(Lava, self).__init__(pos, size, group)
        self.image.fill('red')
