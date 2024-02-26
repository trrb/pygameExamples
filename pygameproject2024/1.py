import pygame
import random

pygame.init()
# главные величины в игре
size = width, height = 900, 650
fps = 60
platform_speed = 20
# создание спрайтов
all_sprites = pygame.sprite.Group()
platform = pygame.sprite.Sprite()
platform.image = pygame.image.load('data/cyberpunk_platform.png')
platform.rect = platform.image.get_rect()
all_sprites.add(platform)
platform.rect.x = 350
platform.rect.y = 550
ball_radius = 10
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, width - ball_rect), height // 2, ball_rect, ball_rect)
dx, dy = 1, -1 #переменные отвечающие за направление шарика
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background = pygame.image.load('data/fon.jpg').convert()

if __name__ == '__main__':
    while pygame.event.wait().type != pygame.QUIT:
        screen.blit(background, (-150, -500))
        all_sprites.draw(screen)
        pygame.draw.circle(screen, pygame.Color('#013220'), ball.center, ball_radius)
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        if ball.centerx < 20 or ball.centerx> width - 20:
            dx = -dx
        if ball.centery < 20:
            dy = -dy
        if ball.colliderect(platform) and dy > 0:
            dy = -dy
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and platform.rect.right < width:
            platform.rect.x += platform_speed
        if key[pygame.K_a] and platform.rect.left > 0:
            platform.rect.x -= platform_speed
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
