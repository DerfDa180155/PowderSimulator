import random
import pygame
import Empty

class Water:
    def __init__(self):
        self.colorArray = [(30,144,255), (24,116,205), (65,105,255), (28,134,238), (0,178,238)]

        self.color = self.colorArray[random.randint(0, len(self.colorArray)-1)]

        self.weight = 1

    def next(self, board, newBoard, x, y):
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

            if board[y+1][x-1].__class__ == Empty.Empty and newBoard[y+1][x-1].__class__ == Empty.Empty and x-1 >= 0 and not moved:
                newBoard[y+1][x-1] = board[y][x]
                moved = True

            if board[y+1][x-1].weight < self.weight and newBoard[y+1][x-1].weight < self.weight and x-1 >= 0 and not moved:
                temp = newBoard[y+1][x-1]
                newBoard[y+1][x-1] = board[y][x]
                newBoard[y][x] = temp
                moved = True


            if x+1 < len(board[y]) and not moved:
                if board[y+1][x+1].__class__ == Empty.Empty and newBoard[y+1][x+1].__class__ == Empty.Empty:
                    newBoard[y+1][x+1] = board[y][x]
                    moved = True

                if board[y+1][x+1].weight < self.weight and newBoard[y+1][x+1].weight < self.weight and not moved:
                    temp = newBoard[y+1][x+1]
                    newBoard[y+1][x+1] = board[y][x]
                    newBoard[y][x] = temp
                    moved = True

        if board[y][x-1].__class__ == Empty.Empty and newBoard[y][x-1].__class__ == Empty.Empty and x-1 > 0 and not moved:
            newBoard[y][x-1] = board[y][x]
            moved = True

        if board[y][x-1].weight < self.weight and newBoard[y][x-1].weight < self.weight and x-1 > 0 and not moved:
            temp = newBoard[y][x-1]
            newBoard[y][x-1] = board[y][x]
            newBoard[y][x] = temp
            moved = True

        if x + 1 < len(board[y]) and not moved:
            if board[y][x+1].__class__ == Empty.Empty and newBoard[y][x+1].__class__ == Empty.Empty:
                newBoard[y][x+1] = board[y][x]
                moved = True

            if board[y][x+1].weight < self.weight and newBoard[y][x+1].weight < self.weight and not moved:
                temp = newBoard[y][x+1]
                newBoard[y][x+1] = board[y][x]
                newBoard[y][x] = temp
                moved = True

        if not moved:
            newBoard[y][x] = board[y][x]

        board[y][x] = Empty.Empty()

