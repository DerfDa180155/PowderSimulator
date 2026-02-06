import random
import pygame
import Empty

class Stone:
    def __init__(self):
        self.colorArray = [(112,128,144), (119,136,153), (115,123,139), (108,123,139), (118,130,154)]

        self.color = self.colorArray[random.randint(0, len(self.colorArray)-1)]

        self.weight = 10

    def next(self, board, newBoard, x, y):
        newBoard[y][x] = board[y][x]
