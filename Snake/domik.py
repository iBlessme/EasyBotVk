import pygame
from pygame.locals import *

pygame.init() # инициализация модуля pygame

pygame.display.set_caption('Snake') # создание заголовка игры

screen = pygame.display.set_mode((800, 600)) # создание поверхности игры

clock = pygame.time.Clock() # создаем объект класса Clock()



sky = Rect(0, 0, 800, 300)
ground = Rect(0, 300, 800, 600)

pygame.draw.rect(screen, (30, 100, 200), sky)
pygame.draw.rect(screen, (39, 138, 34), ground)

square = Rect(300, 200, 200, 200)
pygame.draw.rect(screen, (132, 5, 15), square)

triangle = [[250, 200], [400, 50], [550, 200]]
pygame.draw.polygon(screen, (153, 14, 172), triangle)


pygame.draw.circle(screen, (255, 255, 0), (800, 0), 200)



play = True 

while play: # 
	for event in pygame.event.get(): # Цикл по всем событиям в игре
		if event.type == QUIT:       # Если мы нажали на крестик, то окно закроется
			play = False

	pygame.display.update() # обновляем поверхность игры
	clock.tick(60) # замедляем игру до 60 ФПС

