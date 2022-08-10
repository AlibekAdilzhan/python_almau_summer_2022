import time


game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
block_size = 64

square = pygame.image.load("красный квадрат.png")
square = pygame.transform.scale(square, (60, 60))
TreugolnikS= pygame.image.load("синий треугольник.png")
TreugolnikS= pygame.transform.scale(TreugolnikS, (60, 60))
Romb= pygame.image.load("желтый ромб.png")
Romb= pygame.transform.scale(Romb, (60, 60))

width, height = 1280, 760
speed_h = 5
screen = pygame.display.set_mode((width, height))

run = True

hero_prev_x = 0
hero_prev_y = 0
hero_x = 64
hero_y = 64
switch = 0

class Enemy:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
        self.prev_x=x
        self.prev_y=y
        self.rect = pygame.Rect(x, y, block_size, block_size)
        self.changed = False
        self.changed_time = 0


    def update(self):
        if self.changed:
            if time.time() - self.changed_time > 5:
                self.changed = False
        v = [self.x - hero_x, self.y - hero_y]
        self.prev_x = self.x
        self.prev_y = self.y
        if v[0] > 0:
            self.x=self.x+1
        if v[0]<0:
            self.x=self.x-1
        if v[0]>0:
            self.y=self.y+1
        if v[0]<0:
            self.y=self.y-1
        self.rect.x = self.x
        self.rect.y = self.y

hero_rect = pygame.Rect(hero_x+15, hero_y+15, 55, 55)
t = Enemy(256,256)
block_rects = []
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == 1:
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            block_rects.append(rect)



    def update(self):
        if self.changed:
            if time.time() - self.changed_time > 5:
                self.changed = False
        v = [self.x - hero_x, self.y - hero_y]
        self.prev_x = self.x
        self.prev_y = self.y
        if v[0] > 0:
            self.x=self.x+1
        if v[0]<0:
            self.x=self.x-1
        if v[0]>0:
            self.y=self.y+1
        if v[0]<0:
            self.y=self.y-1
        self.rect.x = self.x
        self.rect.y = self.y

z = Enemy(233, 85)
block_rects = []
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == 1:
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            block_rects.append(rect)


            

t_rect = pygame.Rect(t.x+15, t.y+15, 55, 55)
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

    for rect in block_rects:
        if t.rect.colliderect(rect):
            t.x = t.prev_x
            t.y = t.prev_y
    
    if hero_rect.colliderect(t.rect):
        hero_x=hero_prev_x
        hero_y = hero_prev_y
        

    if hero_rect.colliderect(t.rect) and t.changed == False:
        # t.y, hero_y = hero_y, t.y
        # t.x, hero_x = hero_x, t.x
        # hero_rect = t_rect
        square, TreugolnikS = TreugolnikS, square
        t.changed = True
        t.changed_time = time.time()
        
    
    
    t.update()
    screen.blit(square, (hero_x, hero_y))
    screen.blit(TreugolnikS, (t.x, t.y))
    screen.blit(Romb,(z.x, z.y))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()