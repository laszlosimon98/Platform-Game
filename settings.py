import pygame
pygame.init()

# LEVEL
LEVEL = [
    'G                                                  G',
    'G                                                  G',
    'G        GLLLG                                     G',
    'G        GGGGGGG   P                               G',
    'G                                                  G',
    'G               G GGG                              G',
    'G             G          G                         G',
    'G              G                                   G',
    'GWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWG',
    'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
    ]

# SURFACE
TILE_SIZE = 64
WIDTH = 800
HEIGHT = len(LEVEL) * TILE_SIZE
MAX_WIDTH = len(LEVEL[0]) * TILE_SIZE

# PLAYER
PLAYER_SIZE = TILE_SIZE / 2
PLAYER_SPEED = 300

# GRAVITY
GRAVITY_FORCE = 20
JUMP_SPEED = -10

# WORLD
SHIFT_SPEED = PLAYER_SPEED

# WEAPONS
WEAPONS = ["pistol", "shotgun"]

MACHINEGUN_DELAY = 100
SNIPER_DELAY = 1500

# PISTOL
PISTOL_BULLET_SIZE = 10
PISTOL_BULLET_SPEED = 500
PISTOL_BULLET_MAX_RANGE = 1000
PISTOL_BULLET_DELAY = 500
PISTOL_BULLET_CAPACITY = 7
PISTOL_RELOAD_TIME = 2

# SHOTGUN
SHOTGUN_BULLET_SIZE = 7
SHOTGUN_BULLET_SPEED = 500
SHOTGUN_BULLET_MAX_RANGE = 100
SHOTGUN_BULLET_DELAY = 400
SHOTGUN_BULLET_CAPACITY = 2
SHOTGUN_RELOAD_TIME = 4