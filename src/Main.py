import time

import pygame

import PowderSimulator
import Button
import Sand


class main:
    def __init__(self):
        pygame.init()
        pygame.display.init()

        pygame.display.gl_set_attribute(pygame.GL_ACCELERATED_VISUAL, 0)
        pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)

        self.windowWidth = 1500
        self.windowHeight = 1500

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE | pygame.GL_DOUBLEBUFFER)
        pygame.display.set_caption("Powder Simulator by David Derflinger")

        self.clock = pygame.time.Clock()
        self.running = True

        self.pouderSimulator = PowderSimulator.PowderSimulator(20,20)

        self.buttons = []
        self.buttons.append(Button.Button(self.screen, 100, 1430, 50, 50, (255,255,0), "start simulation", "Start"))
        self.buttons.append(Button.Button(self.screen, 200, 1430, 50, 50, (255,255,0), "stop simulation", "Stop"))
        self.buttons.append(Button.Button(self.screen, 300, 1430, 50, 50, (255,255,0), "step one", "Step one"))
        self.buttons.append(Button.Button(self.screen, 400, 1430, 50, 50, (255,255,0), "speed", "Speed"))
        self.buttons.append(Button.Button(self.screen, 500, 1430, 50, 50, (255,255,0), "clear", "Clear"))
        self.buttons.append(Button.Button(self.screen, 600, 1430, 50, 50, (255,255,0), "new board", "New Board"))
        self.buttons.append(Button.Button(self.screen, 700, 1430, 50, 50, (255,255,0), "new x", "X"))
        self.buttons.append(Button.Button(self.screen, 800, 1430, 50, 50, (255,255,0), "new y", "Y"))
        self.buttons.append(Button.Button(self.screen, 900, 1430, 50, 50, (255,238,140), "select1", "Sand"))
        self.buttons.append(Button.Button(self.screen, 1000, 1430, 50, 50, (30,144,255), "select2", "Water"))
        self.buttons.append(Button.Button(self.screen, 1100, 1430, 50, 50, (128, 128, 128), "select3", "Metal"))

        for button in self.buttons:
            if button.onClick == "select1":
                button.isSelected = True

        self.newX = self.pouderSimulator.sizeX
        self.newY = self.pouderSimulator.sizeY

        self.run()

    def run(self):
        oldMousePressed = pygame.mouse.get_pressed()
        while self.running:
            scrolledUp = False
            scrolledDown = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Quit the Game
                        self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    scrolledUp = (event.button == 4)
                    scrolledDown = (event.button == 5)

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

            mx, my = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            mousePressedUp = []
            mousePressedDown = []
            mouseHolding = []
            for i in range(len(mousePressed)):
                mousePressedUp.append(not mousePressed[i] and oldMousePressed[i])
                mousePressedDown.append(mousePressed[i] and not oldMousePressed[i])
                mouseHolding.append(mousePressed[i])

            oldMousePressed = mousePressed

            font = pygame.font.Font(pygame.font.get_default_font(), 50)

            text = font.render("Powder Simulator", True, (255, 255, 255))
            newRect = text.get_rect()
            newRect.centerx = self.windowWidth / 2
            newRect.y = 25
            self.screen.blit(text, newRect)


            boardStartX = 100
            boardStartY = 100
            boardWidth = 1300
            boardHeight = 1300
            boardGapSizeX = 100/self.pouderSimulator.sizeX
            boardGapSizeY = 100/self.pouderSimulator.sizeY

            self.drawBoard(boardStartX, boardStartY, boardWidth, boardHeight, boardGapSizeX, boardGapSizeY)
            x, y = self.boardClicked(mx, my, boardStartX, boardStartY, boardWidth, boardHeight)
            #print(str(x) + " " + str(y))

            if mouseHolding[0] and x > 0 and y > 0: # left click
                self.pouderSimulator.placeElement(x, y)
            elif mouseHolding[2] and x > 0 and y > 0: # right click
                self.pouderSimulator.removeElement(x, y)


            # auto generate
            if self.pouderSimulator.running:
                if (self.pouderSimulator.speed == self.pouderSimulator.speedCounter):
                    self.pouderSimulator.generateNext()
                    self.pouderSimulator.speedCounter = 0
                self.pouderSimulator.speedCounter += 1



            for button in self.buttons:
                button.hover(mx, my)
                button.clicked(mx, my, mousePressedUp)
                button.draw(self.windowWidth, self.windowHeight)

                if button.onClick in ["new x", "new y", "speed", "start simulation"]:
                    font = pygame.font.Font(pygame.font.get_default_font(), 20)
                    
                    if button.onClick == "new x":
                        text = font.render(str(self.pouderSimulator.sizeX), True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.centerx = button.x + button.width / 2
                        newRect.y = button.y - button.height / 2
                        self.screen.blit(text, newRect)
                        text = font.render(str(self.newX), True, (255, 255, 255))
                    elif button.onClick == "new y":
                        text = font.render(str(self.pouderSimulator.sizeY), True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.centerx = button.x + button.width / 2
                        newRect.y = button.y - button.height / 2
                        self.screen.blit(text, newRect)
                        text = font.render(str(self.newY), True, (255, 255, 255))
                    elif button.onClick == "speed":
                        text = font.render(str(self.pouderSimulator.speed), True, (255, 255, 255))
                    elif button.onClick == "start simulation":
                        text = font.render(str(self.pouderSimulator.running), True, (255, 255, 255))

                    newRect = text.get_rect()
                    newRect.centerx = button.x + button.width / 2
                    newRect.y = button.y + button.height
                    self.screen.blit(text, newRect)

                if button.isleftClicked:
                    print(button.onClick)
                    match button.onClick:
                        case "start simulation":
                            self.pouderSimulator.running = True
                        case "stop simulation":
                            self.pouderSimulator.running = False
                        case "step one":
                            self.pouderSimulator.generateNext()
                        case "clear":
                            self.pouderSimulator.reset()
                        case "new board":
                            if self.newX != self.pouderSimulator.sizeX or self.newY != self.pouderSimulator.sizeY:
                                self.pouderSimulator.reset((self.newX, self.newY))
                        case "select1":
                            self.pouderSimulator.currentElement = "Sand"
                            self.resetButtonSelection()
                            button.isSelected = True
                        case "select2":
                            self.pouderSimulator.currentElement = "Water"
                            self.resetButtonSelection()
                            button.isSelected = True
                        case "select3":
                            self.pouderSimulator.currentElement = "Metal"
                            self.resetButtonSelection()
                            button.isSelected = True

                if button.isHovered:
                    match button.onClick:
                        case "new x":
                            if scrolledUp:
                                self.newX += 5
                            elif scrolledDown:
                                self.newX -= 5
                                if self.newX < 5:
                                    self.newX = 5
                        case "new y":
                            if scrolledUp:
                                self.newY += 5
                            elif scrolledDown:
                                self.newY -= 5
                                if self.newY < 5:
                                    self.newY = 5
                        case "speed":
                            if scrolledUp:
                                self.pouderSimulator.speed += 1
                                self.pouderSimulator.speedCounter = 0
                            elif scrolledDown:
                                self.pouderSimulator.speed -= 1
                                if self.pouderSimulator.speed < 1:
                                    self.pouderSimulator.speed = 1
                                self.pouderSimulator.speedCounter = 0
            #print(self.pouderSimulator.board)

            pygame.display.flip()
            self.clock.tick(60)

    def resetButtonSelection(self):
        for tempButton in self.buttons:
            tempButton.isSelected = False

    def drawText(self, size, color, centerx, centery):
        font = pygame.font.Font(pygame.font.get_default_font(), size)
        text = font.render(str(self.pouderSimulator.sizeX), True, color)
        newRect = text.get_rect()
        newRect.centerx = centerx
        newRect.centery = centery
        self.screen.blit(text, newRect)

    def drawBoard(self, startX, startY, width, height, gapSizeX, gapSizeY):
        color = (255, 255, 255)

        for x in range(self.pouderSimulator.sizeX):
            for y in range(self.pouderSimulator.sizeY):
                color = self.pouderSimulator.board[y][x].color
                pygame.draw.rect(self.screen, color, (startX + ((width/self.pouderSimulator.sizeX)*x) + (gapSizeX/2), startY + ((height/self.pouderSimulator.sizeY)*y) + (gapSizeY/2), (width/self.pouderSimulator.sizeX)-(gapSizeX/2), (height/self.pouderSimulator.sizeY)-(gapSizeY/2)))

    def boardClicked(self, mx, my, startX, startY, width, height):
        endX = startX + width
        endY = startY + height

        x = 0
        y = 0

        widthBoard = width / self.pouderSimulator.sizeX
        heightBoard = height / self.pouderSimulator.sizeY

        if startX <= mx and mx <= endX and startY <= my and my <= endY:
            while mx > startX + widthBoard * x:
                x += 1

            while my > startY + heightBoard * y:
                y += 1

        return x, y


if __name__ == "__main__":
    main()
