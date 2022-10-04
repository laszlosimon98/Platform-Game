from src.map.mapIO import MapIO

# LEVEL
LEVEL = MapIO.load("D:/Projects/Python/Platform-Game/maps/map1.txt")

# SURFACE
TILE_SIZE = 64
WIDTH = 1200
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
WEAPONS = ["pistol", "shotgun", "machinegun", "sniper"]

# PISTOL
PISTOL_BULLET_SIZE = 10
PISTOL_BULLET_SPEED = 500
PISTOL_BULLET_MAX_RANGE = 500
PISTOL_AMMO_CAPACITY = 7
PISTOL_SHOT_DELAY = 500
PISTOL_RELOAD_TIME = 2000

# SHOTGUN
SHOTGUN_BULLET_SIZE = 7
SHOTGUN_BULLET_SPEED = 500
SHOTGUN_BULLET_MAX_RANGE = 200
SHOTGUN_AMMO_CAPACITY = 2
SHOTGUN_SHOT_DELAY = 400
SHOTGUN_RELOAD_TIME = 4000

# MACHINEGUN
MACHINEGUN_BULLET_SIZE = 5
MACHINEGUN_BULLET_SPEED = 800
MACHINEGUN_BULLET_MAX_RANGE = 600
MACHINEGUN_AMMO_CAPACITY = 30
MACHINEGUN_SHOT_DELAY = 100
MACHINEGUN_RELOAD_TIME = 5000

# SNIPER
SNIPER_BULLET_SIZE = 5
SNIPER_BULLET_SPEED = 1200
SNIPER_BULLET_MAX_RANGE = 1000
SNIPER_AMMO_CAPACITY = 5
SNIPER_SHOT_DELAY = 800
SNIPER_RELOAD_TIME = 7000
