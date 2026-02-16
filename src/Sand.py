import random
import pygame
import Empty

class Sand:
    def __init__(self):
        self.colorArray = [(255,238,140), (228,217,111), (251,236,93), (240,220,130), (236,213,64)]

        self.color = self.colorArray[random.randint(0, len(self.colorArray)-1)]

        self.weight = 2

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

            if board[y+1][x-1].__class__ == Empty.Empty and newBoard[y+1][x-1].__class__ == Empty.Empty and x-1 >= 0 and not moved:
                newBoard[y+1][x-1] = board[y][x]
                moved = True

            if board[y+1][x-1].weight < self.weight and newBoard[y+1][x-1].weight < self.weight and x-1 >= 0 and not moved:
                temp = newBoard[y+1][x-1]
                newBoard[y+1][x-1] = board[y][x]
                newBoard[y][x] = temp
                moved = True

            if border:
                if x-1 < 0:
                    if board[y+1][len(board[0])-1].__class__ == Empty.Empty and newBoard[y+1][len(newBoard[0])-1].__class__ == Empty.Empty and not moved:
                        newBoard[y+1][len(board[0])-1] = board[y][x]
                        moved = True

                    if board[y+1][len(board[0])-1].weight < self.weight and newBoard[y+1][len(newBoard[0])-1].weight < self.weight and not moved:
                        temp = newBoard[y+1][len(board[0])-1]
                        newBoard[y+1][len(board[0])-1] = board[y][x]
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
            elif border:
                if board[y+1][0].__class__ == Empty.Empty and newBoard[y+1][0].__class__ == Empty.Empty and not moved:
                    newBoard[y+1][0] = board[y][x]
                    moved = True

                if board[y+1][0].weight < self.weight and newBoard[y+1][0].weight < self.weight and not moved:
                    temp = newBoard[y+1][0]
                    newBoard[y+1][0] = board[y][x]
                    newBoard[y][x] = temp
                    moved = True

        if not moved:
            newBoard[y][x] = board[y][x]

        board[y][x] = Empty.Empty()

