import pygame
from settings import *
from level import Level
from sys import exit


class GrowIt:
    def __init__(self):
        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        active = True
        while active:
            # event listener
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    active = False
            #update
            self.screen.fill(BG_COLOR)
            self.clock.tick(FPS)
            self.level.update()
            pygame.display.update()


if __name__ == '__main__':
    game = GrowIt()
    game.run()            

