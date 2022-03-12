# coding: utf8
import pygame

# задаем размер окна, создаем окно размера size
size = [400, 400]
window = pygame.display.set_mode(size)
# задаем имя - в кавычках, т.к. текст - это строка
pygame.display.set_caption('Hello world!')

screen = pygame.Surface(size)

# создание объекта - квадрат - размера 40х40
square = pygame.Surface([40, 40])
# закрашиваем квадрат. цвет задается тремя числами 0-255, по системе RGB
square.fill([255, 255, 255])

right_free = True
# переменныя для координат х и у квадрата
x = 0
y = 0

running = True
while running:
    # обработка событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running  = False

    # закрашиваем фон
    screen.fill([23, 198, 93])

    # движение квадрата
    # условия для того, чтобы он не уходил за пределы окна.
    if right_free == True:
        x += 1
        y += 1
        if x > 360:
            right_free = False
    else:
        x -= 1
        y -= 1
        if x < 0:
            right_free = True

    # отображение квадрата
    screen.blit(square, [x, 0])

    # отображение окна
    window.blit(screen, [0, 0])
    pygame.display.flip()
    pygame.time.delay(5)


pygame.quit()