import pygame

canvas_width = 400
canvas_height = 400

walkRight = [pygame.image.load('./imgs/R1.png'), pygame.image.load('./imgs/R2.png'), pygame.image.load('./imgs/R3.png'), pygame.image.load('./imgs/R4.png'), pygame.image.load('./imgs/R5.png'), pygame.image.load('./imgs/R6.png'), pygame.image.load('./imgs/R7.png'), pygame.image.load('./imgs/R8.png'), pygame.image.load('./imgs/R9.png')]
walkLeft = [pygame.image.load('./imgs/L1.png'), pygame.image.load('./imgs/L2.png'), pygame.image.load('./imgs/L3.png'), pygame.image.load('./imgs/L4.png'), pygame.image.load('./imgs/L5.png'), pygame.image.load('./imgs/L6.png'), pygame.image.load('./imgs/L7.png'), pygame.image.load('./imgs/L8.png'), pygame.image.load('./imgs/L9.png')]
bg = pygame.image.load('./imgs/bg.jpg')
char = pygame.image.load('./imgs/standing.png')

clock = pygame.time.Clock()

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

	def draw(self, win):
		self.move()
		if self.walkCount +1 >= 33:
			self.walkCount = 0

		if self.vel > 0:
			win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
			self.walkCount += 1
		else:
			win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
			self.walkCount += 1
		# pygame.draw.rect(win, (255,0,0), (self.x + 12, self.y, self.width - 20, self.height), 2)

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

	#def hit(self):
		#print('GOBLIN HIT...')
		#pass


pygame.init()
win = pygame.display.set_mode((canvas_width, canvas_height))

pygame.display.set_caption("MothersVengeance")


def redrawGameWindow():
	win.blit(bg, (0 ,0))
	man.draw(win)
	goblin.draw(win)
	#actually drawing the bullets from bullet spamming
	for bullet in bullets:
		bullet.draw(win)
	#pygame.draw.rect(win, (255,0,0), (x,y, width, height))
	pygame.display.update()

run = True
man = player(50, 300, 64, 64)
goblin = enemy(30, 300, 64, 64, 200)
bullets = []
#main loop
while run:
	clock.tick(27)	#for setting FPS to 27
	#pygame.time.delay(27)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for bullet in bullets:

		if bullet.x < canvas_width and bullet.x > 0:
			bullet.x += bullet.vel
		else:
			bullets.pop(bullets.index(bullet))
	keys = pygame.key.get_pressed()

	#logic for bullet creation and direction
	if keys[pygame.K_SPACE]:
		if man.left:
			facing = -1
		else:
			facing = 1
		if len(bullets) < 5:
			bullets.append(projectile(round(man.x + man.width//2), round(man.y+ man.height//2), 6, (0, 0, 0), facing))

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