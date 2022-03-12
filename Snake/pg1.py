import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.display.set_caption('First game')
screen = pygame.display.set_mode( (800, 600) )

clock = pygame.time.Clock()

r1 = Rect(100, 100, 200, 100)
r2 = Rect(400, 300, 400, 400)

pygame.draw.rect(screen, (0, 255, 0), r1)
pygame.draw.rect(screen, (255, 0, 0), r2)

pygame.draw.circle(screen, (255, 255, 0), (400, 300), 200)

pygame.draw.polygon(screen, (30, 140, 200), ((200, 100), (400, 100), (300, 200)))

pygame.draw.arc(screen, (200, 100, 20), r1, 0, 6.28, 40)

while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	clock.tick(30)
