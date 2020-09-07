import pygame
import sys
#import random
sys.path.append('classes')
import player, enemy, projectile, healthBar, ammoui, tile_rect

#globals for the project
canvas_width = 600
canvas_height = 800

even = True

bg = pygame.image.load('./imgs/bg.jpg')
backSky = pygame.image.load('./imgs/backSky.png')
backSky = pygame.transform.scale(backSky, (600, 1200))

Sky = pygame.image.load('./imgs/Sky.png')

clock = pygame.time.Clock()
 
pygame.mixer.init()
pygame.mixer.music.load("./sounds/music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


pygame.init()
win = pygame.display.set_mode((canvas_width, canvas_height), 1, 32)
pygame.display.set_caption("MothersVengeance")

#display = pygame.Surface((400,300))

run = True
TitleFont = pygame.font.SysFont('comicsans', 45, True)
font = pygame.font.SysFont('comicsans', 30, True)
man = player.Player(50, 300, 64, 64)

score = 0

dirt_img = pygame.image.load('./imgs/tiles/dirt.png')
grass_img = pygame.image.load('./imgs/tiles/grass.png')
dirt_img = pygame.transform.scale(dirt_img, (32, 32))
grass_img = pygame.transform.scale(grass_img, (32, 32))

branch_moss = pygame.image.load('./imgs/tiles/Branch_Moss.png')
branch_sap = pygame.image.load('./imgs/tiles/Branch_Sap.png')
branch_body = pygame.image.load('./imgs/tiles/Branch_Body.png')
branch_start_left = pygame.image.load('./imgs/tiles/Branch_Start.png')
branch_start_right = pygame.transform.flip(branch_start_left, True, False)
branch_end_right = pygame.image.load('./imgs/tiles/Branch_End_New.png')
branch_end_left = pygame.transform.flip(branch_end_right, True, False)


player_rect = pygame.Rect(300,300,48,64)
player_gravity = 0
collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

true_scroll = [0,0]

run = True

gameStates = 0



game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','3','3','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','4','4','4','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','3','3','3','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','1','1','2','2','0','0','0','0','0','0','0','0','0','0','0','2','2','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','2','2','2','2','2','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['2','2','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['1','1','2','2','2','2','1','1','1','1','1','1','1','2','2','2','2','1','1','2','2','2','2','2','2','1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]



def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile.rect):
            hit_list.append(tile)
    return hit_list

def switchEven():
	global even
	even = not even

#can be called during camera move to plot the platforms alternately on left and right with order reveres from previous viewport
def checkEvenOrOdd(current_platform):
	global even
	if even:
		return current_platform % 2
	else:
		return not (current_platform % 2)

def spawnUnitPlatform(current_platform_x, current_platform_y, tile_rects, scroll):
	#win.blit(grass_img, (300 - scroll[0], -50 - scroll[1]))
	#tile_rects.append(pygame.Rect(300 , -50  , 32, 32))
	win.blit(branch_body, (current_platform_x  - scroll[0], current_platform_y - scroll[1]))
	tile_rects.append(tile_rect.TileRect(tile_type='2', rect=pygame.Rect(current_platform_x , current_platform_y  , 32, 32)))
	win.blit(branch_body, ((current_platform_x + 32)  - scroll[0], current_platform_y - scroll[1]))
	tile_rects.append(tile_rect.TileRect(tile_type='2', rect=pygame.Rect((current_platform_x + 32)  , current_platform_y , 32, 32)))
	win.blit(branch_body, ((current_platform_x + 64)  - scroll[0], current_platform_y - scroll[1]))
	tile_rects.append(tile_rect.TileRect(tile_type='2', rect=pygame.Rect((current_platform_x + 64) , current_platform_y , 32, 32)))


