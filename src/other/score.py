import pygame

from settings import *


class Score:
    def __init__(self, surface: pygame.display):
        self.surface = surface
        self.font = pygame.font.SysFont("Arial", 32)
        self.score = 0

    def draw(self) -> None:
        text = self.font.render(f"Score: {self.score}", False, "yellow")
        x = WIDTH / 2 - text.get_width() / 2
        y = 30 - text.get_height() / 2
        self.surface.blit(text, (x, y))

    def add_score(self, score: int) -> None:
        self.score += score
