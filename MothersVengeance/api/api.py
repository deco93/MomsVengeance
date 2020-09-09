import pygame
import sys
from collections import deque
import random
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

TreeTrunk = pygame.image.load('./imgs/tiles/NewTrunk.png')
TreeTrunk = pygame.transform.scale(TreeTrunk, (600, 2400))

clock = pygame.time.Clock()
 
pygame.mixer.init()
pygame.mixer.music.load("./sounds/music.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)


pygame.init()
win = pygame.display.set_mode((canvas_width, canvas_height), 1, 32)
pygame.display.set_caption("MothersVengeance")

#display = pygame.Surface((400,300))

run = True
TitleFont = pygame.font.SysFont('comicsans', 45, True)
font = pygame.font.SysFont('comicsans', 30, True)
man = player.Player(50, 300, 64, 64)
final_layer = [False]
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

putty_baby = pygame.image.load('./imgs/PuttyBaby.png')
putty_baby = pygame.transform.scale(putty_baby, (96, 96))

bird_fly = [pygame.image.load('./imgs/Magpie/Fly1.gif'), pygame.image.load('./imgs/Magpie/Fly2.gif'), pygame.image.load('./imgs/Magpie/Fly3.gif')]
bird_fly = [pygame.transform.scale(bird_fly[0], (128, 128)), pygame.transform.scale(bird_fly[1], (128, 128)), pygame.transform.scale(bird_fly[2], (128, 128))]
bird_fly = [pygame.transform.flip(img, True, False) for img in bird_fly]

bird_catch = [pygame.image.load('./imgs/Magpie/Catch0.gif'),
			  pygame.image.load('./imgs/Magpie/Catch1.gif'),
			  pygame.image.load('./imgs/Magpie/Catch2.gif'),
			  pygame.image.load('./imgs/Magpie/Catch3.gif'),
			  pygame.image.load('./imgs/Magpie/Catch4.gif'),
			  pygame.image.load('./imgs/Magpie/Catch5.gif'),
			  pygame.image.load('./imgs/Magpie/Catch6.gif'),
			  pygame.image.load('./imgs/Magpie/Catch7.gif'),
			  pygame.image.load('./imgs/Magpie/Catch8.gif')]

bird_catch = [pygame.transform.scale(bird_catch[0], (128, 128)),
			  pygame.transform.scale(bird_catch[1], (128, 128)),
			  pygame.transform.scale(bird_catch[2], (128, 128)),
			  pygame.transform.scale(bird_catch[3], (128, 128)),
			  pygame.transform.scale(bird_catch[4], (128, 128)),
			  pygame.transform.scale(bird_catch[5], (128, 128)),
			  pygame.transform.scale(bird_catch[6], (128, 128)),
			  pygame.transform.scale(bird_catch[7], (128, 128)),
			  pygame.transform.scale(bird_catch[8], (128, 128))]

bird_catch = [pygame.transform.flip(img, True, False) for img in bird_catch]

player_rect = pygame.Rect(300,300,48,64)
player_gravity = 0
collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

true_scroll = [0,0]

for x_platform_cood in man.leftPlatformsX:
	man.rightPlatformsX.append( canvas_width - (x_platform_cood + (16*3)) )

game_map = deque( [
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','4','4','4','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','3','3','3','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
			['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']])

init_gamemap_length = len(game_map)

#>1000 value signifies last prcedurally generated platform wasn't a moss so dont need to 
#follow a special spawn rule for current platform as it will anyway be reachable
prevSapY = 1000 


def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile.rect):
            hit_list.append(tile)
    return hit_list

def switchEven():
	global even
	even = not even

#generates randomX coordinate by first radnomly choosing left side or right side and then from 
#corresponding side's choices randomly selects a xcoordinate
def getCoodFromLeftOrRight():
	## 0 is left 1 is right
	#side_choice = random.choice([0, 1])
	#the index of coordinate to be returned from left or right side arrays
	switchEven()
	cood_choice = random.choice([0, 1, 2])
	if even:
		return man.leftPlatformsX[cood_choice]
	else:
		return man.rightPlatformsX[cood_choice]


