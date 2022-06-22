import pygame
from pygame.locals import *
from .fractals import *

pygame.init()

class App():
    def __init__(self, ScreenSize, caption, fps):
        self.screen = pygame.display.set_mode(ScreenSize)
        pygame.display.set_caption(caption)

        self.fps = fps
        self.clock = pygame.time.Clock()


    def loop(self):
        screen = self.screen
        while True:
            self.clock.tick(self.fps)
            screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    raise SystemExit

            pygame.display.update()