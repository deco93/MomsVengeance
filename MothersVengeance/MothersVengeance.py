import pygame
import sys
from api.api import *

#pygame.mixer.init()
#pygame.mixer.music.load("./sounds/music.mp3")

#pygame.mixer.music.play(-1)
#main loop
while run:
	clock.tick(27)	#for setting FPS to 27
	#pygame.time.delay(27)
	if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1] and goblin.visible:
		if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
			man.hit(win, canvas_width, canvas_height)
			if score >= 5:
				score -= 5
				goblin.health += 5
			else:
				score = 0
				goblin.health = 10

	if spaceSpamCount > 0:
		spaceSpamCount += 1
	if spaceSpamCount > 3:
		spaceSpamCount = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for bullet in bullets:
		if goblin.visible:
			#if the bullets upper edge/y-coordinate is above the goblin's hitbox lower edge && 
			# bullet's lower edge/y-coordinate is below the goblin's hitbox upper edge 
			if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
				if bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2] and bullet.x + bullet.radius > goblin.hitbox[0]:
					score = goblin.hit(score)
					#score += 1	
					bullets.pop(bullets.index(bullet))


		if bullet.x < canvas_width and bullet.x > 0:
			bullet.x += bullet.vel
		else:
			bullets.pop(bullets.index(bullet))
	keys = pygame.key.get_pressed()

	#logic for bullet creation and direction
	if keys[pygame.K_SPACE] and spaceSpamCount == 0:
		if man.left:
			facing = -1
		else:
			facing = 1

		if man.ammo > 0 and len(bullets) < 5:
			man.ammo -= 1
			bullets.append(generate_projectile(facing))
		pygame.mixer.Channel(0).play(pygame.mixer.Sound('./sounds/bullet.wav'))
		spaceSpamCount =1
		
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

	redrawGameWindow(score)
pygame.quit()