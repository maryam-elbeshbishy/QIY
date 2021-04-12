from Player import Player

class Spark(Player):
    def __init__(self,coord,velocity,grid, direction):
        self.coord = coord
        self.velocity = velocity
        self.grid = grid
        self.next = 1
        self.direction = direction
        self.isGrey = False
    def getColor(self):
        return (255, 130, 220)
    def checkCollision(self):
        if self.coord == self.grid.coord:
            # print(self.coord)
            # print(self.grid.coord)
            return True
    def checkGrey(self):
        count = 0
        if 0 < self.coord[0] < 79 and 0 < self.coord[1] < 79:
            if self.grid.getGrid([self.coord[0]+1,self.coord[1]]) == 2:
                count+=1
                if self.grid.getGrid([self.coord[0]-1,self.coord[1]]) == 2:
                    count+=1
            elif self.grid.getGrid([self.coord[0],self.coord[1]+1]) == 2:
                count+=1
                if self.grid.getGrid([self.coord[0],self.coord[1]-1]) == 2:
                    count+=1
            if count > 1:
                self.isGrey = True
    def followBounds(self):
        # print("----")
        for i in range(2):
            self.checkGrey()
            # print(self.isGrey)
            if self.direction == 0:
                # print("right")
                self.right()
            elif self.direction == 1:
                # print("LEFT")
                self.left()
            elif self.direction == 2:
                # print("UP")
                self.up()
            elif self.direction == 3:
                # print("DOWN")
                self.down()
            if self.checkCollision():
                break
        self.isGrey = False

    def right(self):
        if self.coord[1] != 79:
            if self.grid.getGrid([self.coord[0], self.coord[1] + 1]) == 1 and self.isGrey==False:
                self.coord[1] += 1
                self.direction = 3
                return
        if self.coord[0] != 79:
            if self.grid.getGrid([self.coord[0]+1, self.coord[1]]) == 1:
                if self.checkGrey():
                    for i in range(2):
                        if self.grid.getGrid([self.coord[0] + 1, self.coord[1]]) == 1:
                            self.coord[0] += 1
                else:
                    self.coord[0]+=1
                return
        if self.coord[1] != 0:
            if self.grid.getGrid([self.coord[0], self.coord[1] - 1]) == 1 and self.isGrey==False:
                self.coord[1] -= 1
                self.direction = 2
                return
    def left(self):
        if self.coord[1] != 0:
            if self.grid.getGrid([self.coord[0], self.coord[1] - 1]) == 1 and self.isGrey==False:
                self.coord[1] -= 1
                self.direction = 2
                return
        if self.coord[0] != 0:
            if self.grid.getGrid([self.coord[0]-1, self.coord[1]]) == 1:
                if self.isGrey == True:
                    for i in range(2):
                        if self.grid.getGrid([self.coord[0] - 1, self.coord[1]]) == 1:
                            self.coord[0] -= 1
                else:
                    self.coord[0] -= 1
                return
        if self.coord[1] != 79:
            if self.grid.getGrid([self.coord[0], self.coord[1] + 1]) == 1 and self.isGrey==False:
                self.coord[1] += 1
                self.direction = 3
                return
    def up(self):
        if self.coord[0] != 79:
            if self.grid.getGrid([self.coord[0]+1, self.coord[1]]) == 1 and self.isGrey==False:
                self.coord[0] += 1
                self.direction = 0
                return
        if self.coord[1] != 0:
            if self.grid.getGrid([self.coord[0], self.coord[1] - 1]) == 1:
                if self.isGrey == True:
                    for i in range(2):
                        if self.grid.getGrid([self.coord[0], self.coord[1] - 1]) == 1:
                            self.coord[1] -= 1
                else:
                    self.coord[1]-=1
                self.direction = 2
                return
        if self.coord[0] != 0:
            if self.grid.getGrid([self.coord[0]-1, self.coord[1]]) == 1 and self.isGrey==False:
                self.coord[0] -= 1
                self.direction = 1
                return
    def down(self):
        if self.coord[0] != 0:
            if self.grid.getGrid([self.coord[0]-1, self.coord[1]]) == 1 and self.isGrey==False:
                self.coord[0] -= 1
                self.direction = 1
                return
        if self.coord[1] != 79:
            if self.grid.getGrid([self.coord[0], self.coord[1] + 1]) == 1:
                if self.isGrey == True:
                    for i in range(2):
                        if self.grid.getGrid([self.coord[0], self.coord[1] + 1]) == 1:
                            self.coord[1] += 1
                else:
                    self.coord[1] += 1
                self.direction = 3
                return
        if self.coord[0] != 79:
            if self.grid.getGrid([self.coord[0]+1, self.coord[1]]) == 1 and self.isGrey==False:
                self.coord[0] += 1
                self.direction = 0
                return
    # def followBounds(self):
    #     for i in range(2):
    #         self.pos = self.grid.totalVertex[self.next]
    #         if self.coord == self.pos:
    #             if self.next+1 == len(self.grid.totalVertex):
    #                 self.next = 0
    #             else:
    #                 self.next+=1
    #             self.pos = self.grid.totalVertex[self.next]
    #         self.x = self.pos[0]
    #         self.y = self.pos[1]
    #
    #         if self.x - self.coord[0] >= 1:
    #             self.coord[0]+=1
    #             if self.checkCollision():
    #                 break
    #         elif self.x - self.coord[0] < 0:
    #             self.coord[0]-=1
    #             if self.checkCollision():
    #                 break
    #         elif self.y - self.coord[1] >= 1:
    #             self.coord[1]+=1
    #             if self.checkCollision():
    #                 break
    #         elif self.y - self.coord[1] < 0:
    #             self.coord[1]-=1
    #             if self.checkCollision():
    #                 break

