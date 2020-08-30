import pygame

canvas_width = 400
canvas_height = 400
healthbar_width = 50
healthbar_height = 10

walkRight = [pygame.image.load('./imgs/R1.png'), pygame.image.load('./imgs/R2.png'), pygame.image.load('./imgs/R3.png'), pygame.image.load('./imgs/R4.png'), pygame.image.load('./imgs/R5.png'), pygame.image.load('./imgs/R6.png'), pygame.image.load('./imgs/R7.png'), pygame.image.load('./imgs/R8.png'), pygame.image.load('./imgs/R9.png')]
walkLeft = [pygame.image.load('./imgs/L1.png'), pygame.image.load('./imgs/L2.png'), pygame.image.load('./imgs/L3.png'), pygame.image.load('./imgs/L4.png'), pygame.image.load('./imgs/L5.png'), pygame.image.load('./imgs/L6.png'), pygame.image.load('./imgs/L7.png'), pygame.image.load('./imgs/L8.png'), pygame.image.load('./imgs/L9.png')]
bg = pygame.image.load('./imgs/bg.jpg')
char = pygame.image.load('./imgs/standing.png')


pygame.mixer.init()
#bullet_sound = pygame.mixer.music.load("./sounds/bullet.mp3")
#hit_sound = pygame.mixer.music.load("./sounds/hit.mp3")
#bullet_sound = pygame.mixer.Sound("./sounds/bullet.mp3")
#hit_sound = pygame.mixer.Sound("./sounds/hit.mp3")

pygame.mixer.music.load("./sounds/music.mp3")

pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

score = 0

class player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.jumpCount = 10
		self.isJump = False
		self.left = False
		self.right = False
		self.walkCount = 0
		self.standing = True
		self.hitbox = (self.x + 12, self.y, self.width - 20, self.height)

	def draw(self, win):
		if self.walkCount + 1 >= 27:
			self.walkCount = 0

		if not(self.standing):
			if self.left:
				win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
			elif self.right:
				win.blit(walkRight[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
		else:
			if self.right:
				win.blit(walkRight[0], (self.x, self.y))
			else: 
				win.blit(walkLeft[0], (self.x, self.y))
		self.hitbox = (self.x + 12, self.y, self.width - 20, self.height)
		#pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

	#hit event with enemy
	def hit(self, win):
		#resetting player on hit with enemy
		self.x = 50
		self.y = 300
		self.walkCount = 0
		font1 = pygame.font.SysFont('comicsans', 100)
		text = font1.render('-5', 1, (255, 0, 0))
		win.blit(text, (canvas_width/2 - (text.get_width()/2), (canvas_height/2 -(text.get_height()/2))))
		pygame.display.update()
		i = 0
		while i < 300:
			pygame.time.delay(10)
			i += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					i = 301
					pygame.quit()
		#pygame.draw.rect(win, (255,0,0), (self.x+12, self.y, self.width - 20, self.height), 2)

class projectile(object):
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 8 * facing

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class enemy(object):
	walkRight = [pygame.image.load('./imgs/R1E.png'), pygame.image.load('./imgs/R2E.png'), pygame.image.load('./imgs/R3E.png'), pygame.image.load('./imgs/R4E.png'), pygame.image.load('./imgs/R5E.png'), pygame.image.load('./imgs/R6E.png'), pygame.image.load('./imgs/R7E.png'), pygame.image.load('./imgs/R8E.png'), pygame.image.load('./imgs/R9E.png'), pygame.image.load('./imgs/R10E.png'), pygame.image.load('./imgs/R11E.png')]
	walkLeft = [pygame.image.load('./imgs/L1E.png'), pygame.image.load('./imgs/L2E.png'), pygame.image.load('./imgs/L3E.png'), pygame.image.load('./imgs/L4E.png'), pygame.image.load('./imgs/L5E.png'), pygame.image.load('./imgs/L6E.png'), pygame.image.load('./imgs/L7E.png'), pygame.image.load('./imgs/L8E.png'), pygame.image.load('./imgs/L9E.png'), pygame.image.load('./imgs/L10E.png'), pygame.image.load('./imgs/L11E.png')]

	def __init__(self, x, y, width, height, end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x, self.end]
		self.walkCount = 0
		self.vel = 3
		self.hitbox = (self.x + 12, self.y, self.width - 20, self.height)
		self.health = 10
		self.visible = True

	def draw(self, win):
		self.move()
		if self.visible:
			if self.walkCount +1 >= 33:
				self.walkCount = 0

			if self.vel > 0:
				win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
			else:
				win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
			pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, healthbar_width, healthbar_height), 0)
			pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, self.health * (healthbar_width/10), healthbar_height), 0)
			self.hitbox = (self.x + 12, self.y, self.width - 20, self.height)
		#pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

	def move(self):
		if self.vel > 0:
			if self.x + self.vel < self.path[1]:
				self.x += self.vel
			else:
				self.vel = self.vel * -1
				self.walkCount = 0
		else:
			if self.x + self.vel > self.path[0]:
				self.x += self.vel
			else:
				self.vel = self.vel * -1
				self.walkCount = 0

	def hit(self):
		global score
		if self.health > 0:
			self.health -= 1
			score += 1
			pygame.mixer.Channel(1).play(pygame.mixer.Sound('./sounds/hit.wav'))

		if self.health == 0:
			self.visible = False
		print('GOBLIN HIT...')


pygame.init()
win = pygame.display.set_mode((canvas_width, canvas_height))

pygame.display.set_caption("MothersVengeance")


def redrawGameWindow():
	win.blit(bg, (0 ,0))
	text = font.render('Score: '+ str(score), 1, (0, 0, 0))
	win.blit(text, (275, 10))
	man.draw(win)
	goblin.draw(win)
	#actually drawing the bullets from bullet spamming
	for bullet in bullets:
		bullet.draw(win)
	#pygame.draw.rect(win, (255,0,0), (x,y, width, height))
	pygame.display.update()

run = True
font = pygame.font.SysFont('comicsans', 30, True)
man = player(50, 300, 64, 64)
#goblin = enemy(30, 300, 64, 64, 200)
goblin = enemy(120, 300, 64, 64, 200)
bullets = []
spaceSpamCount = 0
#main loop
while run:
	clock.tick(27)	#for setting FPS to 27
	#pygame.time.delay(27)
	if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1] and goblin.visible:
		if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
			man.hit(win)
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
					goblin.hit()
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
		if len(bullets) < 5:
			bullets.append(projectile(round(man.x + man.width//2), round(man.y+ man.height//2), 6, (0, 0, 0), facing))
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
		#if keys[pygame.K_UP] and y >= vel:
		#	y -= vel
		#if keys[pygame.K_DOWN] and y < canvas_height - height:
		#	y += vel
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