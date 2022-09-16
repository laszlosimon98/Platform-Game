import pygame
from settings import *

class Score:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.SysFont("Arial", 32)
        self.time = 0
        self.extra_score = 0
    
    def draw(self) -> None:
        text = self.font.render(f"Score: {self.time}", 0, "yellow")
        x = WIDTH / 2 - text.get_width() / 2
        y = 30 - text.get_height() / 2
        self.surface.blit(text, (x, y))

    def update(self) -> None:
        self.time = pygame.time.get_ticks() // 50 + self.extra_score
    
    def add_score(self, amount:int) -> None:
        self.extra_score += amount
