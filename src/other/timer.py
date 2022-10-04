import pygame


class Timer:
    def __init__(self, duration=0, func=None):
        self.duration = duration + 1
        self.func = func
        self.start_time = 0
        self.is_active = False

    def activate(self) -> None:
        self.is_active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self) -> None:
        self.is_active = False
        self.start_time = 0

    def update(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            self.deactivate()
            if self.func:
                self.func()

    def get_time(self):
        current_time = pygame.time.get_ticks()
        return (self.duration // 1000) - ((current_time - self.start_time) // 1000)
