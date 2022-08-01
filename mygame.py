from turtle import speed
import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
exit = False

#game settings
rdegree = 0
degree = 0
width, height = 800, 800
block_size = 80
speed_x = 90
speed_y = 0
camera_x = 3
camera_y = 3

screen = pygame.display.set_mode((width, height))

car = pygame.image.load("assets/mytank.png")
tree = pygame.image.load("assets/tree.png")
car = pygame.transform.scale(car, (block_size, block_size))
tree = pygame.transform.scale(tree, (block_size, block_size))

hero_x = 50
hero_y = 50
hero_rect = pygame.Rect(hero_x, hero_y, block_size, block_size)

block_rects = [] 

# Game loop.
while not exit:
    screen.fill((0, 200, 255))
    keystate = pygame.key.get_pressed()

    while keystate[pygame.K_RIGHT]:
        degree += 1
        if degree > 360:
            degree = 0
        rdegree += degree
    while keystate[pygame.K_LEFT]:
        degree -= 1

    if keystate[pygame.K_UP]:
        hero_x = hero_x + speed_x
        hero_y = hero_y + speed_y
    elif keystate[pygame.K_DOWN]:
        hero_x = hero_x - speed_x
        hero_y = hero_y - speed_y
    

    image = pygame.transform.rotate(car, rdegree)
    if rdegree =< 90:
        for i in range(len(rdegree)):
            speed_x -= 1
            speed_y += 1
    elif rdegree >= 90:
        for i in range(len(rdegree)):
            speed_x -= 1
            speed_y += 1
        for i in range(len(rdegree) - 90):
            speed_x += 1
            speed_y -= 1
    elif rdegree >= 180:
        for i in range(len(rdegree) - 180):


    pygame.display.flip()
    clock.tick(fps)

pygame.quit()