import random
import pygame
import Empty

class Lava:
    def __init__(self):
        self.colorArray = [(255,144,0)]

        self.color = self.colorArray[random.randint(0, len(self.colorArray)-1)]

        self.weight = 1

    def next(self, board, newBoard, x, y, border):
        newBoard[y][x] = board[y][x]
