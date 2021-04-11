import pygame
import random
import math
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
        self.claimed = '0'
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
            self.drawScoreboard()
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
    
    def drawScoreboard(self):
        centerX = ((745-474)//2) + 474 #center of the scoreboard

        #Upper Border
        pygame.draw.rect(self.win, (109, 67, 234), (469, 50, 281, 5))
        #Left Border
        pygame.draw.rect(self.win, (109, 67, 234), (469, 50, 5, 400))
        #Lower Border
        pygame.draw.rect(self.win, (109, 67, 234), (469, 445, 281, 5))
        #Right Border
        pygame.draw.rect(self.win, (109, 67, 234), (745, 50, 5, 400))

        #Title Text
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        font = pygame.font.Font('freesansbold.ttf', 64)
        text_Colour = (red, green, blue)
        text_Background = (0,0,0) 
        text = font.render('QIX', True, text_Colour, text_Background)
        text_Rect = text.get_rect()
        text_Rect.center = (centerX, 110)
        self.win.blit(text, text_Rect)

        #Hearts
        font = pygame.font.SysFont('segoeuisymbol', 32)
        text_Colour = (243, 149, 182)
        text_Background = (0,0,0) 
        text = font.render('❤'*self.player.lives, True, text_Colour, text_Background)
        text_Rect = text.get_rect()
        text_Rect.center = (centerX, 200)
        self.win.blit(text, text_Rect)

        #Precentage Claimed 
        if not self.grid.travel:
            self.claimed = str(math.floor(self.grid.getClaimed()))
        font = pygame.font.Font('freesansbold.ttf', 24)
        text_Colour = (205, 191, 248)
        text_Background = (0,0,0) 
        text_String = 'Claimed: ' + self.claimed + '%'
        text = font.render(text_String, True, text_Colour, text_Background)
        text_Rect = text.get_rect()
        text_Rect.center = (centerX, 250)
        self.win.blit(text, text_Rect)

    def reset(self):
        print("RESET")
        self.player.reset()
        self.grid.reset()
main()

pygame.quit()