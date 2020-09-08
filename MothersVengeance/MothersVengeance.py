import pygame
import sys
from api.api import *
import time

#pygame.mixer.init()
#pygame.mixer.music.load("./sounds/music.mp3")

#pygame.mixer.music.play(-1)
air_time = 0
jump_delta = -15

win = pygame.display.set_mode((canvas_width, canvas_height), 1, 32)

## Game States 0 For Starting Menu, 1 For Running Game, 2 For Game Lose Menu
gameStates = 0

selectedGameMenus = 0

birdAnimCounter = 0
birdAnimSpeed = 5
birdAnimFrame = 0

birdStartLocation = (0, 0)
birdLandLocation = (310, 230)
birdCurrentLocationX = birdStartLocation[0]
birdCurrentLocationY = birdStartLocation[1]

bird_Current_Frame = bird_catch[0]

babyLocation = (400, 265)
differenceX = babyLocation[0] - birdLandLocation[0]
differenceY = babyLocation[1] - birdLandLocation[1]

branch_moss = pygame.image.load('./imgs/tiles/Branch_Moss.png')


def DrawText(text, font, color, surface, x, y):
	textObj = font.render(text, 1, color)
	textRect = textObj.get_rect()
	textRect.topleft = (x, y)
	win.blit(textObj, textRect)





start_ticks = pygame.time.get_ticks()

#main loop
while run:

	clock.tick(30)	#for setting FPS to 30

	######################### Menu Code ########################
	while(gameStates == 0):
		win.blit(Sky, (0 ,-1400))
		win.blit(TreeTrunk, (150, -1600))

		win.blit(branch_body, (300, 350))
		win.blit(branch_moss, (332, 350))
		win.blit(branch_moss, (364, 350))
		win.blit(branch_body, (396, 350))
		win.blit(branch_body, (428, 350))
		win.blit(branch_end_right, (460, 350))



		if(birdAnimCounter >= birdAnimSpeed):
			birdAnimCounter = 0
			birdAnimFrame += 1
		else:
			birdAnimCounter += 1

		if(birdCurrentLocationX < birdLandLocation[0]):
			birdCurrentLocationX += birdLandLocation[0] / 200
			birdCurrentLocationY += birdLandLocation[1] / 200
			win.blit(bird_fly[birdAnimFrame % 3], (birdCurrentLocationX, birdCurrentLocationY))
			win.blit(putty_baby, babyLocation)

		elif(bird_Current_Frame != bird_catch[8]):
			bird_Current_Frame = bird_catch[birdAnimFrame % 9]
			win.blit(bird_catch[birdAnimFrame % 9], (birdCurrentLocationX, birdCurrentLocationY))
			win.blit(putty_baby, babyLocation)
		else:
			birdCurrentLocationX += birdLandLocation[0] / 200
			birdCurrentLocationY -= birdLandLocation[1] / 200



			win.blit(bird_fly[birdAnimFrame % 3], (birdCurrentLocationX, birdCurrentLocationY))
			win.blit(putty_baby, (birdCurrentLocationX + differenceX, birdCurrentLocationY + differenceY))

		DrawText("Putty Mama", TitleFont, (255, 255, 255), win, 195, 100)

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()

		if(selectedGameMenus == 0):
			DrawText("Press Enter To Play", font, (255, 0, 0), win, 180, 300)
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
			DrawText("Press Enter To Play", font, (255, 255, 255), win, 180, 300)
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
			DrawText("Zhengyuan Huang", font, (255, 255, 255), win, 200, 200)
			DrawText("Renee Linford", font, (255, 255, 255), win, 200, 240)
			DrawText("Brandon Montero", font, (255, 255, 255), win, 200, 280)
			DrawText("Saransh Wali", font, (255, 255, 255), win, 200, 320)
			DrawText("Pengxi Wang (Pix)", font, (255, 255, 255), win, 200, 360)
			DrawText("Haotian Zhang", font, (255, 255, 255), win, 200, 400)

			DrawText("Return", font, (255, 0, 0), win, 250, 500)

			for event in events:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						selectedGameMenus -= 1
						break

		pygame.display.update()

	if gameStates == 2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


		win.fill((0,0,0))

		DrawText("Failed To Save Baby!", font, (255, 0, 255), win, 210, 300)
		pygame.display.update()

	if gameStates == 3:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		run = False

		win.fill((0,0,0))

		
		pygame.mixer.music.load("./sounds/greyandmama_combined.wav")
		pygame.mixer.music.set_volume(0.1)
		pygame.mixer.music.play()
		flipper = True
		while pygame.mixer.music.get_busy():
			flipper = not flipper	#just flipping a random value until sound completed
		DrawText("You Win!", font, (255, 0, 255), win, 250, 300)
		DrawText("The Bravest Putty Mom Has Saved Her Baby!", font, (255, 0, 255), win, 50, 350)
		#time.sleep(3000)
		#baby_sound.stop()
		pygame.display.update()
		

	###################### End Of Menu Code ######################
	if gameStates == 1:

		seconds = (pygame.time.get_ticks() - start_ticks) / 1000
		counter = 61 - seconds

		if man.win:
			gameStates = 3

		if (counter <= 0):
			gameStates = 2

		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()



		if keys[pygame.K_LEFT] and man.x >= man.vel and not man.isDash:
			#man.x -= man.vel
			man.vel = -5 if man.onBranch != '4' else 0
			man.left = True
			man.right = False
			man.standing = False
		elif keys[pygame.K_RIGHT] and man.x < canvas_width - man.width and not man.isDash:
			#man.x += man.vel
			man.vel = 5 if man.onBranch != '4' else 0
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
					man.gravity = -23 if man.currentSquishFrame > 1 else (-15 * man.currentSquishFrame)
				else:
					man.gravity = -15
				if man.onBranch == '3':
					man.gravity = man.gravity * 2 // 3

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


		redrawGameWindow()



		display = font.render(str(int(counter)), 1, (0,0,0))
		win.blit(display, (20, 20))

		pygame.display.update()

pygame.quit()