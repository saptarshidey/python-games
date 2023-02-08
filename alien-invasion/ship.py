import pygame
#from alien_invasion import AlienInvasion

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.image = pygame.image.load("assets/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = game.screen.get_rect().midbottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
