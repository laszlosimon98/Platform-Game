import pygame, sys, time

from settings import *
from src.level import Level

pygame.init()


class Game:
    def __init__(self):
        pygame.display.set_caption("Cube Test")
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # LEVEL
        self.level = Level(self.display_surface, LEVEL)

    def draw(self, surface, dt) -> None:
        surface.fill("black")
        self.level.update(dt)
        pygame.display.update()

    def update(self) -> None:
        prev_time = time.time()
        while True:
            dt = time.time() - prev_time
            prev_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(60)
            self.draw(self.display_surface, dt)


if __name__ == "__main__":
    game = Game()
    game.update()
