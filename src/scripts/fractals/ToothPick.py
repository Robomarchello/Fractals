#will try to write code after 11:00
import pygame

class ToothPickSeq:
    def __init__(self, ScreenSize, steps):
        self.center = pygame.Vector2(ScreenSize[0] // 2, ScreenSize[1] // 2)
        self.color = pygame.Color('black')

        self.length = 10
        self.steps = steps

        self.ToothPicks = []
        self.active = [
            [pygame.Vector2(self.center[0], self.center[1] - self.length),
            pygame.Vector2(self.center[0], self.center[1] + self.length)]
        ]

    def draw(self, screen):
        self.ToothPicks = []
        self.active = [
            [pygame.Vector2(self.center[0], self.center[1] - self.length),
            pygame.Vector2(self.center[0], self.center[1] + self.length)]
        ]

        gae = time.perf_counter()
        for step in range(self.steps):
            NewToothPicks = []
            for ToothPick in self.active:
                NewToothPicks += self.PlaceToothPicks(ToothPick)
            self.ToothPicks += self.active.copy()
            self.active = NewToothPicks

        for ToothPick in self.ToothPicks:#pygame.gfxdraw
            if ToothPick[0].x == ToothPick[1].x:
                pygame.draw.line(screen, self.color, ToothPick[0], ToothPick[1])
                
            if ToothPick[0].y == ToothPick[1].y:
                pygame.draw.line(screen, self.color, ToothPick[0], ToothPick[1])
            
        for ToothPick in self.active:
            pygame.draw.line(screen, pygame.Color('cyan'), ToothPick[0], ToothPick[1])

    def PlaceToothPicks(self, toothPick):
        AvailableSides = [True, True]
        
        for side in toothPick:
            for i, tPick in enumerate(self.active):
                if i != self.active.index(toothPick):
                    if tPick[0] == side or tPick[1] == side:
                        AvailableSides[toothPick.index(side)] = False

            for tPick in self.ToothPicks:
                if i != self.active.index(toothPick):
                    if tPick[0] == side or tPick[1] == side:
                        AvailableSides[toothPick.index(side)] = False

            
        ToothPicks = []
        if toothPick[0].x == toothPick[1].x:
            #place horizontal toothpicks
            if AvailableSides[0]:
                ToothPicks.append(
                    [
                        pygame.Vector2(toothPick[0].x - self.length, toothPick[0].y),
                        pygame.Vector2(toothPick[0].x + self.length, toothPick[0].y)
                    ])

            if AvailableSides[1]:
                ToothPicks.append(
                    [
                        pygame.Vector2(toothPick[0].x - self.length, toothPick[1].y),
                        pygame.Vector2(toothPick[0].x + self.length, toothPick[1].y)
                    ])

        if toothPick[0].y == toothPick[1].y:
            #place vertical toothpicks
            if AvailableSides[0]:
                ToothPicks.append(
                    [
                        pygame.Vector2(toothPick[0].x, toothPick[0].y - self.length),
                        pygame.Vector2(toothPick[0].x, toothPick[0].y + self.length)
                    ])

            if AvailableSides[1]:
                ToothPicks.append(
                    [
                        pygame.Vector2(toothPick[1].x, toothPick[0].y - self.length),
                        pygame.Vector2(toothPick[1].x, toothPick[0].y + self.length)
                    ])
        
        return ToothPicks

        #do something like "if one end of toothpick touches other end of some toothpick, then don't spawn"    