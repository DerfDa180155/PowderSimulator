import random
import pygame
import Empty

class Stone:
    def __init__(self):
        self.colorArray = [(112,128,144), (119,136,153), (115,123,139), (108,123,139), (118,130,154)]

        self.color = self.colorArray[random.randint(0, len(self.colorArray)-1)]

        self.weight = 10

    def next(self, board, newBoard, x, y, border):
        if y > len(board) or y < 0 or x > len(board[y]) or x < 0:
            return

        moved = False

        if y < len(board)-1:
            if board[y+1][x].__class__ == Empty.Empty and newBoard[y+1][x].__class__ == Empty.Empty:
                newBoard[y+1][x] = board[y][x]
                moved = True

            if board[y+1][x].weight < self.weight and newBoard[y+1][x].weight < self.weight and not moved:
                temp = newBoard[y+1][x]
                newBoard[y+1][x] = board[y][x]
                newBoard[y][x] = temp
                moved = True

        if not moved:
            newBoard[y][x] = board[y][x]

        board[y][x] = Empty.Empty()
