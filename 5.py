game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
block_size = 64

square = pygame.image.load("красный квадрат.png")
square = pygame.transform.scale(square, (block_size, block_size))


width, height = 1280, 760
speed_h = 5
screen = pygame.display.set_mode((width, height))

run = True
hero_prev_x = 0
hero_prev_y = 0
hero_x = 64
hero_y = 64
switch = 0

hero2_x = 30
hero2_y = 45
switch = 0

hero_rect = pygame.Rect(hero_x, hero_y, block_size, block_size)

block_rects = []
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == 1:
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            block_rects.append(rect)

# Game loop.
while run:
    screen.fill((255, 255, 255))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    hero_prev_x = hero_x
    hero_prev_y = hero_y
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP] == True:
        hero_y = hero_y - 4
    if keystate[pygame.K_w] == True:
        hero_y = hero_y - 4
    if keystate[pygame.K_DOWN] == True:
        hero_y = hero_y + 4
    if keystate[pygame.K_s] == True:
        hero_y = hero_y + 4
    if keystate[pygame.K_RIGHT] == True:
        hero_x = hero_x + 4
    if keystate[pygame.K_d] == True:
        hero_x = hero_x + 3
    if keystate[pygame.K_LEFT] == True:
        hero_x = hero_x -4
    if keystate[pygame.K_LEFT] == True:
        hero_x = hero_x -5
    if keystate[pygame.K_a] == True:
        hero_x = hero_x -4
    if keystate[pygame.K_SPACE] == True:
        hero_x=3
    hero_rect.x = hero_x
    hero_rect.y = hero_y

    for rect in block_rects:
        if hero_rect.colliderect(rect):
            hero_x = hero_prev_x
            hero_y = hero_prev_y


    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (j * block_size, i * block_size, block_size, block_size))
    
    screen.blit(square, (hero_x, hero_y))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()