

class PowderSimulator:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = []

        self.generateEmpty()

    def reset(self):
        self.board = []
        self.generateEmpty()

    def placeElement(self, x, y, type):
        self.board[y-1][x-1] = type

    def generateEmpty(self):
        self.board = []
        temp = []

        for y in range(self.sizeY):
            temp = []
            for x in range(self.sizeX):
                temp.append([0])

            self.board.append(temp)

    def generateNext(self):
        pass