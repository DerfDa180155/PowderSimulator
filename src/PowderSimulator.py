import Sand

class PowderSimulator:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = self.generateEmpty()

        self.running = False
        self.speed = 10
        self.speedCounter = 0

        self.currentElement = "Sand"

    def reset(self):
        self.board = self.generateEmpty()

    def placeElement(self, x, y):
        match self.currentElement:
            case "Sand":
                self.board[y-1][x-1] = Sand.Sand()

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
        for y in range(len(self.board)-1,-1,-1):
            for x in range(len(self.board[y])-1,-1,-1):
                if self.board[y][x] != 0:
                    self.board[y][x].next(self.board, newBoard, x, y)

        self.board = newBoard

            