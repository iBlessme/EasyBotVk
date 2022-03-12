# coding: utf8
import pygame

# window
window = pygame.display.set_mode([400, 400])
pygame.display.set_caption('My first game')
screen = pygame.Surface([400, 400])

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

# герой
hero = Sprite(200, 350, 'archer.png')
hero.right = True
hero.up = True
# враг
enemy = Sprite(10, 10, 'dragon.png')
enemy.right = True
enemy.step = 1

weapon = Sprite(-100, -100, 'arrow.png')
weapon.push = False

running = True
pygame.key.set_repeat(1,1)
while running:
    # обработка событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running  = False
        # движение героя
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                if hero.x > 10:
                    hero.x -= 1
            if e.key == pygame.K_RIGHT:
                if hero.x < 350:
                    hero.x += 1
            if e.key == pygame.K_UP:
                if hero.y > 200:
                    hero.y -= 1
            if e.key == pygame.K_DOWN:
                if hero.y < 350:
                    hero.y += 1
            if e.key == pygame.K_SPACE:
                if weapon.push == False:
                    weapon.x = hero.x + 15
                    weapon.y = hero.y
                    weapon.push = True


    # задайте фоновый цвет
    screen.fill([23, 198, 93])

    if weapon.push == True:
        weapon.y -= 1
    else:
        weapon.x = -100
        weapon.y = -100
    if weapon.y < 0:
        weapon.push = False
    # движение врага
    if enemy.right == True:
        enemy.x += enemy.step
        if enemy.x > 360:
            enemy.right = False
    else:
        enemy.x -= enemy.step
        if enemy.x < 0:
            enemy.right = True

    if Intersect(weapon.x, enemy.x, weapon.y, enemy.y):
        weapon.push = False
        enemy.step += 0.2
    # отображение персонажей
    hero.render()
    enemy.render()
    weapon.render()

    # отображение окна
    window.blit(screen, [0, 0])
    pygame.display.flip()
    pygame.time.delay(5)

pygame.quit()