import pygame
import sys
sys.path.append('classes')
import player, enemy, projectile
#globals for the project
canvas_width = 400
canvas_height = 400

bg = pygame.image.load('./imgs/bg.jpg')
char = pygame.image.load('./imgs/standing.png')

clock = pygame.time.Clock()

pygame.init()
win = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("MothersVengeance")

run = True
man = player.Player(50, 300, 64, 64)
goblin = enemy.Enemy(30, 300, 64, 64, 200)
bullets = []

def redrawGameWindow():
	win.blit(bg, (0 ,0))
	man.draw(win)
	goblin.draw(win)
	#actually drawing the bullets from bullet spamming
	for bullet in bullets:
		bullet.draw(win)
	pygame.display.update()

def generate_projectile(facing):
	return projectile.Projectile(round(man.x + man.width//2), round(man.y+ man.height//2), 6, (0, 0, 0), facing)



