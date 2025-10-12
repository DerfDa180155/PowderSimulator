import pygame

import PowderSimulator


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

        self.pouderSimulator = PowderSimulator.PowderSimulator(10,10)

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


            self.drawBoard(100, 100, 100, 100)



            pygame.display.flip()
            self.clock.tick(60)

    def drawBoard(self, startX, startY, width, height):
        print(self.pouderSimulator.board)

        color = (255, 255, 255)


        for x in range(self.pouderSimulator.sizeX):
            for y in range(self.pouderSimulator.sizeY):
                pygame.draw.rect(self.screen, color, (startX + ((width+5)*x), startY + ((height+5)*y), width-5, height-5))




if __name__ == "__main__":
    main()
