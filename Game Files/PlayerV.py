import pygame

class DisplayVals(pygame.display):
    def __init(self):
        self.playerpos = 0
        self.playerCamx = 40
        self.playerCamy = 40
        self.death = False
        self.healthgain = 10
        self.healthloss = -10
        self.playerCamxchange = self.playerCamx - 40
        self.playerCamychange = self.playerCamy - 40
        self.screen = pygame.display.get_active()

    def playermovement(self):
        x = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))