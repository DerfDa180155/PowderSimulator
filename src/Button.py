import pygame

class Button:
    def __init__(self, screen, x, y, width, height, color, onClick, displayText="", textSize = 20, textColor=(0, 0, 0)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.onClick = onClick
        self.displayText = displayText
        self.textSize = textSize
        self.textColor = textColor

        self.isSelected = False

        self.isHovered = False
        self.isleftClicked = False
        self.isrightClicked = False

    def draw(self, windowWidth, windowHeight):
        if self.isSelected:
            pygame.draw.rect(self.screen, (0,255,128), (self.x-5, self.y-5, self.width+10, self.height+10))
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        if self.isHovered:
            newColor = (self.color[0]/2 ,self.color[1]/2, self.color[2]/2)
            pygame.draw.rect(self.screen, newColor, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

        if self.displayText != "":
            font = pygame.font.Font(pygame.font.get_default_font(), self.textSize)
            text = font.render(self.displayText, True, self.textColor)
            newRect = text.get_rect()
            newRect.centerx = self.x + self.width / 2
            newRect.centery = self.y + self.height / 2
            self.screen.blit(text, newRect)

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

