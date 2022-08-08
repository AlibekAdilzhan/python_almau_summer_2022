import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
block_size = 64

square = pygame.image.load("красный квадрат.png")
square = pygame.transform.scale(square, (block_size, block_size))

width, height = 640, 480
speed_h = 5
screen = pygame.display.set_mode((width, height))
run = True
hero_x = 50
hero_y = 100
switch = 0
# Game loop.
while run:
    
    if switch == 0:
        screen.fill((9, 35, 4))
    else:
        screen.fill((23, 84, 1))
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                switch = (switch + 1) % 2

    if keystate[pygame.K_UP] == True:
        hero_y = hero_y - 10
    if keystate[pygame.K_w] == True:
        hero_y = hero_y - 10
    if keystate[pygame.K_DOWN] == True:
        hero_y = hero_y + 10
    if keystate[pygame.K_s] == True:
        hero_y = hero_y + 10
    if keystate[pygame.K_RIGHT] == True:
        hero_x = hero_x + 10
    if keystate[pygame.K_d] == True:
        hero_x = hero_x + 10
    if keystate[pygame.K_LEFT] == True:
        hero_x = hero_x -10
    if keystate[pygame.K_LEFT] == True:
        hero_x = hero_x -10
    if keystate[pygame.K_a] == True:
        hero_x = hero_x -10
    if keystate[pygame.K_SPACE] == True:
        hero_x=10

    
    screen.blit(square, (hero_x, hero_y))
    pygame.display.flip()
    clock.tick(fps)


pygame.quit()