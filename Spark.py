from Player import Player

class Spark(Player):
    def __init__(self,coord,velocity,grid):
        self.coord = coord
        self.velocity = velocity
        self.grid = grid
        self.next = 1
    def checkCollision(self):
        if self.coord == self.grid.coord:
            # print(self.coord)
            # print(self.grid.coord)
            return True
    def followBounds(self):
        self.pos = self.grid.totalVertex[self.next]
        if self.coord == self.pos:
            if self.next+1 == len(self.grid.totalVertex):
                self.next = 0
            else:
                self.next+=1
            self.pos = self.grid.totalVertex[self.next]
        self.x = self.pos[0]
        self.y = self.pos[1]

        if self.x - self.coord[0] >= 1:
            self.coord[0]+=1
        elif self.x - self.coord[0] < 0:
            self.coord[0]-=1
        elif self.y - self.coord[1] >= 1:
            self.coord[1]+=1
        elif self.y - self.coord[1] < 0:
            self.coord[1]-=1

