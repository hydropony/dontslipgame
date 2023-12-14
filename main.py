# Complete your game here
import pygame, random

class CoinRush():
    def __init__(self):
        pygame.init()

        self.window_height = 480
        self.window_width = 640

        self.loadImages()
        self.newGame()

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Don't slip!")
        self.game_font = pygame.font.SysFont("Bold", 50)

        self.clock = pygame.time.Clock()

        self.mainLoop()

    def loadImages(self):
        self.robot = pygame.image.load("robot.png")
        self.robotWidth = self.robot.get_width()
        self.robotHeight = self.robot.get_height()
        self.coin = pygame.image.load("coin.png")
        self.coinWidth = self.coin.get_width()
        self.coinHeight = self.coin.get_height()
    
    def newGame(self):
        self.robotx = self.window_width / 2 - self.robotWidth / 2
        self.roboty = self.window_height / 2 - self.robotHeight / 2
        self.robotxVel = 0
        self.robotyVel = 0
        self.score = 0
        self.coinx = random.randint(0, self.window_width - self.coinWidth)
        self.coiny = random.randint(0, self.window_height - self.coinHeight)

    
    def checkEvents(self):
        if self.checkDead():
            self.robotxVel = 0
            self.robotyVel = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return self.newGame()
        else:
            to_right = False
            to_left = False
            to_up = False
            to_down = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        to_left = True
                    if event.key == pygame.K_RIGHT:
                        to_right = True
                    if event.key == pygame.K_UP:
                        to_up = True
                    if event.key == pygame.K_DOWN:
                        to_down = True
                    if event.key == pygame.K_r:
                        return self.newGame()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        to_left = False
                    if event.key == pygame.K_RIGHT:
                        to_right = False
                    if event.key == pygame.K_UP:
                        to_up = False
                    if event.key == pygame.K_DOWN:
                        to_down = False

                if to_right:
                    self.robotxVel += 1
                if to_left:
                    self.robotxVel -= 1
                if to_up:
                    self.robotyVel -= 1
                if to_down:
                    self.robotyVel += 1

            self.robotx += self.robotxVel
            self.roboty += self.robotyVel

    def randomizeCoin(self):
        self.coinx = random.randint(0, self.window_width - self.coinWidth)
        self.coiny = random.randint(0, self.window_height - self.coinHeight)

    def isCoinAcquired(self) -> bool:
        if self.coinx + self.coinWidth > self.robotx and self.coinx < self.robotx + self.robotWidth:
            if self.coiny + self.coinHeight > self.roboty and self.coiny < self.roboty + self.robotHeight:
                self.score += 1
                return True
        return False
    
    def drawWindow(self):
        self.window.fill((0,0,0))

        self.window.blit(self.robot, (self.robotx, self.roboty))
        self.window.blit(self.coin, (self.coinx, self.coiny))
        text = self.game_font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(text, (0,0))
        if self.checkDead():            
            text = self.game_font.render("GAME OVER!", True, (255, 0, 0))
            self.window.blit(text, (self.window_width / 2 - 100, self.window_height / 2 - 25))
            text = self.game_font.render("PRESS R!", True, (255, 0, 0))
            self.window.blit(text, (self.window_width / 2 - 100, self.window_height / 2 + 50))

        pygame.display.flip()
        self.clock.tick(60 + self.score)
    
    def checkDead(self) -> bool:
        if self.robotx < 0 or self.robotx > self.window_width - self.robotWidth:
            return True
        if self.roboty < 0 or self.roboty > self.window_height - self.robotHeight:
            return True
        else:
            return False

    def mainLoop(self):
        while True:
            self.checkEvents()
            self.drawWindow()
            if self.isCoinAcquired():
                self.randomizeCoin()


CoinRush()
