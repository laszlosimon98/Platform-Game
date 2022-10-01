import pygame.sprite


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super(CameraGroup, self).__init__()
        self.display_surface = pygame.display.get_surface()

        # camera
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def center_target_camera(self, target: pygame.sprite):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player: pygame.sprite):
        self.center_target_camera(player)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
