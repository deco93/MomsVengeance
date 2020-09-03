import pygame

class Player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.jumpCount = 0
		self.isJump = False
		self.left = False
		self.right = False
		self.walkCount = 0
		self.standCount = 0
		self.standing = True
		self.gravity = 0
		self.hitbox = (self.x + 12, self.y, self.width - 20, self.height)
		self.idleRight = [ pygame.image.load('./imgs/player/idle/Idle {}.png'.format(i)) for i in range(1,6)]
		self.idleLeft = [ pygame.transform.flip(img, True, False) for img in self.idleRight]
		self.walkRight = [ pygame.image.load('./imgs/player/walk/Walk {}.png'.format(i)) for i in range(1,9)]
		self.walkLeft = [ pygame.transform.flip(img, True, False) for img in self.walkRight]

		self.idleAnimCount = 5
		self.IdelAnimCounter = 0
		self.currentIdleFrame = 0
		self.walkAnimCount = 7
		self.WalkAnimCounter = 0
		self.currentWalkFrame = 0
		self.animSpeed = 5
		self.walkAnimSpeed = 2

		self.isInAir = True
		self.maxYCoordinate = 0 
		self.currentViewportLevel = 0

	def draw(self, win):

		if self.IdelAnimCounter >= self.animSpeed:
			self.IdelAnimCounter = 0
			self.currentIdleFrame += 1
			if self.currentIdleFrame == self.idleAnimCount:
				self.currentIdleFrame = 0
		else:
			self.IdelAnimCounter += 1

		if self.WalkAnimCounter >= self.walkAnimSpeed:
			self.WalkAnimCounter = 0
			self.currentWalkFrame += 1
			if self.currentWalkFrame == self.walkAnimCount:
				self.currentWalkFrame = 0
		else:
			self.WalkAnimCounter += 1


		if not(self.standing):
			if self.left:
				#win.blit(self.walkLeft[self.walkCount % len(self.walkRight)], (self.x, self.y))
				win.blit(self.walkLeft[self.currentWalkFrame], (self.x, self.y))
			elif self.right:
				#win.blit(self.walkRight[self.walkCount % len(self.walkLeft)], (self.x, self.y))
				win.blit(self.walkRight[self.currentWalkFrame], (self.x, self.y))
			self.walkCount = (self.walkCount + 1) % 30
			self.standCount = 0
		else:
			if self.right:
				#win.blit(self.idleRight[self.standCount % len(self.idleRight)], (self.x, self.y))
				win.blit(self.idleRight[self.currentIdleFrame], (self.x, self.y))
			else: 
				#win.blit(self.idleLeft[self.standCount % len(self.idleLeft)], (self.x, self.y))
				win.blit(self.idleLeft[self.currentIdleFrame], (self.x, self.y))
			self.standCount = (self.standCount + 1) % 30
			self.walkCount = 0
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



