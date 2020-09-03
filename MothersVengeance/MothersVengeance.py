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



		
	if keys[pygame.K_LEFT] and man.x >= man.vel:
		#man.x -= man.vel
		man.vel = -5
		man.left = True
		man.right = False
		man.standing = False
	elif keys[pygame.K_RIGHT] and man.x < canvas_width - man.width:
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
		if man.gravity in [0, 1]:
			man.isSquish = True
			man.vel = 0
		else:
			man.isSquish = False
	else:
		man.isSquish = False

	if keys[pygame.K_SPACE]:
		if man.jumpCount == 0:
			if man.isSquish:
				man.gravity = -25
			else:
				man.gravity = -15
			print(man.isSquish)
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
	print
	print("jumpCount: %s, gravity: %s" % (man.jumpCount, man.gravity))
	redrawGameWindow()
pygame.quit()