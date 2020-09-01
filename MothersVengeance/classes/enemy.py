import pygame

class Enemy(object):
	def __init__(self, x, y, width, height, end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x, self.end]
		self.walkCount = 0
		self.vel = 3
		self.walkRight = [pygame.image.load('./imgs/R1E.png'), pygame.image.load('./imgs/R2E.png'), pygame.image.load('./imgs/R3E.png'), pygame.image.load('./imgs/R4E.png'), pygame.image.load('./imgs/R5E.png'), pygame.image.load('./imgs/R6E.png'), pygame.image.load('./imgs/R7E.png'), pygame.image.load('./imgs/R8E.png'), pygame.image.load('./imgs/R9E.png'), pygame.image.load('./imgs/R10E.png'), pygame.image.load('./imgs/R11E.png')]
		self.walkLeft = [pygame.image.load('./imgs/L1E.png'), pygame.image.load('./imgs/L2E.png'), pygame.image.load('./imgs/L3E.png'), pygame.image.load('./imgs/L4E.png'), pygame.image.load('./imgs/L5E.png'), pygame.image.load('./imgs/L6E.png'), pygame.image.load('./imgs/L7E.png'), pygame.image.load('./imgs/L8E.png'), pygame.image.load('./imgs/L9E.png'), pygame.image.load('./imgs/L10E.png'), pygame.image.load('./imgs/L11E.png')]
		self.hitbox = (self.x + 12, self.y, self.width - 20, self.height)
		self.health = 10
		self.visible = True
		self.healthbar_width = 50
		self.healthbar_height = 10

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
			pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, self.healthbar_width, self.healthbar_height), 0)
			pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, self.health * (self.healthbar_width/10), self.healthbar_height), 0)
			self.hitbox = (self.x + 12, self.y, self.width - 20, self.height)
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


	def hit(self, score):
		if self.health > 0:
			self.health -= 1
			score += 1
			pygame.mixer.Channel(1).play(pygame.mixer.Sound('./sounds/hit.wav'))

		if self.health == 0:
			self.visible = False
		print('GOBLIN HIT...')
		return score

