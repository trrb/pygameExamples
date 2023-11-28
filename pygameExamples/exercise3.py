import pygame


def draw(screen, size, count):
    size = size // count
    screen.fill('white')
    for i in range(count):
        for j in range(i % 2, count, 2):
            pygame.draw.rect(screen, (0, 0, 0),
                             (j * size, i * size, size, size))


if __name__ == '__main__':
    pygame.init()
    n = input().split()
    size = int(n[0])
    count = int(n[1])
    size_screen = size, size
    screen = pygame.display.set_mode(size_screen)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
        draw(screen, size, count)
        pygame.display.update()
    pygame.quit()
