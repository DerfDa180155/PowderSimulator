

class PowderSimulator:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = []

        self.running = False
        self.speed = 1

        self.currentElement = "0"

        self.generateEmpty()

    def reset(self):
        self.board = []
        self.generateEmpty()

    def placeElement(self, x, y):
        self.board[y-1][x-1] = self.currentElement

    def removeElement(self, x, y):
        self.board[y-1][x-1] = "0"

    def generateEmpty(self):
        self.board = []
        temp = []

        for y in range(self.sizeY):
            temp = []
            for x in range(self.sizeX):
                temp.append([0])

            self.board.append(temp)

    def generateNext(self):
        for y in self.board:
            for x in self.board[y]:
                pass
                #self.board[y][x]

            