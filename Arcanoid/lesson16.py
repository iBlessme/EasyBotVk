import pygame as pg
from pygame.locals import *

BALLSPEED = 10
BLOCKWIDTH = 75
BLOCKHEIGHT = 30

class Block(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.size = [BLOCKWIDTH, BLOCKHEIGHT]
		self.image = pg.Surface(self.size)
		self.image.fill((255, 0, 255))
		self.rect = self.image.get_rect()
		self.name = 'BLOCK'

class Ball(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((15, 15))
		self.image.fill((0, 255, 0))
		self.rect = self.image.get_rect(center=(400, 580))
		self.score = 0
		self.isMoving = True
		self.speedx = BALLSPEED
		self.speedy = BALLSPEED * -1
		self.bounce = pg.mixer.Sound('bounce.wav')
		self.point = pg.mixer.Sound('goal.wav')
		self.lose = pg.mixer.Sound('lose.wav')

	def update(self, keys, platform, blocks, *args):
		if self.isMoving:
			self.rect.y += self.speedy

			hitGroup = pg.sprite.Group(platform, blocks)

			spriteHitList = pg.sprite.spritecollide(self, hitGroup, False)

			if len(spriteHitList) > 0:
				for sprite in spriteHitList:
					if sprite.name == 'BLOCK':
						sprite.kill()
						self.point.play()
						self.speedy *= -1
						self.score += 1
						self.rect.y += self.speedy
					elif sprite.name == 'PLATFORM':
						self.speedy *= -1
						self.bounce.play()
					
					

			self.rect.x += self.speedx

			if self.rect.right > 800:
				self.speedx *= -1
				self.rect.right = 800
				self.bounce.play()
			if self.rect.left < 0:
				self.speedx *= -1
				self.rect.left = 0
				self.bounce.play()

			if self.rect.top < 0:
				self.speedy *= -1
				self.rect.top = 0
				self.bounce.play()

			if self.rect.bottom > 600:
				self.isMoving = False
				self.lose.play()
class Platform(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface( (200, 10) )
		self.rect = self.image.get_rect(center=(400, 590))
		self.image.fill( (255, 150, 0) )
		self.name = 'PLATFORM'
	def update(self, keys, *args):
		if keys[K_a] and self.rect.x > 0:
			self.rect.x -= 15
		if keys[K_d] and self.rect.x < 740:
			self.rect.x += 15



class Game:
	def __init__(self):
		self.score = 0
		self.game_over = 0

		 

		self.sprites = pg.sprite.Group()
		self.platform = Platform()
		self.ball = Ball()
		self.sprites.add(self.platform)
		self.sprites.add(self.ball)
		self.blocks = pg.sprite.Group()
		self.font = pg.font.Font(None, 32)
		for row in range(5):
			for col in range(10):
				block = Block()
				block.rect.x = col * (BLOCKWIDTH + 7)
				block.rect.y = row * (BLOCKHEIGHT +7)
				self.blocks.add(block)

		self.sprites.add(self.blocks)

	def process_events(self):
		for event in pg.event.get():
			if event.type == QUIT:
				return True
			if event.type == MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()

	def run_logic(self):
		pass

	def display_frame(self, screen, keys):
		screen.fill( (0, 0, 0) )
		score = self.font.render('Score:  ' + str(self.ball.score), 1, (255, 255, 255))
		screen.blit(score, [20 , 550])
		self.sprites.update(keys, self.platform, self.blocks)
		self.sprites.draw(screen)

		if self.ball.isMoving == False:
			self.__init__()


def main():
	pg.init()
 
	pg.display.set_caption("Arcanoid")
	screen = pg.display.set_mode((800, 600))
 
	endgame = False
	clock = pg.time.Clock()
 
	game = Game()
 
	while not endgame:

		endgame = game.process_events()
		game.run_logic()
		keys = pg.key.get_pressed()
		game.display_frame(screen, keys)

		pg.display.update()
		clock.tick(60)
 
if __name__ == "__main__":
	main()




