import pygame
import sys
from api.api import *

while run:
	clock.tick(27)	#for setting FPS to 27
	#pygame.time.delay(27)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for bullet in bullets:

		if bullet.x < canvas_width and bullet.x > 0:
			bullet.x += bullet.vel
		else:
			bullets.pop(bullets.index(bullet))
	keys = pygame.key.get_pressed()

	#logic for bullet creation and direction
	if keys[pygame.K_SPACE]:
		if man.left:
			facing = -1
		else:
			facing = 1
		if len(bullets) < 5:
			bullets.append(generate_projectile(facing))

	if keys[pygame.K_LEFT] and man.x >= man.vel:
		man.x -= man.vel
		man.left = True
		man.right = False
		man.standing = False
	elif keys[pygame.K_RIGHT] and man.x < canvas_width - man.width:
		man.x += man.vel
		man.left = False
		man.right = True
		man.standing = False
	else:
		man.standing = True
		man.walkCount = 0

	if not(man.isJump):
		if keys[pygame.K_UP]:
			man.isJump = True
			man.left = False
			man.right = False
			man.walkCount = 0
	else:
		if man.jumpCount >= -10:
			neg = 1
			if man.jumpCount < 0:
				neg = -1
			man.y -= int((man.jumpCount ** 2) * .5) * neg
			man.jumpCount -= 1
		else:
			man.isJump = False
			man.jumpCount = 10

	redrawGameWindow()
pygame.quit()