import pygame

class Player(object):
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



