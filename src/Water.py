import random
import pygame
import Empty

class Water:
    def __init__(self):
        self.colorArray = [(0,0,255)]

        self.color = self.colorArray[random.randint(0, len(self.colorArray)-1)]

        self.weight = 1

    def next(self, board, newBoard, x, y):
        if y > len(board) or y < 0 or x > len(board[y]) or x < 0:
            return

        moved = False

        if y+1 < len(board):
            if board[y+1][x] == 0 and newBoard[y+1][x] == 0:
                newBoard[y+1][x] = board[y][x]
                moved = True

            if board[y+1][x-1] == 0 and newBoard[y+1][x-1] == 0 and x-1 >= 0 and not moved:
                newBoard[y+1][x-1] = board[y][x]
                moved = True

            if x + 1 < len(board[y]) and not moved:
                if board[y+1][x+1] == 0 and newBoard[y+1][x+1] == 0:
                    newBoard[y+1][x+1] = board[y][x]
                    moved = True

        if board[y][x-1] == 0 and newBoard[y][x-1] == 0 and x-1 > 0 and not moved:
            newBoard[y][x-1] = board[y][x]
            moved = True

        if x + 1 < len(board[y]) and not moved:
            if board[y][x+1] == 0 and newBoard[y][x+1] == 0:
                newBoard[y][x+1] = board[y][x]
                moved = True

        if not moved:
            newBoard[y][x] = board[y][x]

        board[y][x] = Empty.Empty()

