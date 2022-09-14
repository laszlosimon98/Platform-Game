import pygame, math

from settings import *
from timer import Timer
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()

        # Init
        self.image = pygame.Surface((size, size*2))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft = pos)

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.bullet_pos = pygame.math.Vector2(self.rect.center)

        # Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.jump_speed = JUMP_SPEED
        self.gravity = GRAVITY_FORCE
        self.is_jump = False

        # Weapon
        self.current_weapon = "pistol"

        # Timer
        self.timers = {
            "pistol" : Timer(PISTOL_DELAY)
        }

        # Bullets
        self.bullets = pygame.sprite.Group()
    
    def get_input(self) -> None:
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_SPACE] and not self.is_jump:
            self.jump()
        
        if mouse[0] and not self.timers[self.current_weapon].is_active:
            self.bullets.add(Bullet(self.bullet_pos, BULLET_SIZE, mouse_pos))
            self.timers[self.current_weapon].activate()

    def check_bullet(self) -> None:
        for bullet in self.bullets.sprites():
            x = bullet.pos.x - bullet.original_pos.x
            y = bullet.pos.y - bullet.original_pos.y
            dist = math.sqrt(pow(x, 2) + pow(y, 2))
            if dist >= BULLET_MAX_RANGE:
                bullet.kill()

    def jump(self) -> None:
        self.is_jump = True
        self.direction.y = self.jump_speed

    def move(self, dt) -> None:
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.bullet_pos.x = self.rect.x + PLAYER_SIZE / 2
    
    def apply_gravity(self, dt) -> None:
        self.direction.y += self.gravity * dt
        self.pos.y += self.direction.y
        self.rect.y = round(self.pos.y)
        self.bullet_pos.y = self.rect.y + PLAYER_SIZE / 2
    
    def update_timers(self) -> None:
        for timer in self.timers.values():
            timer.update()

    def update(self, dt) -> None:
        self.get_input()
        self.update_timers()
        self.bullets.update(dt)
        self.check_bullet()