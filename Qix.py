from Player import Player
import random
class Qix(Player):
    def __init__(self,coord,velocity,grid,speed):
        self.speed = speed
        self.coord = coord
        self.velocity = velocity
        self.grid = grid
        self.count = 0
        self.direction = random.randint(0,3)
        self.collision = False
    def checkCollision(self):
        collision = self.collision
        self.collision= False
        return collision
    def findDirection(self):
        # print(self.coord)
        self.monkey = random.randint(8,16)
        self.grid.updateGrid(self.coord,0)
        if self.count>=self.monkey:
            self.count = 0
            self.direction = random.randint(0,3)
        for i in range(self.monkey):
            if i%self.speed == 0:
                self.move()

    def move(self):
        self.grid.updateGrid(self.coord,0)
        if self.direction == 0:
            self.moveUpwards()
        if self.direction == 1:
            self.moveDownwards()
        if self.direction == 2:
            self.moveLeftwards()
        if self.direction == 3:
            self.moveRightwards()

    def moveUpwards(self):
        if self.grid.getGrid([self.coord[0], self.coord[1] - 1]) == 3 or self.coord == self.grid.coord:
            self.collision = True
        if self.grid.getGrid([self.coord[0],self.coord[1]-1]) !=1:
            self.coord[1]-=1
        self.grid.updateGrid(self.coord, 4)
        self.count+=1
    def moveDownwards(self):
        if self.grid.getGrid([self.coord[0], self.coord[1] + 1]) == 3 or self.coord == self.grid.coord:
            self.collision = True
        if self.grid.getGrid([self.coord[0],self.coord[1]+1]) !=1:
            self.coord[1]+=1
        self.grid.updateGrid(self.coord, 4)
        self.count+=1
    def moveLeftwards(self):
        if self.grid.getGrid([self.coord[0]-1, self.coord[1]]) == 3 or self.coord == self.grid.coord:
            self.collision = True
        if self.grid.getGrid([self.coord[0]-1, self.coord[1]]) != 1:
            self.coord[0] -= 1
        self.grid.updateGrid(self.coord, 4)
        self.count+=1
    def moveRightwards(self):
        if self.grid.getGrid([self.coord[0]+1, self.coord[1]]) == 3 or self.coord == self.grid.coord:
            self.collision = True
        if self.grid.getGrid([self.coord[0]+1, self.coord[1]]) != 1:
            self.coord[0] += 1
        self.grid.updateGrid(self.coord, 4)
        self.count+=1