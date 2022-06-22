from numpy import square
import pygame

class sCarpet:
    def __init__(self, ScreenSize, steps):
        self.ScreenSize = ScreenSize
        self.color = pygame.Color('black')
        self.steps = steps

    def draw(self, screen):
        squares = [
            pygame.Rect(0, 0, self.ScreenSize[0] // 3, self.ScreenSize[1] // 3)
            ]
        squares[0].center = (self.ScreenSize[0] // 2, self.ScreenSize[1] // 2)

        pygame.draw.rect(screen, self.color, squares[0])

        for step in range(self.steps):
            new_squares = []
            for square in squares:
                new_squares += self.slice_square(square)
                
            squares = new_squares.copy()

            for square in new_squares:
                #pygame.draw.circle(screen, self.color, square.center, square.width//2)
                pygame.draw.rect(screen, self.color, square)
                
    def slice_square(self, rect):
        '''Splits a square into 8 3 times smaller squares😅'''

        squares = []
        cutSize = (rect.width // 3, rect.height // 3)
        directions = [
            pygame.Vector2(-rect.width, -rect.height),
            pygame.Vector2(0, -rect.height),
            pygame.Vector2(rect.width, -rect.height),
            pygame.Vector2(-rect.width, 0),
            pygame.Vector2(rect.width, 0),
            pygame.Vector2(-rect.width, rect.height),
            pygame.Vector2(0, rect.height),
            pygame.Vector2(rect.width, rect.height),
        ]

        for direction in directions:
            new_rect = pygame.Rect((0, 0), cutSize)
            new_rect.center = rect.center + direction
            squares.append(new_rect.copy())

        return squares
