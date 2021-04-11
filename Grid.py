from copy import deepcopy

class Grid():
    def __init__(self,size,block):
        self.block = block          # Stores data about each block (mainly the block ID is what we're looking for)
        self.total =(size*size)-316 # this is the # of unclaimed blocks
        self.travel = False         # whether or not the player is in motion right now
        self.coord =[40,79]         # keeps coordinates of player
        self.current = []           # keeps current player path
        self.grid = []              # grid
        self.vertex = []            # keeps all the vertexes
        self.totalVertex = [[0,0],[79,0],[79,79],[0,79]]
        self.totalMotion = []       # keeps track of every single path
        self.size = size            # size of grid
        self.createGrid()           # calls the createGrid function that creates the grid system
# --------------------------------------- DATA COLLECTION FUNCTIONS -------------------------------------------
    def addToVertex(self):
        self.vertex.append([self.coord[0],self.coord[1]])
    def addLastVertex(self):
        if self.coord[0] == 0:
            self.vertex.append([self.coord[0] + 1, self.coord[1]])
            return
        elif self.coord[0] == 79:
            self.vertex.append([self.coord[0] - 1, self.coord[1]])
            return
        elif self.coord[1] == 0:
            self.vertex.append([self.coord[0], self.coord[1] + 1])
            return
        elif self.coord[1] == 79:
            self.vertex.append([self.coord[0], self.coord[1] - 1])
            return
        self.vertex.append([self.coord[0], self.coord[1]])
        return

    def addTotals(self):
        for i in range(len(self.vertex)):
            self.totalVertex.append(self.vertex[i])
        for i in range(len(self.current)):
            self.totalMotion.append(self.current[i])

    def getClaimed(self): 
        amountOfZeros = sum(x.count(0) for x in self.grid)
        sizeOfGrid = (len(self.grid))**2
        borderOfOnes = (len(self.grid)-1)*4
        return 100 - ((amountOfZeros)/(sizeOfGrid - borderOfOnes))*100
# --------------------------------------- GRID ACCESS/CREATION FUNCTIONS --------------------------------------
    def reset(self):
        self.coord = [40,79]
    def createGrid(self):
        for i in range(self.size):  # For loop that creates the grid system, first loop makes the row, second makes the columns
            self.grid.append([])
            for j in range(self.size):
                if i == 0 or i == 79:
                    self.grid[i].append(1)
                elif j == 0 or j == 79:
                    self.grid[i].append(1)
                else:
                    self.grid[i].append(0)
    def printGrid(self):
        for i in range(0,self.size):                     # These for loops PRINT the grid. We dont need it anymore but good for debug
            for j in range(0,self.size):
                print(self.grid[j][i],end=' ')
            print()
    def getGrid(self,pos):
        return self.grid[pos[0]][pos[1]]
    def updateGrid(self,coord,id):
        self.grid[coord[0]][coord[1]] = id
# ----------------------------------- PLAYER RELATED FUNCTIONS -------------------------------------------
    def updatePlayerX(self,x):
        self.coord[0] += x
        if self.checkMovementBounds(self.coord[0]):
            if self.checkBlock():
                return self.coord
        self.coord[0]-=x
        return self.coord

    def updatePlayerY(self,y):
        self.coord[1] += y
        if self.checkMovementBounds(self.coord[1]):
            if self.checkBlock():
                return self.coord

        self.coord[1] -= y
        return self.coord


    def checkMovementBounds(self,value):
        if value >= 80:
            return False
        if value < 0:
            return False
        return True

    def checkBlock(self):
        blockType = self.getGrid([self.coord[0],self.coord[1]])
        if blockType == 0:
            self.travel = True
            self.total -= 1
            self.current.append([self.coord[0],self.coord[1]])
            self.grid[self.coord[0]][self.coord[1]] = 3
            return True
        if blockType == 3:
            return False

        if blockType == 1:
            if self.travel:
                self.travel = False
                self.addLastVertex()
                self.endCircuit()
                self.addTotals()
                # print(self.current)
                # print(self.vertex)
                self.vertex = []
                self.current = []
            return True

        return False

    def endCircuit(self):
        for i in range(len(self.current)):
            self.grid[self.current[i][0]][self.current[i][1]] = 1
        # if len(self.vertex) <= 2:
        #     return
        for i in range(len(self.current)):
            if self.getGrid([self.current[i][0], self.current[i][1] + 1]) != 1:
                self.fill([self.current[i][0], self.current[i][1] + 1])
            if self.getGrid([self.current[i][0], self.current[i][1] - 1]) != 1:
                self.fill([self.current[i][0], self.current[i][1] - 1])
            if self.getGrid([self.current[i][0]+1, self.current[i][1]]) != 1:
                self.fill([self.current[i][0]+1, self.current[i][1]])
            if self.getGrid([self.current[i][0]-1, self.current[i][1]]) != 1:
                self.fill([self.current[i][0]-1, self.current[i][1]])
    def fill(self,pos):
        tempGrid = deepcopy(self.grid)

        queue = [[pos[0],pos[1]]]
        # print(queue)
        while len(queue) > 0:
            square = queue.pop()
            if self.getGrid(square) == 4:
                return False
            if tempGrid[square[0]][square[1]] == 0:
                queue.append([square[0]+1,square[1]])
                queue.append([square[0]-1,square[1]])
                queue.append([square[0],square[1]+1])
                queue.append([square[0],square[1]-1])
                tempGrid[square[0]][square[1]] = 2
        self.grid = deepcopy(tempGrid)
        # self.printGrid()
        return True