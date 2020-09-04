import pygame
import sys
from api.api import *

#pygame.mixer.init()
#pygame.mixer.music.load("./sounds/music.mp3")

#pygame.mixer.music.play(-1)
air_time = 0
jump_delta = -15 
#main loop

while run:
	clock.tick(30)	#for setting FPS to 30

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()



		
	if keys[pygame.K_LEFT] and man.x >= man.vel and not man.isDash:
		#man.x -= man.vel
		man.vel = -5
		man.left = True
		man.right = False
		man.standing = False
	elif keys[pygame.K_RIGHT] and man.x < canvas_width - man.width and not man.isDash:
		#man.x += man.vel
		man.vel = 5
		man.left = False
		man.right = True
		man.standing = False
	else:
		man.standing = True
		man.walkCount = 0
		man.vel = 0
#if not(man.isJump):

	if keys[pygame.K_DOWN]:
		if man.gravity in [0, 1] and man.isDash == False:
			man.isSquish = True
			man.vel = 0
		else:
			man.isSquish = False
	else:
		man.isSquish = False

	if keys[pygame.K_SPACE]:
		if man.jumpCount == 0 and man.isDash == False:
			if man.isSquish:
				man.gravity = -15 * man.currentSquishFrame
			else:
				man.gravity = -15

	# key UP for long jump in the air.
	if keys[pygame.K_UP]:
		# in_air and dropping
		if man.jumpCount > 2 and man.gravity > 0 and not man.isDash:
			man.isBubbled = True
		else:
			man.isBubbled = False
	else:
		man.isBubbled = False
	# print(man.isBubbled)

	# key x, c for left, right dash
	if keys[pygame.K_x]:
		if man.dashCount == 0:
			man.left = True
			man.right = False
			man.isDash = True
			man.dashCount = player.DASH_COOL_DOWN


	if keys[pygame.K_c]:
		if man.dashCount == 0:
			man.right = True
			man.left = False
			man.isDash = True
			man.dashCount = player.DASH_COOL_DOWN

	# calc vel
	if man.isDash:
		man.standing = False
		if man.left and man.x >= man.vel:
			man.vel = -player.DASH_DELTA_X
		elif man.right and man.x < canvas_width - man.width:
			man.vel = player.DASH_DELTA_X
		else:
			man.vel = 0
	print('dashcount: %s, isDash %s, vel: %s' %(man.dashCount, man.isDash, man.vel))
			# print(man.isSquish)
		#man.isJump = True
		#man.left = False
		#man.right = False
		#man.walkCount = 0
	
	# else:
	# 	if man.jumpCount >= 0:
	#
	# 		man.gravity = -10
	# 		man.jumpCount -= 1
	# 	else:
	# 		man.isJump = False
	# 		man.jumpCount = 2

	# Gravity

	redrawGameWindow()
	
pygame.quit()