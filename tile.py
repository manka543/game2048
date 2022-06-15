import pygame
import random


class Tile:
    def __init__(self, surface, position):
        self.colors = {2: (255, 0, 0), 4: (0, 255, 0), 8: (0, 0, 255), 16: (0, 0, 255), 32: (255, 255, 0),
                       64: (0, 255, 255), 128: (255, 0, 255), 256: (192, 192, 192), 512: (0, 0, 128),
                       1024: (128, 0, 128), 2048: (0, 128, 128)}
        self.value = random.randint(1, 2) * 2
        self.font = pygame.font.Font('Ubuntu-Regular.ttf', 64)
        self.surface = surface
        self.position = position
        self.color = self.colors[self.value]
        self.posAdapt = lambda x: x * 100
        self.fontRender = self.font.render(str(self.value), True, (255, 255, 255))

    def draw(self):
        pygame.draw.rect(self.surface, self.color,
                         (self.posAdapt(self.position[0]) + 55, self.posAdapt(self.position[1]) + 255, 90, 90), 0, 10)
        self.surface.blit(self.fontRender,
                          (self.posAdapt(self.position[0]) + 81, self.posAdapt(self.position[1]) + 262))

    def fontRenderUpdate(self):
        self.fontRender = self.font.render(str(self.value), True, (255, 255, 255))

    def doubleValue(self):
        self.value *= 2
        self.color = self.colors[self.value]
        self.fontRenderUpdate()
