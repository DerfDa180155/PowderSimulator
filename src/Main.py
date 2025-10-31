import pygame

import PowderSimulator
import Button


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
        self.buttons.append(Button.Button(self.screen, 100, 1430, 50, 50, (255,255,0), "start simulation"))
        self.buttons.append(Button.Button(self.screen, 200, 1430, 50, 50, (255,255,0), "stop simulation"))
        self.buttons.append(Button.Button(self.screen, 300, 1430, 50, 50, (255,255,0), "speed"))
        self.buttons.append(Button.Button(self.screen, 400, 1430, 50, 50, (255,255,0), "clear"))

        self.run()

    def run(self):
        oldMousePressed = pygame.mouse.get_pressed()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Quit the Game
                        self.running = False

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

            mx, my = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            mousePressedUp = []
            mousePressedDown = []
            for i in range(len(mousePressed)):
                mousePressedUp.append(not mousePressed[i] and oldMousePressed[i])
                mousePressedDown.append(mousePressed[i] and not oldMousePressed[i])

            oldMousePressed = mousePressed


            boardStartX = 100
            boardStartY = 100
            boardWidth = 1300
            boardHeight = 1300
            boardGapSize = 10

            self.drawBoard(boardStartX, boardStartY, boardWidth, boardHeight, boardGapSize)
            x, y = self.boardClicked(mx, my, boardStartX, boardStartY, boardWidth, boardHeight)
            #print(str(x) + " " + str(y))

            if mousePressedUp[0] and x > 0 and y > 0: # left click
                self.pouderSimulator.placeElement(x, y, "1")
            elif mousePressedUp[2] and x > 0 and y > 0: # right click
                self.pouderSimulator.placeElement(x, y, "0")


            for button in self.buttons:
                button.hover(mx, my)
                button.clicked(mx, my, mousePressedUp)
                button.draw(self.windowWidth, self.windowHeight)

                if button.isleftClicked:
                    print(button.onClick)


            pygame.display.flip()
            self.clock.tick(60)

    def drawBoard(self, startX, startY, width, height, gapSize):
        color = (255, 255, 255)

        for x in range(self.pouderSimulator.sizeX):
            for y in range(self.pouderSimulator.sizeY):
                if self.pouderSimulator.board[y][x] == "1":
                    color = (0, 0, 0)
                else:
                    color = (255, 255, 255)
                pygame.draw.rect(self.screen, color, (startX + ((width/self.pouderSimulator.sizeX)*x) + (gapSize/2), startY + ((height/self.pouderSimulator.sizeY)*y) + (gapSize/2), (width/self.pouderSimulator.sizeX)-(gapSize/2), (height/self.pouderSimulator.sizeY)-(gapSize/2)))

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
