import pygame
import random
import sys

pygame.init()
# главные величины в игре
running = True
size = width, height = 900, 700
fps = 60
platform_speed = 10
# создание спрайтов
all_sprites = pygame.sprite.Group()
platform = pygame.sprite.Sprite()
platform.image = pygame.image.load('data/template.png')
platform.rect = platform.image.get_rect()
all_sprites.add(platform)
platform.rect.x = 350
platform.rect.y = 600
ball_radius = 10
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, width - ball_rect), height // 2,
                   ball_rect, ball_rect)
dx, dy = 1, -1  # переменные отвечающие за направление шарика
defence_all = [pygame.Rect(45 + 120 * i, 10 + 70 * j, 100, 50) for i in range(7) for j in range(5)]
defence_color = [(0, random.randrange(70, 120), 0) for i in range(7) for j in range(5)]


screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background = pygame.image.load('data/netrun.png').convert()
pygame.key.set_repeat(10, 10)

def start_screen():
    intro_text = ["HACKER ENVIRONMENT", "",
                  "ЦЕЛЬ:",
                  "Добейся полного удаления защиты,",
                  "старайся разбить все платформы.", "Для начала нажми пробел"]
    background_1 = pygame.image.load('data/watch.jpg').convert()
    screen.blit(background_1, (-500, -100))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

def balldetect(deltax, deltay, ball, rect):
    if deltax > 0:
        delx = ball.right - rect.left
    else:
        delx = rect.right - ball.left
    if deltay > 0:
        dely = ball.bottom - ball.top
    else:
        dely = rect.bottom - ball.top
    if abs(delx - dely) < 10:
        deltax, deltay = -deltax, -deltay
    elif delx > dely:
        deltay = -deltay
    elif dely > delx:
        deltax = - deltax
    return deltax, deltay

def bag(screen):
    for i in range(6000):
        screen.fill(pygame.Color('grey'),
                    (random.random() * width,
                     random.random() * height, 1, 1))


if __name__ == '__main__':
    while running:
        start_screen()
        screen.blit(background, (-300, -100))
        bag(screen)
        all_sprites.draw(screen)
        [pygame.draw.rect(screen, defence_color[i], j) for i, j in enumerate(defence_all)]
        pygame.display.set_caption('hacking the system')
        pygame.draw.circle(screen, pygame.Color('#18FFE1'), ball.center,
                           ball_radius)
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        if ball.centerx < ball_radius or ball.centerx > width - ball_radius:
            dx = -dx
        if ball.centery < ball_radius:
            dy = -dy
        if ball.colliderect(platform) and dy > 0:
            dx, dy = balldetect(dx, dy, ball, platform.rect)
        hits = ball.collidelist(defence_all)
        if hits != -1:
            hits_rect = defence_all.pop(hits)
            hit_color = defence_color.pop(hits)
            ball_speed += 0.3
            dx, dy = balldetect(dx, dy, ball, hits_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_d] and platform.rect.right < width:
                platform.rect.x += platform_speed
            if key[pygame.K_a] and platform.rect.left > 0:
                platform.rect.x -= platform_speed
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()