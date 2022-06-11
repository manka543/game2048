import pygame
import tile
import random


class Game:
    def __init__(self):
        self.running = None
        pygame.init()
        self.screen = pygame.display.set_mode((900, 900))
        self.tiles = []
        self.generateTiles()
        self.gameLoop()


    def graphic(self):
        self.screen.fill((0, 0, 0))
        for i in self.tiles:
            i.draw()
        pygame.display.update()

    def gameLoop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("up")
                    elif event.key == pygame.K_DOWN:
                        print("down")
                    elif event.key == pygame.K_RIGHT:
                        print("right")
                    elif event.key == pygame.K_LEFT:
                        print("left")
            self.graphic()

    def generateTiles(self):
        for i in range(2):
            self.generateTile()

    def generateTile(self):
        while True:
            i = (random.randint(0, 4), random.randint(0, 4))
            if not i in self.tiles:
                break
        self.tiles.append(tile.Tile(self.screen, i))


game = Game()