def spawnPlatforms(y_origin, platform_count, tile_rects, scroll):
	#print(f'man.currentViewportLevel: {man.currentViewportLevel} yorigin: {y_origin}')
	currentViewportLevel = man.currentViewportLevel
	currentYOrigin = y_origin
	while currentViewportLevel >= 0:
		#print(f'---- currentViewportLevel: {currentViewportLevel}')
		current_platform = 1
		platform_y_offset = (canvas_height/platform_count) - (canvas_height/platform_count)/4
		# randomly choosing whether to spawn current platform on left or right
		while (currentViewportLevel > 0 and current_platform <= platform_count) or current_platform < platform_count:
			if checkEvenOrOdd(current_platform):
				current_platform_x = 220
				#current_platform_x = 50
			else:
				current_platform_x = canvas_width - (220 + (16*3))
				#current_platform_x = canvas_width - (50 + (16*3))
			current_platform_y = currentYOrigin + (platform_y_offset * current_platform)
			#spawn a series of 3 dirt tiles one after other to simulate a platform and check if the last platform for that frame it should spawn a bit lower eg here 70px
			spawnUnitPlatform(current_platform_x, current_platform_y + 70 if current_platform == platform_count else current_platform_y, tile_rects, scroll)
			current_platform += 1

		currentViewportLevel -= 1
		currentYOrigin += canvas_height


def DrawText(text, font, color, surface, x, y):
	textObj = font.render(text, 1, color)
	textRect = textObj.get_rect()
	textRect.topleft = (x, y)
	win.blit(textObj, textRect)