def blitStripAndUpdateGameMap(randomXCoordinate):
	strip_list = []
	sapPlatformSpawned = False
	if randomXCoordinate == -1:
		x=0
		while x <= (canvas_width - 32):
			strip_list.append('0')
			x+=32
	else:
		x=0
		while x <= (canvas_width - 32):
			if randomXCoordinate>=x and randomXCoordinate<= (x+32):
				r = random.randint(0, 10)
				if r < 1:
					strip_list.extend(['3','3','3'])# ['3', '3' ,'3'] sap
					sapPlatformSpawned = True
				elif r < 2:
					strip_list.extend(['4','4','4'])#  ['4', '4' ,'4'] moss
				else:
					strip_list.extend(['2','2','2'])# (make sure that most of them are normal branches)
				x+=96
			else:
				strip_list.append('0')
				x+=32
	game_map.appendleft(strip_list)
	return sapPlatformSpawned

def getRandomYOffset(maxYOffset):
	return random.randrange(130, int(maxYOffset)+1, 5)

def updateGameMapWithNewPlatform(prevSapPlatformY, currentPlatformY, xCoodForUpdate):
	actualCurrentYOrigin = currentPlatformY
	differenceNewAndPrevSapY = abs(currentPlatformY) - abs(prevSapPlatformY)
	if differenceNewAndPrevSapY >128:
		tempExcessYToBeRemoved = differenceNewAndPrevSapY - 128
		if (tempExcessYToBeRemoved // 32) > 0:
			tempExcessYToBeRemoved = 32 * (tempExcessYToBeRemoved // 32)
			stripOfZeroesToBeUpdated = game_map[int(tempExcessYToBeRemoved/32)-1]
			x = 0
			while x < len(stripOfZeroesToBeUpdated)*32:
				if x <=xCoodForUpdate and xCoodForUpdate <(x+32):
					updateIndex = int(x/32)
					r = random.randint(0, 10)
					if r < 2:	#update with moss platform tile
						stripOfZeroesToBeUpdated[updateIndex] = '4'
						stripOfZeroesToBeUpdated[updateIndex + 1] = '4'
						stripOfZeroesToBeUpdated[updateIndex + 2] = '4'
					else:		#update with normal platform tile
						stripOfZeroesToBeUpdated[updateIndex] = '2'
						stripOfZeroesToBeUpdated[updateIndex + 1] = '2'
						stripOfZeroesToBeUpdated[updateIndex + 2] = '2'
					break

				x+=32
			actualCurrentYOrigin = actualCurrentYOrigin + tempExcessYToBeRemoved	#here actualCurrentYOrigin will always be a -ve number and tempExcessYToBeRemoved a positive number so that new platform's Y coordinate 
																					#has moved effectively that much down, as is required to be within reachable height from prev sap platform
	return actualCurrentYOrigin

def spawnPlatformsNew(y_origin, platform_count, tile_rects):
	global prevSapY
	currentYOrigin = (y_origin + canvas_height) - 32
	current_platform = platform_count
	#platform_y_offset = (canvas_height/platform_count) - (canvas_height/platform_count)/4
	#platform_y_offset = (canvas_height/platform_count) - (canvas_height/platform_count)/platform_count
	while(currentYOrigin >= y_origin and y_origin <0):
		if(current_platform == platform_count or current_platform == 1):
			platform_y_offset = (canvas_height/platform_count) - ((canvas_height/platform_count)/platform_count)
		else:
			platform_y_offset = getRandomYOffset( (canvas_height/platform_count) - ((canvas_height/platform_count)/platform_count) )
		#print(f'platform_y_offset: {platform_y_offset} currentYOrigin: {currentYOrigin} y_origin: {y_origin}')
		current_platform_y = (y_origin + (platform_y_offset * current_platform)) + 32
		#below condition means we have to blit row as a platform containing row
		if (current_platform_y >= currentYOrigin and current_platform_y <= currentYOrigin + 32) or current_platform_y>(currentYOrigin + 32):
			#means this is a strip which will include our platform so align platform y coordinate with current strip being iterated on 
			current_platform_y = currentYOrigin
			#check in man.tileStripMapForY if current Y level strip has already been blitted i.e added to game_map
			if currentYOrigin not in man.tileStripMapForY:
				#blit a tile strip containing 
				sapSpawned = False
				tempYOrigin = 1000	#dummy impossible value for placeholder
				if prevSapY < 0:
					tempYOrigin = updateGameMapWithNewPlatform(prevSapY, currentYOrigin, getCoodFromLeftOrRight())	# supply prevSapY and the tobe possibly the actual 
					#currentYOrigin(in case difference between y coordinates of previous spawned sapPlatform and the tobe spawned platform at currentYOrigin <=96 pixels) 
					prevSapY = 1000
				if(tempYOrigin == currentYOrigin or tempYOrigin == 1000):
					sapSpawned = blitStripAndUpdateGameMap(getCoodFromLeftOrRight())
				if sapSpawned:
					prevSapY = currentYOrigin
				current_platform -= 1
				man.tileStripMapForY[currentYOrigin] = True
			else:
				return
		else:
			if currentYOrigin not in man.tileStripMapForY:
				#blit a 0 tile strip
				blitStripAndUpdateGameMap(-1)
				man.tileStripMapForY[currentYOrigin] = True
			else:
				#means this strip already present so just return from function as above tiles would also have been blitted as well
				return

		currentYOrigin-= 32
	
def spawnFinalLayersWithBaby():

	layers = [
		['0','0','0','0','0','0','0','0','5','5','5','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','4','4','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','4','4','4','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','4','4','4','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		]

	for layer in layers[::-1]:
		game_map.appendleft(layer)

	return True

def redrawGameWindow():
	win.blit(backSky, (0 ,0))
	true_scroll[0] += (player_rect.x - true_scroll[0] - 300) / 20
	true_scroll[1] += (player_rect.y - true_scroll[1] - 280) / 2
	scroll = true_scroll.copy()
	scroll[0] = int(scroll[0])
	scroll[1] = int(scroll[1])
	win.blit(Sky, (0 ,-1400 - scroll[1]/5))
	win.blit(TreeTrunk, (0, -1600 - scroll[1]))
	win.blit(TreeTrunk, (0, -3200 - scroll[1]))
	win.blit(TreeTrunk, (0, -4800 - scroll[1]))
	win.blit(TreeTrunk, (0, -6400 - scroll[1]))
	win.blit(TreeTrunk, (0, -8000 - scroll[1]))


	tile_rects = []
	# print(final_layer[0])
	if not final_layer[0]:
		if -man.maxYCoordinate > 2000:
			final_layer[0] = spawnFinalLayersWithBaby()
			# print(final_layer[0])
		else:
			spawnPlatformsNew(man.maxYCoordinate, 4, tile_rects)


	y = 0
	y = init_gamemap_length - len(game_map)
	for layer in game_map:
		x = 0
		for tile in layer:
			if tile == '1':
				win.blit(dirt_img, (x * 32, y * 32 - scroll[1]))
			if tile == '2':
				# Check tile left & right
				# LHS of screen
				if x < 10:
					# check if the tile the right most branch tile
					if layer[x+1] != '2':
						win.blit(branch_start_right,(x * 32, y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == 0 or layer[x-1] != '2':
						win.blit(branch_end_left,(x * 32, y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_body,(x * 32, y * 32 - scroll[1]))
				# win.blit(grass_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
				# RHS of screen 
				else:
					# check if the tile the right most branch tile
					if layer[x-1] != '2':
						win.blit(branch_start_left,(x * 32, y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == len(layer) - 1 or layer[x+1] != '2':
						win.blit(branch_end_right,(x * 32, y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_body,(x * 32 , y * 32 - scroll[1]))

			if tile == '3':
				# Check tile left & right
				# LHS of screen
				if x < 10:
					# check if the tile the right most branch tile
					if layer[x+1] != '3':
						#length lesser than 2 -> 1 end + 1 body
						if x < 2 or layer [x-2] != '3':
							win.blit(branch_sap,(x * 32 , y * 32 - scroll[1]))
						else:
							win.blit(branch_start_right,(x * 32, y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == 0 or layer[x-1] != '3':
						win.blit(branch_end_left,(x * 32, y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_sap,(x * 32, y * 32 - scroll[1]))
				# win.blit(grass_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
				# RHS of screen 
				else:
					# check if the tile the right most branch tile
					if layer[x-1] != '3':
						#length lesser than 3 -> 1 end + 1 body
						if x > len(layer) - 2 or layer [x-2] != '3':
							win.blit(branch_sap,(x * 32, y * 32 - scroll[1]))
						else:
							win.blit(branch_start_right,(x * 32, y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == len(layer) - 1 or layer[x+1] != '3':
						win.blit(branch_end_right,(x * 32, y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_sap,(x * 32 , y * 32 - scroll[1]))
			
			if tile == '4':
				# Check tile left & right
				# LHS of screen
				if x < 10:
					# check if the tile the right most branch tile
					if layer[x+1] != '4':
						#length lesser than 2 -> 1 end + 1 body
						if x < 2 or layer [x-2] != '4':
							win.blit(branch_moss,(x * 32, y * 32 - scroll[1]))
						else:
							win.blit(branch_start_right,(x * 32, y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == 0 or layer[x-1] != '4':
						win.blit(branch_end_left,(x * 32 , y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_moss,(x * 32, y * 32 - scroll[1]))
				# win.blit(grass_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
				# RHS of screen 
				else:
					# check if the tile the right most branch tile
					if layer[x-1] != '4':
						#length lesser than 3 -> 1 end + 1 body
						if x > len(layer) - 2 or layer [x-2] != '4':
							win.blit(branch_moss,(x * 32, y * 32 - scroll[1]))
						else:
							win.blit(branch_start_right,(x * 32, y * 32 - scroll[1]))
					# check if the tile the left most branch tile
					elif x == len(layer) - 1 or layer[x+1] != '4':
						win.blit(branch_end_right,(x * 32, y * 32 - scroll[1]))
					# if it's in the middle, render it as body
					else:
						win.blit(branch_moss,(x * 32, y * 32 - scroll[1]))

			# Baby
			if tile == '5':
				if layer[x+1] == '5' and layer[x+2] == '5':
					win.blit(putty_baby, (x * 32, y * 32 - scroll[1]))
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
		
		if tile.tile_type == '5' or tile.tile_type == '6':
			man.win = True

	player_rect.y += player_movement[1]
	hit_list = collision_test(player_rect, tile_rects)
	for tile in hit_list:
		if player_movement[1] > 0:
			player_rect.bottom = tile.rect.top
			collision_types['bottom'] = True
			man.onBranch = tile.tile_type

		if tile.tile_type == '5' or tile.tile_type == '6':
			man.win = True

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

	man.x = player_rect.x
	man.y = player_rect.y - scroll[1]

	#print(f'man.y {man.y} man.maxYCoordinate {man.maxYCoordinate} player_rect.y {player_rect.y}')
	if (man.currentViewportLevel >0 and player_rect.y < man.maxYCoordinate) or (player_rect.y < man.maxYCoordinate):
		man.maxYCoordinate -= canvas_height
		man.currentViewportLevel += 1
		#print("next viewportLevel ", man.currentViewportLevel)
	man.draw(win)


	################### Draw Health Bar ####################
	#pygame.draw.rect(win, (255, 0, 0), (20, 20, man.maxHealth, 20))
	#pygame.draw.rect(win, (0, 255, 0), (20, 20, man.currentHealth, 20))
	################### End Of Draw Health Bar #############



	# Dash Cool Down
	# decrease counter by 1
	man.dashCount = max(man.dashCount - 1, 0)
	if man.dashCount == 0:
		man.isDash = False

	pygame.display.update()






def generate_projectile(facing):
	return projectile.Projectile(round(man.x + man.width//2), round(man.y+ man.height//2), 6, (0, 0, 0), facing)
