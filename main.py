import pygame
import sys
import random

pygame.init()
theClock = pygame.time.Clock()

display = pygame.display.set_mode((800, 500))
pygame.display.set_caption('NEON fly')

white = (255, 255, 255)
black = (255, 153, 51)
red = (255, 0, 0)

x_move = 700
y_move = 500

rand_height = random.randrange(150, 230, 1)
rand_height2 = random.randrange(-200, -130, 1)

x = 200
y = 100
x_player = 0
y_player = 0
accel_x = 0
accel_y = 0
max_speed = 5

levels = 3
max_speed_blocks = 8

score = 0
triangles = pygame.image.load('Triangles.png')
sprite = pygame.image.load('Sprite.png')

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                accel_x = -.2
            if event.key == pygame.K_RIGHT:
                accel_x = .2
            if event.key == pygame.K_UP:
                accel_y = -.2
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP):
                accel_x = 0
                accel_y = .2

    x_player += accel_x
    y_player += accel_y
    levels += 0.005
    score += 1

    if abs(x_player) >= max_speed:
        x_player = x_player / abs(x_player) * max_speed

    if abs(y_player) >= max_speed:
        y_player = y_player / abs(y_player) * max_speed


    if accel_x == 0:
        x_player *= 0.96
    if accel_y == 0:
        y_player *= 0.96

    x += x_player
    y += y_player

    display.fill(black)

    blockade = pygame.draw.rect(display, white, (int(x_move), 0, 40, rand_height))
    blockade2 = pygame.draw.rect(display, white, (int(x_move), y_move, 40, rand_height2))

    wall = pygame.draw.rect(display, black, (0, 0, 5, 500))
    wall2 = pygame.draw.rect(display, black, (0, 0, 800, 5))
    wall3 = pygame.draw.rect(display, black, (795, 0, 5, 500))
    wall4 = pygame.draw.rect(display, black, (0, 495, 800, 5))

    sprite_block = pygame.draw.rect(display, black, (int(x), int(y), 20, 60))

    if blockade.colliderect(wall):
        x_move = 820
        rand_height = random.randrange(130, 240, 1)
        rand_height2 = random.randrange(-200, -130, 1)

    else:
        x_move -= levels

    if sprite_block.colliderect(blockade) or sprite_block.colliderect(blockade2):
        sys.exit()

    if sprite_block.colliderect(wall):
        x_player += 20
    if sprite_block.colliderect(wall3):
        x_player -= 20

    if sprite_block.colliderect(wall2):
        y_player += 20
    if sprite_block.colliderect(wall4):
        sys.exit()

    x = round(int(x))
    x_move = round(int(x_move))

    score_calc = round(score / 60)

    score_font = pygame.font.SysFont('CourierBold', 40)
    text_score = score_font.render("Score = " + str(score_calc), True, red)
    scoreRect = text_score.get_rect()
    scoreRect.center = (700, 20)
    display.blit(text_score, scoreRect)
    display.blit(triangles, (x_move - 800, 439))
    display.blit(sprite, (int(x) - 40, int(y) - 10))

    pygame.display.update()
    theClock.tick(60)

pygame.quit()
