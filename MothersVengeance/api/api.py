import pygame
import sys
import random
sys.path.append('classes')
import player, enemy, projectile, healthBar, ammoui
from collections import deque

#globals for the project
canvas_width = 800	#keep canvas_width a multiple of 32 always so increase and decrease accordingly as tiles and platforms spawned accordingly
canvas_height = 600

even = True

bg = pygame.image.load('./imgs/bg.jpg')
backSky = pygame.image.load('./imgs/backSky.png')

clock = pygame.time.Clock()
 
pygame.mixer.init()
pygame.mixer.music.load("./sounds/music.mp3")
pygame.mixer.music.set_volume(0.0)
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

for x_platform_cood in man.leftPlatformsX:
	man.rightPlatformsX.append( canvas_width - (x_platform_cood + (16*3)) )

game_map = deque( [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
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
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']])

init_gamemap_length = len(game_map)

def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
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
	if randomXCoordinate == -1:
		x=0
		while x <= (canvas_width - 32):
			strip_list.append('0')
			x+=32
	else:
		x=0
		while x <= (canvas_width - 32):
			if randomXCoordinate>=x and randomXCoordinate<= (x+32):
				strip_list.extend(['2','2','2'])
				x+=96
			else:
				strip_list.append('0')
				x+=32
	game_map.appendleft(strip_list)


def spawnPlatformsNew(y_origin, platform_count, tile_rects, scroll):
	currentYOrigin = (y_origin + canvas_height) - 32
	current_platform = platform_count
	#platform_y_offset = (canvas_height/platform_count) - (canvas_height/platform_count)/4
	platform_y_offset = (canvas_height/platform_count) - (canvas_height/platform_count)/platform_count
	while(currentYOrigin >= y_origin and y_origin <0):
		current_platform_y = (y_origin + (platform_y_offset * current_platform)) + 32
		#below condition means we have to blit row as a platform containing row
		if current_platform_y >= currentYOrigin and current_platform_y <= currentYOrigin + 32:
			#means this is a strip which will include our platform so align platform y coordinate with current strip being iterated on 
			current_platform_y = currentYOrigin
			#check in man.tileStripMapForY if current Y level strip has already been blitted i.e added to game_map
			if currentYOrigin not in man.tileStripMapForY:
				#blit a tile strip containing 
				blitStripAndUpdateGameMap(getCoodFromLeftOrRight())
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
	

def redrawGameWindow():
	win.blit(backSky, (0 ,0))
	true_scroll[0] += (player_rect.x - true_scroll[0] - 300) / 20
	true_scroll[1] += (player_rect.y - true_scroll[1] - 280) / 2
	scroll = true_scroll.copy()
	scroll[0] = int(scroll[0])
	scroll[1] = int(scroll[1])
	
	tile_rects = []

	spawnPlatformsNew(man.maxYCoordinate, 4, tile_rects, scroll)
	y = 0
	y = init_gamemap_length - len(game_map)
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
	if man.gravity > 20:
		man.gravity = 20

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
