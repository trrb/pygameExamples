import pygame


def draw(screen, wi, he):
    screen.fill((255, 0, 0), pygame.Rect(1, 1, wi - 2, he - 2))


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
