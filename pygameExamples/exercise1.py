import pygame


def draw(screen, wi, he):
    pygame.draw.line(screen, 'white', (0, 0), (wi, he), width=5)
    pygame.draw.line(screen, 'white', (wi, 0), (0, he), width=5)


if __name__ == '__main__':
    pygame.init()
    n = input().split()
    size = width, height = int(n[0]), int(n[1])
    screen = pygame.display.set_mode(size)
    draw(screen, width, height)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
