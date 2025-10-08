

class PowderSimulator:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = []

        self.generateEmpty()

    def reset(self):
        self.board = []
        self.generateEmpty()

    def generateEmpty(self):
        self.board = []
        temp = []

        for x in range(self.sizeX):
            temp.append([])

        for y in range(self.sizeY):
            self.board.append(temp)

    def generateNext(self):
        pass