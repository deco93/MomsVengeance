import pygame
import sys
sys.path.append('classes')
import player, enemy, projectile, healthBar, ammoui

#globals for the project
canvas_width = 400
canvas_height = 400

bg = pygame.image.load('./imgs/bg.jpg')
char = pygame.image.load('./imgs/standing.png')

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
goblin = enemy.Enemy(120, 300, 64, 64, 200)
bullets = []
spaceSpamCount = 0
hp_bar = healthBar.HealthBar(man, 32, 2, 32, canvas_height - 32)
ammo_ui = ammoui.AmmoUI(man, 12, canvas_width - 100, canvas_height - 32)

score = 0

def redrawGameWindow(score):
	win.blit(bg, (0 ,0))
	text = font.render('Score: '+ str(score), 1, (0, 0, 0))
	win.blit(text, (275, 10))
	man.draw(win)
	goblin.draw(win)
	#actually drawing the bullets from bullet spamming
	for bullet in bullets:
		bullet.draw(win)

	# UI on the top layer
	hp_bar.draw(win)
	ammo_ui.draw(win)
	pygame.display.update()


def generate_projectile(facing):
	return projectile.Projectile(round(man.x + man.width//2), round(man.y+ man.height//2), 6, (0, 0, 0), facing)