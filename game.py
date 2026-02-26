import pygame
pygame.init()
winx = 3840
winy = 2160
win = pygame.display.set_mode((winx,winy))
font = pygame.font.SysFont(None, 120)


pygame.display.set_caption("Firstgame")

width = 40
height = 60
x1 = 0
y1 = 0
x2 = winx - width
y2 = winy - height
vel1 = 5
vel2 = 5

isJump1 = False
jumpCount1 = 10
isJump2 = False
jumpCount2 = 10
speed_time1 = None
speed_time2 = None

speler1_rect = (x1, y1, width, height)
speler2_rect = (x2, y2, width, height)
obstakel1_rect = (100, 1030, 3640, 100)

#mainloop
run = True
while run:
    pygame.time.delay(8)
    tijd_ms = pygame.time.get_ticks()
    tijd_s = tijd_ms / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #1e

    #toetsen
    if keys[pygame.K_a] and x1 > vel1:
        player1_rect = pygame.Rect(x1, y1, width, height)
        if player1_rect.colliderect(obstakel1_rect):
            x1 += vel1 * 2
        if not player1_rect.colliderect(obstakel1_rect):
            x1 -= vel1
    if keys[pygame.K_d] and x1 < winx - width - vel1:
        player1_rect = pygame.Rect(x1, y1, width, height)
        if player1_rect.colliderect(obstakel1_rect):
            x1 -= vel1 * 2
        if not player1_rect.colliderect(obstakel1_rect):
            x1 += vel1
    if keys[pygame.K_w] and y1 > vel1:
        player1_rect = pygame.Rect(x1, y1, width, height)
        if player1_rect.colliderect(obstakel1_rect):
            y1 += vel1 * 2
        if not player1_rect.colliderect(obstakel1_rect):
            y1 -= vel1
    if keys[pygame.K_s] and y1 < winy - height - vel1:
        player1_rect = pygame.Rect(x1, y1, width, height)
        if player1_rect.colliderect(obstakel1_rect):
            y1 -= vel1 * 2
        if not player1_rect.colliderect(obstakel1_rect):
            y1 += vel1

    #speed boost
    if keys[pygame.K_LSHIFT]:
        if speed_time1 is None:
            speed_time1 = pygame.time.get_ticks()
            vel1 *= 2
    time_check1 = pygame.time.get_ticks()
    if speed_time1 is not None:
        if time_check1 - speed_time1 >= 3000:
            speed_time1 = None
            vel1 = 5

    #jump
    if not isJump1:
        if keys[pygame.K_SPACE]:
            isJump1 = True
    else:
        beginx = x1
        if jumpCount1 >= -10:
            neg = 1
            if jumpCount1 < 0:
                neg = -1
            y1 -= (jumpCount1 ** 2) * 0.5 * neg
            jumpCount1 -= 1
        else:
            isJump1 = False
            jumpCount1 = 10

    #2e

    #toetsen
    if keys[pygame.K_LEFT] and x2 > vel2:
        player1_rect = pygame.Rect(x2, y2, width, height)
        if not player1_rect.colliderect(obstakel1_rect):
            x2 -= vel2
    if keys[pygame.K_RIGHT] and x2 < winx - width - vel2:
        player1_rect = pygame.Rect(x1, y1, width, height)
        if not player1_rect.colliderect(obstakel1_rect):
            x2 += vel2
    if keys[pygame.K_UP] and y2 > vel2:
        player1_rect = pygame.Rect(x1, y1, width, height)
        if not player1_rect.colliderect(obstakel1_rect):
            y2 -= vel2
    if keys[pygame.K_DOWN] and y2 < winy - height - vel2:
        player1_rect = pygame.Rect(x1, y1, width, height)
        if not player1_rect.colliderect(obstakel1_rect):
            y2 += vel2

    #speed boost
    if keys[pygame.K_KP_PERIOD]:
        if speed_time2 is None:
            speed_time2 = pygame.time.get_ticks()
            vel2 *= 2
    time_check2 = pygame.time.get_ticks()
    if speed_time2 is not None:
        if time_check2 - speed_time2 >= 3000:
            speed_time2 = None
            vel2 = 5

    #jump
    if not isJump2:
        if keys[pygame.K_KP0]:
            isJump2 = True
    else:
        beginx = x2
        if jumpCount2 >= -10:
            neg = 1
            if jumpCount2 < 0:
                neg = -1
            y2 -= (jumpCount2 ** 2) * 0.5 * neg
            jumpCount2 -= 1
        else:
            isJump2 = False
            jumpCount2 = 10

    #achtergrond kleur
    win.fill((74, 73, 74))

    #tijd meter
    tijd = font.render(f"Time: {tijd_s}", True, (255, 255, 255))
    win.blit(tijd, (winx-500, 0))

    #speler 1
    pygame.draw.rect(win, (255, 0, 0), (x1, y1, width, height))

    #speler 2
    pygame.draw.rect(win, (160, 89, 186), (x2, y2, width, height))

    #obstakel
    pygame.draw.rect(win, (255, 255, 255), (100, 1030, 3640, 100))

    #update scherm
    pygame.display.update()

pygame.quit()
