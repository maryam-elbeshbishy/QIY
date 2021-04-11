import pygame
from Block import Block
from Grid import Grid
from Player import Player
from Spark import Spark
from Qix import Qix
class main():
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((800,500))
        pygame.display.set_caption("QIX")
        self.gridSize = 80
        self.coord = [40,79]
        self.width = 5
        self.velocity = 5
        self.x = self.coord[0]*self.velocity
        self.y = self.coord[1]*self.velocity
        self.block = Block()
        self.grid = Grid(self.gridSize, self.block)
        self.player = Player(self.coord,self.velocity,self.grid)
        self.spark = Spark([40,0],self.velocity,self.grid)
        self.qix = Qix([40,40],self.velocity,self.grid)
        # print(self.block.getWhite())
        self.start()
    def start(self):
        run = True
        while run:
            pygame.time.delay(65)

            self.spark.followBounds()
            self.qix.findDirection()
            if self.spark.checkCollision():
                self.reset()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            self.keys = pygame.key.get_pressed()
            self.win.fill(self.block.getBlackColor())
            if self.keys[pygame.K_LEFT]:
                self.player.moveLeft()
            elif self.keys[pygame.K_RIGHT]:
                self.player.moveRight()
            elif self.keys[pygame.K_UP]:
                self.player.moveUp()
            elif self.keys[pygame.K_DOWN]:
                self.player.moveDown()
            self.drawGrid()
            self.drawEntities()
            # print("HEYL")
            pygame.display.update()
    def drawGrid(self):
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if self.grid.getGrid([i,j]) == 1:
                    pygame.draw.rect(self.win, (255, 255, 255),
                                     (50 + 5 * i, 50 + 5 * j, self.width, self.width))
                if self.grid.getGrid([i, j]) == 2:
                    pygame.draw.rect(self.win, (128, 128, 128),
                                     (50 + 5 * i, 50 + 5 * j, self.width, self.width))
                if self.grid.getGrid([i, j]) == 3:
                    pygame.draw.rect(self.win, self.block.getOrangeColor(),
                                     (50 + 5 * i, 50 + 5 * j, self.width, self.width))
    def drawEntities(self):
        pygame.draw.rect(self.win, (255, 0, 0),
                         (50 + self.player.coord[0]*self.velocity - 3, 50 + self.player.coord[1]*self.velocity - 3,
                          self.width + 6, self.width + 6))
        pygame.draw.rect(self.win, (255, 105, 180), (50 + self.spark.coord[0] * self.velocity - 3,
                                                     50 + self.spark.coord[1] * self.velocity - 3,
                                                     self.width + 4, self.width + 4))
        pygame.draw.rect(self.win, (0, 100, 255),
                         (50 + self.qix.coord[0] * self.velocity - 4, 50 + self.qix.coord[1] * self.velocity - 4,
                          self.width + 6, self.width + 6))
    def reset(self):
        print("HELLO")
        self.player.reset()
        self.grid.reset()
main()

pygame.quit()