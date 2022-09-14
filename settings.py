import pygame
pygame.init()

# LEVEL
LEVEL = [
    'G                                                  G',
    'G                                                  G',
    'G        GLLLG                                     G',
    'G        GGGGG     P                               G',
    'G                                                  G',
    'G                 GGG                              G',
    'G                                                  G',
    'G                                                  G',
    'GWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWG',
    'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
    ]

# SURFACE
TILE_SIZE = 64
WIDTH = pygame.display.Info().current_w
HEIGHT = len(LEVEL) * TILE_SIZE

# PLAYER
PLAYER_SIZE = TILE_SIZE / 2
PLAYER_SPEED = 200

# GRAVITY
GRAVITY_FORCE = 20
JUMP_SPEED = -10

# WORLD
SHIFT_SPEED = PLAYER_SPEED
SHIFT_EDGE = 8

# BULLET
BULLET_SIZE = 10
BULLET_SPEED = 300
BULLET_GRAVITY = 10
BULLET_MAX_RANGE = 200

# WEAPONS
PISTOL_DELAY = 700
