import random

import pygame

class Metal:
    def __init__(self):
        self.colorArray = [(128,128,128), (105,105,105), (120,120,125), (112,128,130), (90,95,95)]

        self.color = self.colorArray[random.randint(0, len(self.colorArray) - 1)]

        self.weight = 100

    def next(self, board, newBoard, x, y):
        newBoard[y][x] = board[y][x]
