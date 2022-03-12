# coding: utf8
import pygame
import random

# задааем размер окна, создаем окно размера size
size = [400, 400]
window = pygame.display.set_mode(size)
# задаем имя - в кавычках, т.к. текст - это строка
pygame.display.set_caption('My second file')

screen = pygame.Surface(size)

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))


def Intersect(s1_x, s2_x, s1_y, s2_y):
    if ((s1_x>s2_x-40) and (s1_x<s2_x+40) and (s1_y>s2_y-40) and (s1_y<s2_y+40)):
        return 1
    else:
        return 0

# создание персонажей
# герой
hero = Sprite(200, 350, 'archer.png')
# переменные-"переключатели" движения для героя
hero.right = True
hero.up = True
# враг
enemy = Sprite(200, 10, 'dragon.png')
# переменные-"переключатели" движения для врага
enemy.right = True
enemy.up = False

running = True
while running:
    # обработка событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running  = False

    # задайте фоновый цвет
    screen.fill([23, 198, 93])

    # движение персонажей - аналогично тому,
    # что делали с квадратом, но теперь по вертикали
    if hero.up == True:
        hero.y -= 1
        if hero.y < 0:
            hero.up = False
    else:
        hero.y += 1
        if hero.y > 360:
            hero.up = True

    if enemy.up == True:
        enemy.y -= 1
        if enemy.y < 0:
            enemy.up = False
    else:
        enemy.y += 1
        if enemy.y > 360:
            enemy.up = True
    #enemy.x = random.randint(0, 400)
    #enemy.y = random.randint(0, 400)


    # столкновение персонажей
    if Intersect(hero.x, enemy.x, hero.y, enemy.y):
        hero.up = False
        enemy.up = True

    # отображение персонажей
    hero.render()
    enemy.render()

    # отображение окна
    window.blit(screen, [0, 0])
    pygame.display.flip()
    pygame.time.delay(50)


pygame.quit()