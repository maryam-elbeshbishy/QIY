import random
class Block():
    def __init__(self):
        self.white = 1
        self.black = 0
        self.grey = 2
        self.orange = 3
        self.claimed = (128,128,128)
    def getOrange(self):
        return self.orange
    def getOrangeColor(self):
        return (255,165,0)
    def getWhite(self):
        return self.white

    def getBlack(self):
        return self.black

    def getGrey(self):
        return self.grey

    def getWhiteColor(self):
        return (255, 255, 255)

    def getBlackColor(self):
        return (0, 0, 0)

    def getGreyColor(self):
        return self.claimed
    def changeClaimed(self):
        red = random.randint(30,230)
        green = random.randint(30,230)
        blue = random.randint(30,230)
        self.claimed = (red,green,blue)
