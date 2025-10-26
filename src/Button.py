import pygame

class Button:
    def __init__(self, screen, x, y, width, height, color, onClick):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.onClick = onClick

    def draw(self, windowWidth, windowHeight):
        pass

    def clicked(self, mx, my, mouseClick):
        pass

    def hover(self, mx, my):
        pass

