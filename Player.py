
class Player(object):
    def __init__(self,coord,velocity,grid):
        self.coord = coord
        self.velocity = velocity
        self.x = self.coord[0]*velocity
        self.y = self.coord[1] * velocity
        self.grid = grid
        self.direction = -1
        self.lives = 5

    def removeLives(self):
        self.lives-=1

    def moveRight(self):
        if self.grid.travel and self.direction!=0:
            self.direction = 0
            self.grid.addToVertex()
        self.coord = self.grid.updatePlayerX(1)
        self.x = self.coord[0]*self.velocity
    def moveLeft(self):
        if self.grid.travel and self.direction!=1:
            self.direction = 1
            self.grid.addToVertex()
        self.coord = self.grid.updatePlayerX(-1)
        self.x = self.coord[0]*self.velocity
    def moveUp(self):
        if self.grid.travel and self.direction!=2:
            self.direction = 2
            self.grid.addToVertex()
        self.coord = self.grid.updatePlayerY(-1)
        self.y = self.coord[1] * self.velocity
        # print(self.y)

    def moveDown(self):
        if self.grid.travel and self.direction!=3:
            self.direction = 3
            self.grid.addToVertex()
        self.coord = self.grid.updatePlayerY(1)
        self.y = self.coord[1] * self.velocity

    def reset(self):
        self.removeLives()
        self.coord = [40,79]