import pygame
import random


class Tile:
    def __init__(self, surface, position):
        self.colors = {2: (255, 0, 0), 4: (0, 255, 0)}
        self.value = random.randint(1, 2) * 2
        self.font = pygame.font.Font('Ubuntu-Regular.ttf', 32)
        self.surface = surface
        self.position = position
        self.color = self.colors[self.value]
        self.posAdapt = lambda x: x * 50
        self.fontRender = self.font.render(str(self.value), True, (255, 255, 255))

    def draw(self):
        pygame.draw.rect(self.surface, self.color,
                         (self.posAdapt(self.position[0]), self.posAdapt(self.position[1]), 50, 50))
        self.surface.blit(self.fontRender, (self.posAdapt(self.position[0])+5, self.posAdapt(self.position[0])+10))

    def fontRenderUpdate(self):
        self.fontRender = self.font.render(str(self.value), True, (255, 255, 255))