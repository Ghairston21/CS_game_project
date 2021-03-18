import pygame
from game_object import GameObject

class Mark(GameObject):
    def __init__(self, x, y, w, h, player, r, pos):
        GameObject.__init__(self, x, y, w, h)
        self.radius = r
        self.player = player
        self.position = pos



    def draw(self, surface):
        if self.player == -1:
            pygame.draw.circle(surface,(0,255,255), self.center,self.radius)
        if self.player == 1:
            pygame.draw.circle(surface,(255,100,0),self.center,self.radius)









