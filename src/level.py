import pygame

from settings import *
from src.tile import Ground, Water, Lava, Ice
from src.player import Player
from src.score import Score
from src.cameragroup import CameraGroup


class Level:
    def __init__(self, surface, level_data):
        self.player = None
        self.tiles = None
        self.display_surface = surface
        self.camera_group = CameraGroup()
        self.load_level(level_data)
        self.start()

        self.world_shift = 0

        # Score
        self.score = Score(self.display_surface)

        # solid
        self.solid_tiles = ["Ground", "Ice"]

    def load_level(self, level) -> None:
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(level):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                match cell:
                    case 'G':
                        self.tiles.add(Ground((x, y), TILE_SIZE, self.camera_group))
                    case 'W':
                        self.tiles.add(Water((x, y), TILE_SIZE, self.camera_group))
                    case 'L':
                        self.tiles.add(Lava((x, y), TILE_SIZE, self.camera_group))
                    case 'I':
                        self.tiles.add(Ice((x, y), TILE_SIZE, self.camera_group))
                    case 'P':
                        self.player.add(Player((x, y), PLAYER_SIZE, self.camera_group))

    def start(self) -> None:
        player = self.player.sprite
        distance = player.pos.x + PLAYER_SIZE / 2 - WIDTH / 2

        if player.pos.x > MAX_WIDTH - WIDTH / 2:
            distance = MAX_WIDTH - WIDTH

        if player.pos.x > WIDTH / 2:
            for tile in self.tiles.sprites():
                tile.start(distance)

            player.pos.x -= distance
            player.rect.x = round(player.pos.x)

    def draw_score(self) -> None:
        self.score.draw()
        self.score.update()

    def bullet_collision(self) -> None:
        player = self.player.sprite

        for tile in self.tiles.sprites():
            for weapon_type in WEAPONS:
                bullets = player.weapon[weapon_type].bullets.sprites()
                for bullet in bullets:
                    type_name = type(tile).__name__
                    if type_name in self.solid_tiles and tile.rect.colliderect(bullet.rect):
                        bullet.kill()

    def horizontal_collision(self, dt) -> None:
        player = self.player.sprite
        player.move(dt)

        for tile in self.tiles.sprites():
            type_name = type(tile).__name__
            if tile.rect.colliderect(player) and type_name in self.solid_tiles:
                if player.direction.x > 0:
                    player.pos.x = tile.rect.left - PLAYER_SIZE
                    player.rect.right = round(player.pos.x) + PLAYER_SIZE
                elif player.direction.x < 0:
                    player.pos.x = tile.rect.right
                    player.rect.left = round(player.pos.x)

    def vertical_collision(self, dt) -> None:
        player = self.player.sprite
        player.apply_gravity(dt)

        for tile in self.tiles.sprites():
            type_name = type(tile).__name__
            if tile.rect.colliderect(player) and type_name in self.solid_tiles:
                if player.direction.y < 0:
                    player.pos.y = tile.rect.bottom
                    player.rect.top = round(player.pos.y)
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.pos.y = tile.rect.top - PLAYER_SIZE * 2
                    player.rect.bottom = round(player.pos.y) + PLAYER_SIZE * 2
                    player.direction.y = 0
                    player.is_jump = False

    def update(self, dt) -> None:
        # Tiles
        self.camera_group.custom_draw(self.player.sprite)
        self.tiles.update(dt)

        # Collision
        self.horizontal_collision(dt)
        self.vertical_collision(dt)

        # Player
        self.player.update(dt)

        # Score
        self.draw_score()
        self.bullet_collision()