def redrawGameWindow():

	true_scroll[0] += (player_rect.x - true_scroll[0] - 300) / 20
	true_scroll[1] += (player_rect.y - true_scroll[1] - 280) / 2
	scroll = true_scroll.copy()
	scroll[0] = int(scroll[0])
	scroll[1] = int(scroll[1])
	win.blit(Sky, (0 ,-1400 - scroll[1]/10))
	#man.draw(display)
	#goblin.draw(display)
	#actually drawing the bullets from bullet spamming

	tile_rects = []
	spawnPlatforms(man.maxYCoordinate, 4, tile_rects, scroll)
	y = 0
	for layer in game_map:
		x = 0
		for tile in layer:
			if tile == '1':
				win.blit(dirt_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
			if tile == '2':
				# Check tile left & right
				# LHS of screen
				if x < 10:
					# check if the tile the right most branch tile
					if layer[x+1] != '2':
						win.blit(branch_start_right,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == 0 or layer[x-1] != '2':
						win.blit(branch_end_left,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_body,(x * 32 - scroll[0], y * 32 - scroll[1]))
				# win.blit(grass_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
				# RHS of screen 
				else:
					# check if the tile the right most branch tile
					if layer[x-1] != '2':
						win.blit(branch_start_left,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == len(layer) - 1 or layer[x+1] != '2':
						win.blit(branch_end_right,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_body,(x * 32 - scroll[0], y * 32 - scroll[1]))

			if tile == '3':
				# Check tile left & right
				# LHS of screen
				if x < 10:
					# check if the tile the right most branch tile
					if layer[x+1] != '3':
						#length lesser than 2 -> 1 end + 1 body
						if x < 2 or layer [x-2] != '3':
							win.blit(branch_sap,(x * 32 - scroll[0], y * 32 - scroll[1]))
						else:
							win.blit(branch_start_right,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == 0 or layer[x-1] != '3':
						win.blit(branch_end_left,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_sap,(x * 32 - scroll[0], y * 32 - scroll[1]))
				# win.blit(grass_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
				# RHS of screen 
				else:
					# check if the tile the right most branch tile
					if layer[x-1] != '3':
						#length lesser than 3 -> 1 end + 1 body
						if x > len(layer) - 2 or layer [x-2] != '3':
							win.blit(branch_sap,(x * 32 - scroll[0], y * 32 - scroll[1]))
						else:
							win.blit(branch_start_right,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == len(layer) - 1 or layer[x+1] != '3':
						win.blit(branch_end_right,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_sap,(x * 32 - scroll[0], y * 32 - scroll[1]))
			
			if tile == '4':
				# Check tile left & right
				# LHS of screen
				if x < 10:
					# check if the tile the right most branch tile
					if layer[x+1] != '4':
						#length lesser than 2 -> 1 end + 1 body
						if x < 2 or layer [x-2] != '4':
							win.blit(branch_moss,(x * 32 - scroll[0], y * 32 - scroll[1]))
						else:
							win.blit(branch_start_right,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == 0 or layer[x-1] != '4':
						win.blit(branch_end_left,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_sap,(x * 32 - scroll[0], y * 32 - scroll[1]))
				# win.blit(grass_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
				# RHS of screen 
				else:
					# check if the tile the right most branch tile
					if layer[x-1] != '4':
						#length lesser than 3 -> 1 end + 1 body
						if x > len(layer) - 2 or layer [x-2] != '4':
							win.blit(branch_moss,(x * 32 - scroll[0], y * 32 - scroll[1]))
						else:
							win.blit(branch_start_right,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == len(layer) - 1 or layer[x+1] != '4':
						win.blit(branch_end_right,(x * 32 - scroll[0], y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_moss,(x * 32 - scroll[0], y * 32 - scroll[1]))
			if tile != '0':
				tile_rects.append(tile_rect.TileRect(tile_type=tile, rect=pygame.Rect(x * 32, y * 32, 32, 32)))
			x += 1
		y += 1

	player_movement = [0, 0]
	player_movement[0] += man.vel
	player_movement[1] += man.gravity
	man.gravity += 1
	if man.isBubbled:
		if man.gravity > player.MAXIMUM_BUBBLED_DROP_SPEED:
			man.gravity = player.MAXIMUM_BUBBLED_DROP_SPEED
	else:
		if man.gravity > player.MAXIMUM_DROP_SPEED:
			man.gravity = player.MAXIMUM_DROP_SPEED



	collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

	player_rect.x += player_movement[0]
	hit_list = collision_test(player_rect, tile_rects)
	#print("tile_rects length: "+ str(len(tile_rects)))
	for tile in hit_list:
		if man.right:
			player_rect.right = tile.rect.left
			collision_types['right'] = True
		elif man.left:
			player_rect.left = tile.rect.right
			collision_types['left'] = True

	player_rect.y += player_movement[1]
	hit_list = collision_test(player_rect, tile_rects)
	for tile in hit_list:
		if player_movement[1] > 0:
			player_rect.bottom = tile.rect.top
			collision_types['bottom'] = True
			man.onBranch = tile.tile_type

	if man.isJump and collision_types['bottom'] == True:
		collision_types['bottom'] = False
		man.gravity = -10
		man.jumpCount -= 1
		man.isInAir = True

	if collision_types['bottom'] == True:
		man.isJump = False
		man.gravity = 0
		man.jumpCount = 0
	else:
		man.jumpCount+=1
		man.onBranch = ''

	man.x = player_rect.x - scroll[0]
	man.y = player_rect.y - scroll[1]

	#print(f'man.y {man.y} man.maxYCoordinate {man.maxYCoordinate} player_rect.y {player_rect.y}')
	if (man.currentViewportLevel >0 and player_rect.y < man.maxYCoordinate) or (player_rect.y < man.maxYCoordinate):
		man.maxYCoordinate -= canvas_height
		man.currentViewportLevel += 1
		#print("next viewportLevel ", man.currentViewportLevel)
	man.draw(win)

	# Dash Cool Down
	# decrease counter by 1
	man.dashCount = max(man.dashCount - 1, 0)
	if man.dashCount == 0:
		man.isDash = False

	pygame.display.update()






def generate_projectile(facing):
	return projectile.Projectile(round(man.x + man.width//2), round(man.y+ man.height//2), 6, (0, 0, 0), facing)
