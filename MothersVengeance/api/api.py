import pygame
import sys
sys.path.append('classes')
import player, enemy, projectile, healthBar, ammoui

#globals for the project
canvas_width = 800
canvas_height = 800

bg = pygame.image.load('./imgs/bg.jpg')

clock = pygame.time.Clock()
 
pygame.mixer.init()
pygame.mixer.music.load("./sounds/music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


pygame.init()
win = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("MothersVengeance")

run = True
font = pygame.font.SysFont('comicsans', 30, True)
man = player.Player(50, 300, 64, 64)

score = 0

def redrawGameWindow():
	win.blit(bg, (0 ,0))
	man.draw(win)

	# UI on the top layer

	pygame.display.update()

