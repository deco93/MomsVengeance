import pygame
import sys
#import random
sys.path.append('classes')
import player, enemy, projectile, healthBar, ammoui

#globals for the project
canvas_width = 600
canvas_height = 800

even = True

bg = pygame.image.load('./imgs/bg.jpg')
backSky = pygame.image.load('./imgs/backSky.png')

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
font = pygame.font.SysFont('comicsans', 30, True)
man = player.Player(50, 300, 64, 64)

score = 0

dirt_img = pygame.image.load('./imgs/tiles/dirt.png')
grass_img = pygame.image.load('./imgs/tiles/grass.png')
dirt_img = pygame.transform.scale(dirt_img, (32, 32))
grass_img = pygame.transform.scale(grass_img, (32, 32))

player_rect = pygame.Rect(300,300,48,64)
player_gravity = 0
collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

true_scroll = [0,0]

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','2','2','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
			['0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','1','1','2','2','0','0','0','0','0','0','0','0','0','0','0','2','2','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','2','2','2','2','2','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0'],
            ['2','2','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
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
        if rect.colliderect(tile):
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
	win.blit(grass_img, (current_platform_x  - scroll[0], current_platform_y - scroll[1]))
	tile_rects.append(pygame.Rect(current_platform_x , current_platform_y  , 32, 32))
	win.blit(grass_img, ((current_platform_x + 32)  - scroll[0], current_platform_y - scroll[1]))
	tile_rects.append(pygame.Rect((current_platform_x + 32)  , current_platform_y , 32, 32))
	win.blit(grass_img, ((current_platform_x + 64)  - scroll[0], current_platform_y - scroll[1]))
	tile_rects.append(pygame.Rect((current_platform_x + 64) , current_platform_y , 32, 32))

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
	

def redrawGameWindow():
	#win.blit(bg, (0 ,0))
	win.blit(backSky, (0 ,0))
	true_scroll[0] += (player_rect.x - true_scroll[0] - 300) / 20
	true_scroll[1] += (player_rect.y - true_scroll[1] - 280) / 2
	scroll = true_scroll.copy()
	scroll[0] = int(scroll[0])
	scroll[1] = int(scroll[1])

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
				win.blit(grass_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
			if tile != '0':
				tile_rects.append(pygame.Rect(x * 32, y * 32, 32, 32))
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
			player_rect.right = tile.left
			collision_types['right'] = True
		elif man.left:
			player_rect.left = tile.right
			collision_types['left'] = True

	player_rect.y += player_movement[1]
	hit_list = collision_test(player_rect, tile_rects)
	for tile in hit_list:
		if player_movement[1] > 0:
			player_rect.bottom = tile.top
			collision_types['bottom'] = True

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

	man.x = player_rect.x - scroll[0]
	man.y = player_rect.y - scroll[1]
	#print(f'man.y {man.y} man.maxYCoordinate {man.maxYCoordinate} player_rect.y {player_rect.y}')
	if (man.currentViewportLevel >0 and player_rect.y < man.maxYCoordinate) or (player_rect.y < man.maxYCoordinate):
		man.maxYCoordinate -= canvas_height
		man.currentViewportLevel += 1
		#print("next viewportLevel ", man.currentViewportLevel)
	man.draw(win)
	pygame.display.update()





def generate_projectile(facing):
	return projectile.Projectile(round(man.x + man.width//2), round(man.y+ man.height//2), 6, (0, 0, 0), facing)
