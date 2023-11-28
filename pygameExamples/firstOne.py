import pygame
import random


def draw(screen):
    screen.fill('#ffcc00')
    for i in range(15000):
        screen.fill(pygame.Color('black'),
                    (random.random() * width,
                     random.random() * height, 1, 1))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, '#65000b')
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, '#65000b', (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    # ...
    # ...
    # смена (отрисовка) кадра:
    draw(screen)
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:

        pass
    # завершение работы:
    pygame.quit()

