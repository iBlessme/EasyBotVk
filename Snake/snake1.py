import pygame 
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode( (800, 600) )
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

SPEED = 10
# head = Rect(400, 300, 30, 30)
DIRECTION = [SPEED, 0]
COLOR = (255, 255, 255)
GAME_POINTS = 0

def load_image(src, x, y):
	image = pygame.image.load(src).convert()
	image = pygame.transform.scale(image, (30, 30))
	rect = image.get_rect(center=(x, y))

	transparent = image.get_at((0,0))
	image.set_colorkey(transparent)

	return image, rect

def random_color():
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	return (r, g, b)

def move(head):
	global DIRECTION, KEYS, SPEED, COLOR

	if KEYS[K_UP]:
		DIRECTION = [0, -SPEED] 
	elif KEYS[K_DOWN]:
		DIRECTION = [0, SPEED] 
	elif KEYS[K_RIGHT]:
		DIRECTION = [SPEED, 0] 
	elif KEYS[K_LEFT]:
		DIRECTION = [-SPEED, 0] 


	if head.bottom > 600:
		 head.top = 0

	elif head.top < 0:
		head.bottom = 600

	elif head.left < 0:
		head.right = 800

	elif head.right > 800:
		head.left = 0


	head.move_ip( DIRECTION )


def pickup():
	global apple_rect, head_rect, GAME_POINTS

	if head_rect.colliderect(apple_rect):
		apple_rect.x = randint(40, 760)
		apple_rect.y = randint(40, 560)
		GAME_POINTS += 10
		print(f'GAME_POINTS: {GAME_POINTS}')

head_image, head_rect = load_image('head.png', 400, 300)
apple_image, apple_rect = load_image('apple.png', 200, 300)


def score():
	global GAME_POINTS
	text = font.render(f'Score: {GAME_POINTS}', True, (255, 255, 255))
	text_rect = text.get_rect(center=(400, 500))
	screen.blit(text, text_rect)

while 1:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

	# pygame.draw.rect(screen, COLOR, head)

	screen.blit(head_image, head_rect)
	screen.blit(apple_image, apple_rect)

	KEYS = pygame.key.get_pressed()

	move(head_rect)
	pickup()
	score()
	
	pygame.display.update()
	clock.tick(30)



