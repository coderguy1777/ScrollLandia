import pygame

class GamePlayer(object):
    def __init(self):
        self.playerpos = 0
        self.playerCamx = 40
        self.playerCamy = 40
        self.death = False
        self.healthgain = 10
        self.healthloss = -10
        self.playerCamxchange = self.playerCamx - 40
        self.playerCamychange = self.playerCamy - 40

    def test(self):
        return self.name