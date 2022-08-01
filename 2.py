import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
exit = False
 
# game settings
width, height = 720, 640
block_size = 64
speed_h = 2
speed_v = 2

screen = pygame.display.set_mode((width, height))

hero_right = pygame.image.load("assets/conquestador.png")
block = pygame.image.load("assets/mario_block.png")
hero_right = pygame.transform.scale(hero_right, (block_size, block_size))
block = pygame.transform.scale(block, (block_size, block_size))

hero_x = 50
hero_y = 100
run = True
# Game loop.
while not exit:
    screen.fill((0, 255, 50))
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_RIGHT]:
        hero_x = hero_x + speed_h
    elif keystate[pygame.K_LEFT]:
        hero_x = hero_x - speed_h
    if ( keystate[pygame.K_UP]):
        hero_y -= speed_v
    elif (keystate[pygame.K_DOWN]):
        hero_y += speed_v

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    screen.blit(hero_right, [hero_x, hero_y])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()