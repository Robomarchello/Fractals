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

        self.sCarpet = sCarpet(ScreenSize, 4)

    def loop(self):
        screen = self.screen
        
        while True:
            self.clock.tick(self.fps)
            screen.fill((255, 255, 255))
            
            self.sCarpet.draw(screen)  

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    raise SystemExit

            pygame.display.update()

#[<rect(64, 64, 64, 64)>, <rect(192, 64, 64, 64)>, <rect(320, 64, 64, 64)>, <rect(64, 192, 64, 64)>, <rect(320, 192, 64, 64)>, <rect(64, 320, 64, 64)>, <rect(192, 320, 64, 64)>, <rect(320, 320, 64, 64)>]