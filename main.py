import pygame
import random
import math
from Block import Block
from Grid import Grid
from Player import Player
from Spark import Spark
from Qix import Qix
class main():
    def __init__(self, require, level):
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
        self.spark = Spark([40,0],self.velocity,self.grid,0)
        self.spark2 = Spark([40,0],self.velocity,self.grid,1)
        if level > 1:
            self.spark3 = Spark([0,40],self.velocity,self.grid,3)
        if level > 2:
            self.spark4 = Spark([0,40],self.velocity,self.grid,2)
        self.level = level
        if self.level > 5:
            self.qix = Qix([40,40],self.velocity,self.grid,3)
        else:
            self.qix = Qix([40,40],self.velocity,self.grid,30-self.level*5)
        self.claimed = 0
        self.requiredClaimed = require

        # print(self.block.getWhite())
        if self.level == 1:
            self.startScreen()
        else:
            self.game()

    def startScreen(self):
        self.fade(100)
        run = True
        con = False
        while run:
            pygame.time.delay(65)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    con = False
                    break
                if event.type == pygame.KEYDOWN: 
                    run = False
                    con = True 
            self.drawStartScreen()
            pygame.display.update()
        if con:
            self.game()

    def game(self):
        self.fade(200)
        endScreen = False
        nextLevel = False
        run = True
        while run:
            pygame.time.delay(30)
            if self.spark.checkCollision() or self.spark2.checkCollision():
                self.reset()
            if self.level > 1:
                if self.spark3.checkCollision():
                    self.reset()
                self.spark3.followBounds()
            if self.level > 2:
                if self.spark4.checkCollision():
                    self.reset()
                self.spark4.followBounds()
            self.spark.followBounds()
            self.spark2.followBounds()
            self.qix.findDirection()
            if self.player.lives == 0:
                run = False
                endScreen = True
                break
            if self.claimed >= self.requiredClaimed:
                run = False
                nextLevel = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endScreen = False
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
            elif self.keys[pygame.K_r]:
                endScreen = True
                run = False
            self.drawGrid()
            self.drawEntities()
            self.drawScoreboard()
            pygame.display.update()
        if endScreen:
            self.endScreen('lost')
        if nextLevel:
            if self.level + 1 == 11:
                self.endScreen('won')
            else:
                self.nextLevelPause()
                self.__init__(self.requiredClaimed+5, self.level+1)

    def nextLevelPause(self):
        self.fade(50)
        self.drawNextLevelPause()
        run = True
        while run:
            pygame.time.delay(65)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return
                if event.type == pygame.KEYDOWN: 
                    run = False
                    return
            pygame.display.update()


    def endScreen(self, result):
        self.fade(100)
        startScreen = False
        run = True
        while run:
            pygame.time.delay(65)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    startScreen = False
                    break
                if event.type == pygame.KEYDOWN: 
                    run = False
                    startScreen = True 
            self.drawEndScreen(result)
            pygame.display.update()
        if startScreen:
            self.__init__(60,1)

    def drawStartScreen(self):
        self.win.fill((0,0,0))
        centerX = 400
        #Qix title
        text = 'QIX'
        self.drawText('freesansbold.ttf', 200, (205, 191, 248), text, centerX, 200)
        #Press any key
        text = 'Press any key to start'
        self.drawText('freesansbold.ttf', 32, (205, 191, 248), text, centerX, 400)
        #Bottom credits
        text = 'Recreated By: Abdullah Aftab, My Chi Duong, Maryam Elbeshbishy, Igor Goncalves Penedos, Deandra Spike-Madden'
        self.drawText('freesansbold.ttf', 13, (205, 191, 248), text, centerX, 470)

    def drawGrid(self):
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if self.grid.getGrid([i,j]) == 1:
                    pygame.draw.rect(self.win, (255, 255, 255),
                                     (50 + 5 * i, 50 + 5 * j, self.width, self.width))
                if self.grid.getGrid([i, j]) == 2:
                    pygame.draw.rect(self.win, self.block.getGreyColor(),
                                     (50 + 5 * i, 50 + 5 * j, self.width, self.width))
                if self.grid.getGrid([i, j]) == 3:
                    pygame.draw.rect(self.win, self.block.getOrangeColor(),
                                     (50 + 5 * i, 50 + 5 * j, self.width, self.width))

    def drawEntities(self):
        pygame.draw.rect(self.win, (255, 0, 0),
                         (50 + self.player.coord[0]*self.velocity - 3, 50 + self.player.coord[1]*self.velocity - 3,
                          self.width + 6, self.width + 6))
        pygame.draw.rect(self.win, self.spark.getColor(), (50 + self.spark.coord[0] * self.velocity - 3,
                                                     50 + self.spark.coord[1] * self.velocity - 3,
                                                     self.width + 4, self.width + 4))
        pygame.draw.rect(self.win, self.spark.getColor(), (50 + self.spark2.coord[0] * self.velocity - 3,
                                                     50 + self.spark2.coord[1] * self.velocity - 3,
                                                     self.width + 4, self.width + 4))
        pygame.draw.rect(self.win, (0, 100, 255),
                         (50 + self.qix.coord[0] * self.velocity - 4, 50 + self.qix.coord[1] * self.velocity - 4,
                          self.width + 6, self.width + 6))
        if self.level > 1:
            pygame.draw.rect(self.win, self.spark.getColor(), (50 + self.spark3.coord[0] * self.velocity - 3,
                                                         50 + self.spark3.coord[1] * self.velocity - 3,
                                                         self.width + 4, self.width + 4))
        if self.level > 2:
            pygame.draw.rect(self.win, self.spark.getColor(), (50 + self.spark4.coord[0] * self.velocity - 3,
                                                         50 + self.spark4.coord[1] * self.velocity - 3,
                                                         self.width + 4, self.width + 4))

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
        self.drawText('freesansbold.ttf', 64, (red, green, blue), 'QIX', centerX, 110)
        #Hearts
        text = '❤'*self.player.lives
        self.drawText('segoeuisymbol', 32, (243, 149, 182), text, centerX, 200)
        #Precentage Claimed 
        if not self.grid.travel:
            self.claimed = math.floor(self.grid.getClaimed())
        text = 'Claimed: ' + str(self.claimed) + '/' + str(self.requiredClaimed) + '%'
        self.drawText('freesansbold.ttf', 24,(205, 191, 248),text, centerX, 250)
        #Level
        text = 'Level: ' + str(self.level)
        self.drawText('freesansbold.ttf', 24, (205, 191, 248), text, centerX, 300)

    def drawNextLevelPause(self):
        self.win.fill((0,0,0))
        centerX = 400
        #Completed level INT
        text = 'Completed Level ' + str(self.level)
        self.drawText('freesansbold.ttf', 50, (205, 191, 248), text, centerX, 100)
        #Claimed: INT%
        text = 'Completed: ' + str(self.claimed) + '%'
        self.drawText('freesansbold.ttf', 24, (205, 191, 248), text, centerX, 200)
        #Click anywhere to more to level INT
        text = 'Press any key to move to level '  + str(self.level + 1)
        self.drawText('freesansbold.ttf', 24, (205, 191, 248), text, centerX, 300)


    def drawEndScreen(self, result):
        self.win.fill((0,0,0))
        centerX = 400
        #YOU (Lost/Won)
        text = 'YOU ' + result.upper()
        self.drawText('freesansbold.ttf', 100, (205, 191, 248), text, centerX, 100)
        #Level: INT
        text = 'Level: ' + str(self.level)
        self.drawText('freesansbold.ttf', 24, (205, 191, 248), text, centerX, 200)
        #Claimed: INT
        text = 'Claimed: ' + str(self.claimed) + '%'
        self.drawText('freesansbold.ttf', 24, (205, 191, 248), text, centerX, 250)
        text = 'Press any key to move to RESTART'
        self.drawText('freesansbold.ttf', 24, (205, 191, 248), text, centerX, 400)

    def drawText(self, font, font_Size, colour, text_String, x, y ):
        font = pygame.font.SysFont(font, font_Size)
        text_Colour = colour
        text_Background = (0,0,0) 
        text = font.render(text_String, True, text_Colour, text_Background)
        text_Rect = text.get_rect()
        text_Rect.center = (x, y)
        self.win.blit(text, text_Rect)

    def fade(self, delay): 
        fade = pygame.Surface(((800,500)))
        fade.fill((0,0,0))
        for alpha in range(0, delay): #delay/100 = seconds
            fade.set_alpha(alpha)
            # redrawWindow()
            self.win.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(5)

    def reset(self):
        self.player.reset()
        self.grid.reset()
main(25, 1)

pygame.quit()