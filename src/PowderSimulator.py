import Sand

class PowderSimulator:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = self.generateEmpty()

        self.running = False
        self.speed = 1

        self.currentElement = Sand.Sand()

    def reset(self):
        self.board = self.generateEmpty()

    def placeElement(self, x, y):
        self.board[y-1][x-1] = self.currentElement.createNewObject()

    def removeElement(self, x, y):
        self.board[y-1][x-1] = 0

    def generateEmpty(self):
        board = []
        temp = []

        for y in range(self.sizeY):
            temp = []
            for x in range(self.sizeX):
                temp.append(0)

            board.append(temp)
        return board

    def generateNext(self):
        newBoard = self.generateEmpty()
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                pass
                #self.board[y][x]

            