import math
import pygame
import random


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.animation = random.random()

        # Init
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, shift, dt) -> None:
        self.pos.x += shift * dt
        self.rect.x = round(self.pos.x)

    def start(self, start_pos) -> None:
        self.pos.x -= start_pos
        self.rect.x = round(self.pos.x)

    def update_pos(self, new_pos) -> None:
        self.pos = new_pos
        self.rect.x = round(self.pos.x)


class Solid(Tile):
    def __init__(self, pos, size, group):
        super().__init__(pos, size, group)


class ShapeLess(Tile):
    def __init__(self, pos, size, group):
        super().__init__(pos, size, group)

    def wave(self, dt) -> None:
        self.pos.y += math.sin(self.animation) * 20 * dt
        self.rect.y = round(self.pos.y)
        self.animation += 0.05

    def update(self, shift, dt) -> None:
        self.pos.x += shift * dt
        self.rect.x = round(self.pos.x)
        self.wave(dt)


class Ground(Solid):
    def __init__(self, pos, size, group):
        super().__init__(pos, size, group)
        # image = pygame.image.load("imgs/wall.jpg").convert_alpha()
        # self.image.blit(image, (0, 0))
        self.image.fill("gray")


class Ice(Solid):
    def __init__(self, pos, size, group):
        super().__init__(pos, size, group)
        self.image.fill('lightblue')


class Water(ShapeLess):
    def __init__(self, pos, size, group):
        super().__init__(pos, size, group)
        self.image.fill("blue")


class Lava(ShapeLess):
    def __init__(self, pos, size, group):
        super().__init__(pos, size, group)
        self.image.fill('red')
