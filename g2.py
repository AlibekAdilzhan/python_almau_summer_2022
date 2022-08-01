import pygame
import random

pygame.init()
 
fps = 60
clock = pygame.time.Clock()
exit = False 

width, height = 720, 640
block_size = 64
speed = 3
width, height = 640, 480
random_warrior = [0,400]
warrior_number = [0] * 50
screen = pygame.display.set_mode((width, height))

hero_right = pygame.image.load("assets/conquestador.png")
block = pygame.image.load("assets/mario_block.png")
treasure = pygame.image.load("assets/treasure.jpg")
warrior = pygame.image.load("assets/warrior.png")

hero_right = pygame.transform.scale(hero_right, (block_size, block_size))
block = pygame.transform.scale(block, (block_size, block_size))
treasure = pygame.transform.scale(treasure, (block_size, block_size))
warrior = pygame.transform.scale(warrior, (block_size, block_size))

warriors = []

for i in range(warrior_number):
    warriors.appenr(warrior.copy())


hero_x = 50
hero_y = 100
run = True
while not exit:
    screen.fill((0, 150, 50))
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_RIGHT]:
        hero_x = hero_x + speed
    elif keystate[pygame.K_LEFT]:
        hero_x = hero_x - speed
    if ( keystate[pygame.K_UP]):
        hero_y -= speed
    elif (keystate[pygame.K_DOWN]):
        hero_y += speed
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    screen.blit(treasure, [250, 200])
    screen.blit(hero_right, [hero_x, hero_y])
    warrior_x = random.choice(random_warrior)
    warrior_y = random.choice(random_warrior)
    for i in range(len(warrior_number)):
        screen.blit(warrior, [warrior_x, warrior_y])

    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()