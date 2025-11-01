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

        self.isHovered = False
        self.isleftClicked = False
        self.isrightClicked = False

    def draw(self, windowWidth, windowHeight):
        if self.isHovered:
            newColor = (self.color[0]/2 ,self.color[1]/2, self.color[2]/2)
            pygame.draw.rect(self.screen, newColor, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def clicked(self, mx, my, mouseClick):
        if self.hover(mx, my) and mouseClick[0]:
            self.isleftClicked = True
        elif self.hover(mx, my) and mouseClick[2]:
            self.isrightClicked = True
        else:
            self.isleftClicked = False
            self.isrightClicked = False
        return self.isleftClicked, self.isrightClicked

    def hover(self, mx, my):
        temp = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered

