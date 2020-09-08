import pygame

DASH_COOL_DOWN = 17
DASH_DELTA_X= 17
MAXIMUM_DROP_SPEED = 15
MAXIMUM_BUBBLED_DROP_SPEED = 3

class Player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.jumpCount = 0
		self.dashCount = 0
		self.isDash = False
		self.isBubbled = False
		self.isSquish = False
		self.isJump = False
		self.left = False
		self.right = False
		self.standing = True
		self.gravity = 0
		self.hitbox = (self.x + 12, self.y, self.width - 20, self.height)
		self.onBranch = '0'
		self.maxHealth = 200
		self.currentHealth = self.maxHealth

		# Animation frams 
		self.idleRight = [ pygame.image.load('./imgs/player/idle/Idle {}.png'.format(i)) for i in range(1,6)]
		self.idleLeft = [ pygame.transform.flip(img, True, False) for img in self.idleRight]
		self.walkRight = [ pygame.image.load('./imgs/player/walk/Walk {}.png'.format(i)) for i in range(1,9)]
		self.walkLeft = [ pygame.transform.flip(img, True, False) for img in self.walkRight]
		self.squishRight = [pygame.image.load('./imgs/player/squish/Squish {}.png'.format(i)) for i in range(1,4) ]
		self.squishLeft = [ pygame.transform.flip(img, True, False) for img in self.squishRight]
		self.bubbleRight = [pygame.image.load('./imgs/player/bubble/Bubble {}.png'.format(i)) for i in range(1,5)]
		self.bubbleLeft = [ pygame.transform.flip(img, True, False) for img in self.bubbleRight]
		self.dashRight = [pygame.image.load('./imgs/player/dash/dash {}.png'.format(i)) for i in range(1,18)]
		self.dashLeft = [ pygame.transform.flip(img, True, False) for img in self.dashRight]
		
		# Counters and others
		self.dashAnimCounter = 0
		self.currentDashFrame = 0
		self.BubbleAnimCounter = 0
		self.currentBubbleFrame = 0
		self.leftPlatformsX = [140, 190, 230]
		self.rightPlatformsX = [] #fill these later in api.py according to canvas width global

		self.IdleAnimCounter = 0
		self.currentIdleFrame = 0
		self.WalkAnimCounter = 0
		self.currentWalkFrame = 0
		self.squishAnimCounter = 0
		self.currentSquishFrame = 0
		self.animSpeed = 5
		self.walkAnimSpeed = 2
		self.squishAnimSpeed = 7
		self.BubbleAnimSpeed = 3
		self.dashAnimSpeed = 1
		self.isInAir = True
		self.maxYCoordinate = 0 
		self.currentViewportLevel = 0
		self.tileStripMapForY = {}	#stores a bool which indicates if an entire strip of tiles have been pushed against that y coordinate

	def __increAnim(self, counter, length, frame, speed, repeat = False):
		
		if self.__dict__[counter] >= speed:
			self.__dict__[counter] = 0
			self.__dict__[frame] += 1
			if repeat:
				if self.__dict__[frame] == length:
					self.__dict__[frame] = 0
			else:
				if self.__dict__[frame] == length:
					self.__dict__[frame] = length - 1 
		else:
			self.__dict__[counter] += 1


	def draw(self, win):

		self.__increAnim('IdleAnimCounter', len(self.idleRight), 'currentIdleFrame', self.animSpeed, repeat= True)
		self.__increAnim('WalkAnimCounter', len(self.walkRight), 'currentWalkFrame', self.walkAnimSpeed, repeat= True)
		self.__increAnim('squishAnimCounter', len(self.squishRight), 'currentSquishFrame', self.squishAnimSpeed, repeat= False)
		self.__increAnim('BubbleAnimCounter', len(self.bubbleRight), 'currentBubbleFrame', self.BubbleAnimSpeed, repeat= False)
		self.__increAnim('dashAnimCounter', len(self.dashRight), 'currentDashFrame', self.dashAnimSpeed, repeat= False)

		if self.isSquish:
			if self.left:
				win.blit(self.squishLeft[self.currentSquishFrame], (self.x, self.y))
			elif self.right:
				win.blit(self.squishRight[self.currentSquishFrame], (self.x, self.y))
			self.currentBubbleFrame = 0
			self.currentDashFrame = 0
		elif self.isBubbled:
			if self.left:
				win.blit(self.bubbleLeft[self.currentBubbleFrame], (self.x, self.y))
			elif self.right:
				win.blit(self.bubbleRight[self.currentBubbleFrame], (self.x, self.y))
			self.currentSquishFrame = 0
			self.currentDashFrame = 0
		elif self.isDash:
			if self.left:
				win.blit(self.dashLeft[self.currentDashFrame], (self.x, self.y))
			elif self.right:
				win.blit(self.dashRight[self.currentDashFrame], (self.x, self.y))
			self.currentBubbleFrame = 0
			self.currentSquishFrame = 0
		elif not(self.standing):
			if self.left:
				#win.blit(self.walkLeft[self.walkCount % len(self.walkRight)], (self.x, self.y))
				win.blit(self.walkLeft[self.currentWalkFrame], (self.x, self.y))
			elif self.right:
				#win.blit(self.walkRight[self.walkCount % len(self.walkLeft)], (self.x, self.y))
				win.blit(self.walkRight[self.currentWalkFrame], (self.x, self.y))
			self.currentBubbleFrame = 0
			self.currentSquishFrame = 0
			self.currentDashFrame = 0
		else:
			if self.right:
				#win.blit(self.idleRight[self.standCount % len(self.idleRight)], (self.x, self.y))
				win.blit(self.idleRight[self.currentIdleFrame], (self.x, self.y))
			else: 
				#win.blit(self.idleLeft[self.standCount % len(self.idleLeft)], (self.x, self.y))
				win.blit(self.idleLeft[self.currentIdleFrame], (self.x, self.y))
			self.currentBubbleFrame = 0
			self.currentSquishFrame = 0
			self.currentDashFrame = 0
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



