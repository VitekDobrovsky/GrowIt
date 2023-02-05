import pygame
import sys


# SETTINGS
WIDTH = 800
HEIGHT = 650
FPS = 60
BG_COLOR = '#ffbf66'

# SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
movable_sprites = []

# PLAYER
img = pygame.image.load('graphics/player/idle/1.png').convert_alpha()
rect = img.get_rect(center=(WIDTH/2, HEIGHT/2))
velocity = pygame.math.Vector2()
speed = 5
status = 'idle'
an_index = 0
an_speed = 0.1
an_frames = {
    'idle': [pygame.image.load('graphics/player/idle/1.png').convert_alpha(),
            pygame.image.load('graphics/player/idle/2.png').convert_alpha(),
            pygame.image.load('graphics/player/idle/3.png').convert_alpha(),
            pygame.image.load('graphics/player/idle/3.png').convert_alpha(),
            pygame.image.load('graphics/player/idle/2.png').convert_alpha(),
            pygame.image.load('graphics/player/idle/1.png').convert_alpha()],
    'left': [pygame.image.load('graphics/player/left/1.png').convert_alpha(),
            pygame.image.load('graphics/player/left/2.png').convert_alpha(),
            pygame.image.load('graphics/player/left/3.png').convert_alpha(),
            pygame.image.load('graphics/player/left/2.png').convert_alpha(),
            pygame.image.load('graphics/player/left/1.png').convert_alpha()],
    'right': [pygame.image.load('graphics/player/right/1.png').convert_alpha(),
            pygame.image.load('graphics/player/right/2.png').convert_alpha(),
            pygame.image.load('graphics/player/right/3.png').convert_alpha(),
            pygame.image.load('graphics/player/right/2.png').convert_alpha(),
            pygame.image.load('graphics/player/right/1.png').convert_alpha()],
    'down': [pygame.image.load('graphics/player/down/1.png').convert_alpha(),
            pygame.image.load('graphics/player/down/2.png').convert_alpha(),
            pygame.image.load('graphics/player/down/3.png').convert_alpha(),
            pygame.image.load('graphics/player/down/2.png').convert_alpha(),
            pygame.image.load('graphics/player/down/1.png').convert_alpha()],
    'up': [pygame.image.load('graphics/player/up/1.png').convert_alpha(),
            pygame.image.load('graphics/player/up/2.png').convert_alpha(),
            pygame.image.load('graphics/player/up/3.png').convert_alpha(),
            pygame.image.load('graphics/player/up/2.png').convert_alpha(),
            pygame.image.load('graphics/player/up/1.png').convert_alpha()]
}

def update_player():
    global an_index, img, an_speed, status
    screen.blit(img, rect)

    # MOVE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        velocity.y = 1
        status = 'up'
    elif keys[pygame.K_DOWN]:
        velocity.y = -1
        status = 'down'
    else:
        velocity.y = 0
    if keys[pygame.K_RIGHT]:
        velocity.x = -1
        status = 'right'
    elif keys[pygame.K_LEFT]:
        velocity.x = 1
        status = 'left'
    else:
        velocity.x = 0
    
    # RESET STATUS
    if velocity.x == 0 and velocity.y == 0:
        status = 'idle'

    # ANIMATIONS
    if an_index >= len(an_frames[status]) - 1:
        an_index = 0
        

    an_index = round(an_index, 1)
    print(status)
    an_index += an_speed
    img = an_frames[status][int(an_index)]



# ENEMY
enemy_img = pygame.Surface((50,50))
enemy_img.fill('red')
enemy_rect = enemy_img.get_rect(center=(WIDTH/3, HEIGHT/3))
movable_sprites.append(enemy_rect)

def update_enemy():
    screen.blit(enemy_img,enemy_rect)

def move_world():
    for rectangle in movable_sprites:
        rectangle.x += velocity.x * speed 
        rectangle.y += velocity.y * speed 

while True:
    # EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # UPDATE
    screen.fill(BG_COLOR)
    update_player()
    update_enemy()
    move_world()
    clock.tick(FPS)
    pygame.display.update()