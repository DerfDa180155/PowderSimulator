import random

import pygame

class Metal:
    def __init__(self):
        self.color = (125,125,125)
        self.weight = 99

    def next(self, board, newBoard, x, y):
        newBoard[y][x] = board[y][x]
