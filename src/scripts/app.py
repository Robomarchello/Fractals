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
        self.ToothPickSeq = ToothPickSeq(ScreenSize, 32)

        #write one of the fractals you want to run
        self.fractal = self.ToothPickSeq

    def loop(self):
        screen = self.screen

        screen.fill((255, 255, 255))
        self.fractal.draw(screen) 

        while True:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    raise SystemExit
                
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.fractal.steps += 1
                        screen.fill((255, 255, 255))
                        self.fractal.draw(screen) 
                        
            pygame.display.update()

#[<rect(64, 64, 64, 64)>, <rect(192, 64, 64, 64)>, <rect(320, 64, 64, 64)>, <rect(64, 192, 64, 64)>, <rect(320, 192, 64, 64)>, <rect(64, 320, 64, 64)>, <rect(192, 320, 64, 64)>, <rect(320, 320, 64, 64)>]