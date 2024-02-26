import pygame
pygame.init()

def Collision(kx, ky, ball, rect):
    if kx > 0:
        dx = ball.right - rect.left
    else:
        dx = rect.right - ball.left
    if ky > 0:
        dy = ball.bottom - rect.top
    else:
        dy = rect.bottom - ball.top

    if (dx - dy) < 5:
        kx, ky == -kx, -ky
    if dx > dy:
        ky *= -1
    if dy > dx:
        kx *= -1

    return kx, ky

width, height = 400, 550
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

text = pygame.font.SysFont('Century Gothic', 40, bold = False)

block = [pygame.Rect(50 * i, 50 + 50 * j, 50, 50) for i in range(8) for j in range(3)]
ColorBlock = [pygame.Color('blue') for i in range(8) for j in range(3)]
score, kolblock = 0, len(block)

player = pygame.Rect(150, 530, 100, 10)

R = 12
ball = pygame.Rect(190, 510, R, R)
kx, ky, life = 1, -1, 3

pusk, play, gameover, win = True, False, False, False

while True:
    sc.fill(pygame.Color('white'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and gameover == False and win == False:
            pusk, play = False, True

    if gameover == False and win == False:
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and player.right < width:
            player.x += 10

            if pusk == True:
                ball.x += 10
        if key[pygame.K_a] and player.left > 0:
            player.x -= 10

            if pusk == True:
                ball.x -= 10

    if play == True:
        ball.x += 4 * kx
        ball.y += 4 * ky

        if ball.x < R or ball.x > width - R:
            kx *= -1
        if ball.y - 50 < R:
            ky *= -1

        if ball.colliderect(player) and ky > 0:
            kx, ky = Collision(kx, ky, ball, player)

        destroy = ball.collidelist(block)
        if destroy != -1:
            destrect = block.pop(destroy)

            kx, ky = Collision(kx, ky, ball, destrect)

            score += 1


        if ball.y > height + R:
            play, pusk = False, True

            player.x, player.y = 150, 530
            ball.x, ball.y = 190, 510

            life -= 1

            if life <= 0:
                gameover = True

        if score == kolblock:
            play, win = False, True

    pygame.draw.aaline(sc, pygame.Color('black'), [0, 50], [width, 50])
    [pygame.draw.rect(sc, ColorBlock[color], i) for color, i in enumerate(block)]
    if gameover == False:
        pygame.draw.rect(sc, pygame.Color('black'), player)
        pygame.draw.circle(sc, pygame.Color('red'), ball.center, R)

    Tlife = text.render(f'Life: {life}', 1, pygame.Color('black'))
    sc.blit(Tlife, (15, 5))
    Tscore = text.render(f'Score: {score}/{kolblock}', 1, pygame.Color('black'))
    sc.blit(Tscore, (160, 5))
    if gameover == True:
        Tgameover = text.render('Game over!', 1, pygame.Color('RED'))
        sc.blit(Tgameover, (10, 200))
    elif win:
        Twin = text.render('You win!', 1, pygame.Color('Blue'))
        sc.blit(Twin, (10, 200))

    pygame.display.flip()
    clock.tick(60)