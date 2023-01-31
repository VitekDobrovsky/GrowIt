import pygame
import sys


# SETTINGS
WIDTH = 800
HEIGHT = 650
FPS = 60
BG_COLOR = '#F2E0C6'

# SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# PLAYER
img = pygame.image.load('graphics/player/idle/1.png').convert_alpha()
rect = img.get_rect(center=(WIDTH/2, HEIGHT/2))
velocity = pygame.math.Vector2()
speed = 5

def update_player():
    screen.blit(img, rect)
    
    # MOVE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        velocity.y = -1
    elif keys[pygame.K_DOWN]:
        velocity.y = 1
    else:
        velocity.y = 0
    if keys[pygame.K_RIGHT]:
        velocity.x = 1
    elif keys[pygame.K_LEFT]:
        velocity.x = -1
    else:
        velocity.x = 0
    
    rect.x += velocity.x * speed
    rect.y += velocity.y * speed


while True:
    # EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # UPDATE
    screen.fill(BG_COLOR)
    update_player()
    clock.tick(FPS)
    pygame.display.update()