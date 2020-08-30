import pygame
import math

class HealthBar(object):


    def __init__(self, player, radius, line_width, x, y):
        self.location = [x, y]
        self.player = player
        self.radius = radius
        self.line_width = line_width
        self.fill_color = pygame.Color(207,0,112)
        self.edge_color = pygame.Color(255,255,255)
        

    def draw(self, win):
  
        # fill 
        pygame.draw.circle(win, self.fill_color, self.location, math.ceil(self.radius * self.player.current_health / self.player.max_health), 0)
        # line
        pygame.draw.circle(win, self.edge_color, self.location, self.radius, self.line_width)




