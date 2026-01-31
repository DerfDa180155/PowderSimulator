import Empty
import Sand
import Water
import Metal
import xml.etree.cElementTree as ET

class PowderSimulator:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = self.generateEmpty()

        self.running = False
        self.speed = 10
        self.speedCounter = 0

        self.currentElement = "Sand"

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

    def save(self):
        path = "savedBoard/"

        root = ET.Element("powderSimulator")

        ET.SubElement(root, "sizeX").text = str(self.sizeX)
        ET.SubElement(root, "sizeY").text = str(self.sizeY)
        board = ET.SubElement(root, "board", type="array")
        for i in self.board:
            x = ET.SubElement(board, "x")
            for j in i:
                y = ET.SubElement(x, "y").text = j.__class__

        ET.ElementTree(root).write(path + "board.xml")

    def load(self):
        self.board = self.generateEmpty()
            