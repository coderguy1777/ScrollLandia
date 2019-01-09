import random
import sys
import pygame


class Inventory:
    def __init__(self):
        self.sword = str("Sword")
        self.backpack = "Backpack"
        self.item1 = "Pan"
        self.item2 = "Food Maker"
        self.itemlist = []

    def invlist(self):
        self.itemlist.append(self.sword)