import pygame.sprite


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, size, group, color, speed):
        super(Entity, self).__init__(group)

        # Init
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.group = group

        self.pos = pygame.math.Vector2(self.rect.center)
        self.bullet_pos = pygame.math.Vector2(self.rect.center)

        # Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = speed
