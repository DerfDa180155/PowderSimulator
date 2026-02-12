import Empty
import Sand
import Water
import Metal
import Stone
import xml.etree.cElementTree as ET

class PowderSimulator:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = self.generateEmpty()

        self.running = False
        self.speed = 10
        self.speedCounter = 0

        self.border = False

        self.currentElement = "Sand"
        self.path = "savedBoard/"

    def reset(self, newSize=None):
        if newSize is not None:
            self.sizeX = newSize[0]
            self.sizeY = newSize[1]
        self.board = self.generateEmpty()

    def placeElement(self, x, y):
        if self.board[y-1][x-1].__class__ != Empty.Empty:
            return
        match self.currentElement:
            case "Sand":
                self.board[y-1][x-1] = Sand.Sand()
            case "Water":
                self.board[y-1][x-1] = Water.Water()
            case "Metal":
                self.board[y-1][x-1] = Metal.Metal()
            case "Stone":
                self.board[y-1][x-1] = Stone.Stone()

    def removeElement(self, x, y):
        self.board[y-1][x-1] = Empty.Empty()

    def generateEmpty(self):
        board = []
        temp = []

        for y in range(self.sizeY):
            temp = []
            for x in range(self.sizeX):
                temp.append(Empty.Empty())

            board.append(temp)
        return board

    def generateNext(self):
        newBoard = self.generateEmpty()
        for y in range(len(self.board)-1,-1,-1):
            for x in range(len(self.board[y])-1,-1,-1):
                if self.board[y][x].__class__ != Empty.Empty:
                    self.board[y][x].next(self.board, newBoard, x, y)

        self.board = newBoard

    def save(self, name = "board"):
        root = ET.Element("powderSimulator")

        ET.SubElement(root, "sizeX").text = str(self.sizeX)
        ET.SubElement(root, "sizeY").text = str(self.sizeY)
        board = ET.SubElement(root, "board", type="array")
        for i in self.board:
            x = ET.SubElement(board, "x")
            for j in i:
                y = ET.SubElement(x, "y").text = str(j.__class__)

        ET.ElementTree(root).write(self.path + name + ".xml")

    def load(self, name = "board"):
        root = ET.parse(self.path + name + ".xml").getroot()
        self.sizeX = int(root[0].text)
        self.sizeY = int(root[1].text)
        self.board = self.generateEmpty()

        for i in range(0, self.sizeX):
            for j in range(0, self.sizeY):
                match root[2][i][j].text:
                    case "<class 'Sand.Sand'>":
                        self.board[i][j] = Sand.Sand()
                    case "<class 'Water.Water'>":
                        self.board[i][j] = Water.Water()
                    case "<class 'Metal.Metal'>":
                        self.board[i][j] = Metal.Metal()
                    case "<class 'Stone.Stone'>":
                        self.board[i][j] = Stone.Stone()
                    case "<class 'Empty.Empty'>":
                        pass
