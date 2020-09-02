import pygame
import pygame.freetype as ft
class AmmoUI(object):
    
    def __init__(self, player, size, x, y):
        self.player = player
        self.size = size
        self.location = [x, y]
        self.font = ft.Font('./fonts/ShortBaby-Mg2w.ttf', size)
        self.fg_color = pygame.color.Color(255,255,255)
        self.bg_color = pygame.color.Color(0,0,0, a=255)
    
    def draw(self, win):
        self.font.render_to(surf = win, dest = tuple(self.location), text = 'Putty Ammo: {}'.format(self.player.ammo), fgcolor = self.fg_color, bgcolor = self.bg_color, size = self.size)

        


