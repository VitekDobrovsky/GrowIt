import pygame
from player import Player
from enemy import Enemy
from random import randint


class Level:
    def __init__(self):
        # setup
        self.screen = pygame.display.get_surface()
        self.visibleSprites = pygame.sprite.Group()
        self.current_time = None

        # map
        self.map = pygame.image.load('graphics/background.png').convert_alpha()
        self.mapRect = self.map.get_rect(topleft=(0,0))

        # player
        self.player = Player([self.visibleSprites])

        # enemy
        self.enemies = pygame.sprite.Group()
            #spawn
        self.canSpawn = True
        self.spawnTimer = None
        self.spawnCooldown = 10000

    def spawnEnemy(self):
        if self.canSpawn:
            Enemy((randint(0, 750), randint(0,600)), [self.enemies])
            self.spawnTimer = pygame.time.get_ticks()
            self.canSpawn = False
        
        value = self.cooldown(self.current_time, self.canSpawn, self.spawnTimer, self.spawnCooldown)      
        self.canSpawn = value

    def cooldown(self, current, var, varTime, cooldown):
        if not var:
            if current - varTime >= cooldown:
                return True
            else:
                return False
  
    def update(self):
        # set current time
        self.current_time = pygame.time.get_ticks()
        
        # enemies
        self.spawnEnemy()
        for enemy in self.enemies:
            enemy.checkDeath(self.player)
        
        # draw map
        self.screen.blit(self.map, self.mapRect)
        
        # update sprites
        self.visibleSprites.draw(self.screen)
        self.visibleSprites.update()
        # update enemies
        self.enemies.draw(self.screen)
        self.enemies.update(self.player)