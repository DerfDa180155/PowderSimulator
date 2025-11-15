import random

import pygame

class Sand:
    def __init__(self):
        self.colorArray = [(255,238,140), (228,217,111), (251,236,93), (240,220,130), (236,213,64)]

        self.color = self.colorArray[random.randint(0, len(self.colorArray)-1)]

    def createNewObject(self):
        return Sand()


    def next(self, board, x, y):
        pass
