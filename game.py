import pygame
import tile
import random
import json


# TODO: switch font renders to other data structure
# TODO: animacje przesuwania klocków
# TODO: punkty
# TODO: Przyciski
# Todo: Reset gry
# TODO: poprawić wyświetlanie się punktów na tilesach

class Game:
    def __init__(self):
        # First
        pygame.init()
        # Loading save
        self.file = open("save.json")
        self.save = json.load(self.file)
        self.file.close()
        # Order does not care
        self.running = True
        self.gameEnd = False
        self.fps = self.save["fps"]
        self.points = 0
        self.centerText = lambda x, y: x - (y * 9)
        self.moveDirection = None
        self.moveDict = {'r': 1, 'l': -1, 'u': -1, 'd': 1}
        self.moving = None
        # Font load
        self.font100 = pygame.font.Font('Ubuntu-Regular.ttf', 100)
        self.font70 = pygame.font.Font('Ubuntu-Regular.ttf', 70)
        self.font24 = pygame.font.Font('Ubuntu-Regular.ttf', 24)
        self.font32 = pygame.font.Font('Ubuntu-Regular.ttf', 32)
        # Render texts
        self.nameRender = self.font100.render("2048", True, (255, 255, 255))
        self.gameModeRender = self.font70.render("5x5", True, (116, 0, 255))
        self.highScoreRender = self.font24.render("HIGH SCORE", True, (255, 255, 255))
        self.scoreRender = self.font24.render("SCORE", True, (255, 255, 255))
        self.scoreRenderNumber = self.renderPoints(self.points)
        self.highScoreRenderNumber = self.renderPoints(self.save["points"]["5x5"])
        self.gameEndRender = self.font70.render("Game over!!!", True, (116, 0, 255))
        # Load icons
        self.resetIcon = pygame.image.load("reset.png")
        self.backIcon = pygame.image.load("back.png")
        # Creating screen
        self.screen = pygame.display.set_mode((600, 800))
        # Generating tiles
        self.tiles = [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None],
                      [None, None, None, None, None],
                      [None, None, None, None, None]]
        self.generateTiles()
        # Set timer to have stable frame rate
        self.clock = pygame.time.Clock()

        # Last
        self.loop()

    def graphic(self):
        self.screen.fill((91, 32, 32))
        pygame.draw.rect(self.screen, (62, 44, 44), (45, 245, 510, 510), 0, 10)
        for i in range(5):
            for j in range(5):
                pygame.draw.rect(self.screen, (122, 96, 96), (i * 100 + 55, j * 100 + 255, 90, 90), 0, 10)
        pygame.draw.rect(self.screen, (62, 44, 44), (260, 20, 150, 90), 0, 10)
        pygame.draw.rect(self.screen, (62, 44, 44), (425, 20, 150, 90), 0, 10)
        pygame.draw.rect(self.screen, (62, 44, 44), (290, 125, 100, 100), 0, 10)
        pygame.draw.rect(self.screen, (62, 44, 44), (450, 125, 100, 100), 0, 10)
        self.screen.blit(self.nameRender, (15, 4))
        self.screen.blit(self.gameModeRender, (65, 130))
        self.screen.blit(self.highScoreRender, (430, 30))
        self.screen.blit(self.scoreRender, (295, 30))
        self.screen.blit(self.scoreRenderNumber, (self.centerText(335, len(str(self.points))), 55))
        self.screen.blit(self.highScoreRenderNumber, (self.centerText(500, len(str(self.points))), 55))
        self.screen.blit(self.resetIcon, (468, 143))
        self.screen.blit(self.backIcon, (308, 143))

        for i in range(5):
            for j in range(5):
                if not self.tiles[i][j] is None:
                    self.tiles[i][j].draw()

        if self.gameEnd:
            pass

        pygame.display.update()

    def renderPoints(self, x):
        return self.font32.render(str(x), True, (255, 255, 255))

    def generateTiles(self):
        for i in range(2):
            self.generateTile()

    def generateTile(self):
        free_Space = []
        for i in range(5):
            for j in range(5):
                if self.tiles[i][j] is None:
                    free_Space.append((i, j))
        if len(free_Space) == 0:
            self.gameEnd = True
        else:
            K = free_Space[random.randint(0, len(free_Space)-1)]
            self.tiles[K[0]][K[1]] = tile.Tile(self.screen, K)

    def returnRange(self):
        if self.moveDirection == "l" or self.moveDirection == "u":
            return range(5)
        else:
            return 4, 3, 2, 1, 0

    def move(self):
        self.moving = True
        while self.moving:
            self.moving = False
            for i in self.returnRange():
                for j in self.returnRange():
                    if self.moveDirection == "r":
                        if self.tiles[i][j] is not None and i != 4:
                            if self.tiles[i + 1][j] is None:
                                self.tiles[i][j].position = (i + 1, j)
                                self.tiles[i + 1][j] = self.tiles[i][j]
                                self.tiles[i][j] = None
                                self.moving = True
                            elif self.tiles[i + 1][j].value == self.tiles[i][j].value:
                                self.tiles[i + 1][j].doubleValue()
                                self.tiles[i][j] = None
                    elif self.moveDirection == "l":
                        if self.tiles[i][j] is not None and i != 0:
                            if self.tiles[i - 1][j] is None:
                                self.tiles[i][j].position = (i - 1, j)
                                self.tiles[i - 1][j] = self.tiles[i][j]
                                self.tiles[i][j] = None
                                self.moving = True
                            elif self.tiles[i - 1][j].value == self.tiles[i][j].value:
                                self.tiles[i - 1][j].doubleValue()
                                self.tiles[i][j] = None
                    elif self.moveDirection == "u":
                        if self.tiles[i][j] is not None and j != 0:
                            if self.tiles[i][j - 1] is None:
                                self.tiles[i][j].position = (i, j - 1)
                                self.tiles[i][j - 1] = self.tiles[i][j]
                                self.tiles[i][j] = None
                                self.moving = True
                            elif self.tiles[i][j - 1].value == self.tiles[i][j].value:
                                self.tiles[i][j - 1].doubleValue()
                                self.tiles[i][j] = None
                    elif self.moveDirection == "d":
                        if self.tiles[i][j] is not None and j != 4:
                            if self.tiles[i][j + 1] is None:
                                self.tiles[i][j].position = (i, j + 1)
                                self.tiles[i][j + 1] = self.tiles[i][j]
                                self.tiles[i][j] = None
                                self.moving = True
                            elif self.tiles[i][j + 1].value == self.tiles[i][j].value:
                                self.tiles[i][j + 1].doubleValue()
                                self.tiles[i][j] = None
        self.moveDirection = None
        self.generateTile()

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if self.moveDirection is None:
                        if event.key == pygame.K_UP:
                            print("up")
                            self.moveDirection = "u"
                        elif event.key == pygame.K_DOWN:
                            print("down")
                            self.moveDirection = "d"
                        elif event.key == pygame.K_RIGHT:
                            print("right")
                            self.moveDirection = "r"
                        elif event.key == pygame.K_LEFT:
                            print("left")
                            self.moveDirection = "l"
                        self.move()
            self.graphic()
            self.clock.tick(self.fps)


game = Game()
