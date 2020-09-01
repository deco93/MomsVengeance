import pygame

class Player(object):
	def __init__(self, x, y, width, height):
		self.max_health = int(100)
		self.current_health = int(50)
		self.ammo = int(100)
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
		self.walkRight = [pygame.image.load('./imgs/R1.png'), pygame.image.load('./imgs/R2.png'), pygame.image.load('./imgs/R3.png'), pygame.image.load('./imgs/R4.png'), pygame.image.load('./imgs/R5.png'), pygame.image.load('./imgs/R6.png'), pygame.image.load('./imgs/R7.png'), pygame.image.load('./imgs/R8.png'), pygame.image.load('./imgs/R9.png')]
		self.walkLeft = [pygame.image.load('./imgs/L1.png'), pygame.image.load('./imgs/L2.png'), pygame.image.load('./imgs/L3.png'), pygame.image.load('./imgs/L4.png'), pygame.image.load('./imgs/L5.png'), pygame.image.load('./imgs/L6.png'), pygame.image.load('./imgs/L7.png'), pygame.image.load('./imgs/L8.png'), pygame.image.load('./imgs/L9.png')]

	def draw(self, win):
		if self.walkCount + 1 >= 27:
			self.walkCount = 0

		if not(self.standing):
			if self.left:
				win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
			elif self.right:
				win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
		else:
			if self.right:
				win.blit(self.walkRight[0], (self.x, self.y))
			else: 
				win.blit(self.walkLeft[0], (self.x, self.y))
		self.hitbox = (self.x + 12, self.y, self.width - 20, self.height)
		#pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

	#hit event with enemy
	def hit(self, win, canvas_width, canvas_height):
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



