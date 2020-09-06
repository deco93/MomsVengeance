import pygame
import sys
from api.api import *

#pygame.mixer.init()
#pygame.mixer.music.load("./sounds/music.mp3")

#pygame.mixer.music.play(-1)
air_time = 0
jump_delta = -15

win = pygame.display.set_mode((canvas_width, canvas_height), 1, 32)

## Game States 0 For Starting Menu, 1 For Running Game, 2 For Game Lose Menu
gameStates = 0

selectedGameMenus = 0

def DrawText(text, font, color, surface, x, y):
	textObj = font.render(text, 1, color)
	textRect = textObj.get_rect()
	textRect.topleft = (x, y)
	win.blit(textObj, textRect)



#main loop
while run:

	clock.tick(30)	#for setting FPS to 30
	######################### Menu Code ########################
	while(gameStates == 0):
		win.blit(Sky)
		DrawText("Putty Mama", TitleFont, (255, 255, 255), win, 210, 100)

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()

		if(selectedGameMenus == 0):
			DrawText("Press Enter To Play", font, (255, 0, 0), win, 200, 300)
			DrawText("Credits", font, (255, 255, 255), win, 250, 400)
			for event in events:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
						selectedGameMenus += 1
						break
					elif event.key == pygame.K_RETURN:
						gameStates = 1
						break

			if(selectedGameMenus == 1):
				continue

		if(selectedGameMenus == 1):
			DrawText("Press Enter To Play", font, (255, 255, 255), win, 200, 300)
			DrawText("Credits", font, (255, 0, 0), win, 250, 400)
			for event in events:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						selectedGameMenus -= 1
						break

					elif event.key == pygame.K_RETURN:
						selectedGameMenus = 2
						break

			if selectedGameMenus == 0:
				continue

			if selectedGameMenus == 2:
				continue

		if(selectedGameMenus == 2):
			DrawText("Zhengyuan Huang", font, (255, 255, 255), win, 200, 150)
			DrawText("Renee Linford", font, (255, 255, 255), win, 200, 180)
			DrawText("Brandon Montero", font, (255, 255, 255), win, 200, 210)
			DrawText("Saransh Wali", font, (255, 255, 255), win, 200, 240)
			DrawText("Pengxi Wang (Pix)", font, (255, 255, 255), win, 200, 270)
			DrawText("Haotian Zhang", font, (255, 255, 255), win, 200, 300)

			DrawText("Return", font, (255, 0, 0), win, 230, 500)

			for event in events:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						selectedGameMenus -= 1
						break

		pygame.display.update()

	###################### End Of Menu Code ######################

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
			man.vel = -(player.DASH_DELTA_X-man.currentDashFrame)
		elif man.right and man.x < canvas_width - man.width:
			man.vel = player.DASH_DELTA_X-man.currentDashFrame
		else:
			man.vel = 0
	# print('dashcount: %s, isDash %s, vel: %s' %(man.dashCount, man.isDash, man.vel))
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