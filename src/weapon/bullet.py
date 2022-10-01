import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.math.Vector2, w_size: int, h_size: int, color: str, direction: pygame.math.Vector2,
                 group: pygame.sprite.Group):
        super(Bullet, self).__init__(group)
        self.image = pygame.Surface((w_size, h_size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.original_pos = pygame.math.Vector2(self.rect.center)

        self.direction = direction

    def update(self, dt: float) -> None:
        self.pos.x += self.direction.x * dt
        self.pos.y += self.direction.y * dt
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
