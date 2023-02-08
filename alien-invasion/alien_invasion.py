import sys
import pygame

from config import Config
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.bgcolor = Config.BACKGROUND_COLOR
        self.ship = Ship(self)

    def run(self):
        while self.running:
            # process input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # drawing logic
            self.screen.fill(self.bgcolor)
            self.ship.draw()

            # refresh display
            pygame.display.update()
            self.clock.tick(Config.FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = AlienInvasion()
    game.run()
