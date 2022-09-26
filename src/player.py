import pygame, math

from settings import *
from src.timer import Timer
from src.weapon.weapon import Pistol, Shotgun, Machinegun, Sniper


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()

        # Init
        self.image = pygame.Surface((size, size * 2))
        self.image.fill("white")
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.bullet_pos = pygame.math.Vector2(self.rect.center)

        # Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.jump_speed = JUMP_SPEED
        self.gravity = GRAVITY_FORCE
        self.is_jump = False

        # Weapon
        self.weapon_index = 0
        self.current_weapon = WEAPONS[self.weapon_index]

        self.weapon = {
            "pistol": Pistol(self.bullet_pos, PISTOL_BULLET_SIZE, PISTOL_BULLET_SIZE, "brown"),
            "shotgun": Shotgun(self.bullet_pos, SHOTGUN_BULLET_SIZE, SHOTGUN_BULLET_SIZE, "red"),
            "machinegun": Machinegun(self.bullet_pos, MACHINEGUN_BULLET_SIZE, MACHINEGUN_BULLET_SIZE, "blue"),
            "sniper": Sniper(self.bullet_pos, MACHINEGUN_BULLET_SIZE, MACHINEGUN_BULLET_SIZE, "white")
        }

        self.weapon_range = {
            "pistol": PISTOL_BULLET_MAX_RANGE,
            "shotgun": SHOTGUN_BULLET_MAX_RANGE,
            "machinegun": MACHINEGUN_BULLET_MAX_RANGE,
            "sniper": SNIPER_BULLET_MAX_RANGE
        }

        # Timer
        self.weapon_timers = {
            "pistol": Timer(PISTOL_SHOT_DELAY),
            "shotgun": Timer(SHOTGUN_SHOT_DELAY),
            "machinegun": Timer(MACHINEGUN_SHOT_DELAY),
            "sniper": Timer(SNIPER_SHOT_DELAY),
        }

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
        elif keys[pygame.K_1]:
            self.switch_weapon(1)
        elif keys[pygame.K_2]:
            self.switch_weapon(2)
        elif keys[pygame.K_3]:
            self.switch_weapon(3)
        elif keys[pygame.K_4]:
            self.switch_weapon(4)

        if mouse[0] and not self.weapon_timers[self.current_weapon].is_active:
            self.weapon[self.current_weapon].mouse_pos = mouse_pos
            self.weapon[self.current_weapon].distance = self.weapon[self.current_weapon].calculate_direction()
            self.weapon_timers[self.current_weapon].activate()

    def switch_weapon(self, index) -> None:
        self.weapon_index = index - 1
        self.current_weapon = WEAPONS[self.weapon_index]

    def check_bullet(self) -> None:
        for key in self.weapon.keys():
            bullets = self.weapon[key].bullets.sprites()
            for bullet in bullets:
                x = bullet.pos.x - bullet.original_pos.x
                y = bullet.pos.y - bullet.original_pos.y
                dist = math.sqrt(pow(x, 2) + pow(y, 2))

                if dist >= self.weapon_range[key]:
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
        for timer in self.weapon_timers.values():
            timer.update()

    def update(self, dt) -> None:
        self.get_input()
        self.update_timers()
        self.check_bullet()

        for weapon in self.weapon.values():
            weapon.update(dt)

    def draw_bullets(self, surface):
        for weapon in self.weapon.values():
            weapon.bullets.draw(surface)
