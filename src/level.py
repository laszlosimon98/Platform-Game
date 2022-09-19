import pygame, math

from settings import *
from src.tile import Ground, Water, Lava, Ice
from src.player import Player
from src.score import Score

class Level:
    def __init__(self, surface, level_data):
        self.display_surface = surface
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
                        self.tiles.add(Ground((x, y), TILE_SIZE))
                    case 'W':
                        self.tiles.add(Water((x, y), TILE_SIZE))
                    case 'L':
                        self.tiles.add(Lava((x, y), TILE_SIZE))
                    case 'I':
                        self.tiles.add(Ice((x, y), TILE_SIZE))
                    case 'P':
                        self.player.add(Player((x, y), PLAYER_SIZE))
        
    def start(self) -> None:
        player = self.player.sprite
        distance = player.pos.x + PLAYER_SIZE / 2 - WIDTH / 2

        if (player.pos.x > WIDTH / 2):
            for tile in self.tiles.sprites():
                tile.start(distance)
            
            player.pos.x -= distance
            player.rect.x = round(player.pos.x)
    
    def draw_score(self) -> None:
        self.score.draw()
        self.score.update()
    
    def draw_line(self) -> None:
        player = self.player.sprite
        pygame.draw.line(self.display_surface, "white", (player.rect.centerx, player.rect.centery), pygame.mouse.get_pos())

    def bullet_collision(self) -> None:
        player = self.player.sprite

        for sprite in self.tiles.sprites():
            for weapon_type in WEAPONS:
                bullets = player.weapon[weapon_type].bullets.sprites()
                for bullet in bullets:
                    type_name = type(sprite).__name__
                    if type_name in self.solid_tiles and sprite.rect.colliderect(bullet.rect):
                        bullet.kill()

    def shiftx(self) -> None:
        player = self.player.sprite

        if player.rect.x < WIDTH / SHIFT_EDGE and player.direction.x < 0:
            self.world_shift = SHIFT_SPEED
            player.speed = 0
        elif player.rect.x > WIDTH - (WIDTH / SHIFT_EDGE) and player.direction.x > 0:
            self.world_shift = -SHIFT_SPEED
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = PLAYER_SPEED

    def horizontal_collision(self, dt) -> None:
        player = self.player.sprite
        player.move(dt)

        for sprite in self.tiles.sprites():
            type_name = type(sprite).__name__
            if sprite.rect.colliderect(player) and type_name in self.solid_tiles:
                if player.direction.x > 0:
                    player.pos.x = sprite.rect.left - PLAYER_SIZE
                    player.rect.right = round(player.pos.x) + PLAYER_SIZE
                elif player.direction.x < 0:
                    player.pos.x = sprite.rect.right
                    player.rect.left = round(player.pos.x)

    def vertical_collision(self, dt) -> None:
        player = self.player.sprite
        player.apply_gravity(dt)

        for sprite in self.tiles.sprites():
            type_name = type(sprite).__name__
            if sprite.rect.colliderect(player) and type_name in self.solid_tiles:
                if player.direction.y < 0:
                    player.pos.y = sprite.rect.bottom
                    player.rect.top = round(player.pos.y)
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.pos.y = sprite.rect.top - PLAYER_SIZE * 2
                    player.rect.bottom = round(player.pos.y) + PLAYER_SIZE * 2
                    player.direction.y = 0
                    player.is_jump = False
    
    def update(self, dt) -> None:
        # Tiles
        self.tiles.draw(self.display_surface)
        self.shiftx()
        self.tiles.update(self.world_shift, dt)

        # Collision
        self.horizontal_collision(dt)
        self.vertical_collision(dt)

        # Player
        self.player.draw(self.display_surface)
        self.player.update(dt)
        self.player.sprite.draw_bullets(self.display_surface)
    
        # Line
        self.draw_line()

        # Score
        self.draw_score()
        self.bullet_collision()