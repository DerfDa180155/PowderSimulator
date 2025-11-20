import random

import pygame

class Sand:
    def __init__(self):
        self.colorArray = [(255,238,140), (228,217,111), (251,236,93), (240,220,130), (236,213,64)]

        self.color = self.colorArray[random.randint(0, len(self.colorArray)-1)]

    def next(self, board, x, y):
        if y > len(board) or y < 0 or x > len(board[y]) or x < 0:
            return

        if y < len(board) -1:
            if board[y-1][x] == 0:
                temp = board[y-1][x]
                board[y-1][x] = board[y][x]
                board[y][x] = temp
            elif board[y-1][x-1] == 0:
                temp = board[y-1][x-1]
                board[y-1][x-1] = board[y][x]
                board[y][x] = temp
            elif board[y-1][x+1] == 0:
                temp = board[y-1][x+1]
                board[y-1][x+1] = board[y][x]
                board[y][x] = temp
