import pygame
import time
import random
from copy import deepcopy
block = 64
square_x = 64
square_y = 64
hero_big = 64
hero_long = 64
block_size = 64
block_rects = []
enemy_x = 512
enemy_y = 512


game_map=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
fps = 60
clock = pygame.time.Clock()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == 1:
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            block_rects.append(rect)
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 64
        self.rect = pygame.Rect(self.x, self.y, hero_long, hero_big)
        self.moved_time = time.time()
        self.path = []
    
    def Random(self,x,y):
        empty_places = []
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                if game_map[i][j] == 0:
                    empty_places.append([i, j])
                    random_choice = random.choice(empty_places)
        self.x = random_choice[-1]
        self.y = random_choice[0]

    def update(self, x, y):
        global run
        index_i = self.y // block_size
        index_j = self.x // block_size
        start = [self.x // block_size ,self.y // block_size]
        end = [x// block_size, y//block_size]
        self.rect = (self.x,self.y,hero_long,hero_big)
        if self.path == []:
            self.path = djicstra(start, end)
        if self.path == []:
            run = False
        elif time.time() - self.moved_time > 0.5:
            print(self.path)
            self.path.pop()
            if self.path != []:
                self.moved_time = time.time()
                if index_i < self.path[-1][0]:
                    self.y+=64
                elif index_i > self.path[-1][0]:
                    self.y -=64
                elif index_j < self.path[-1][-1]:
                    self.x +=64
                elif index_j > self.path[-1][-1]:
                    self.x -=64



def djicstra(start, end):
    if start != end:
        start = [start[1], start[0]]
        end = [end[1], end[0]]
        queue = [start]

        game_map_copy = deepcopy(game_map)

        game_map_copy[start[0]][start[1]] = 2

        while True:
            current = queue[0]
            cx = current[0]
            cy = current[1]
            if game_map_copy[cx][cy - 1] == 0:
                queue.append([cx, cy - 1])
                game_map_copy[cx][cy - 1] = game_map_copy[cx][cy] + 1
            if game_map_copy[cx][cy + 1] == 0:
                queue.append([cx, cy + 1])
                game_map_copy[cx][cy + 1] = game_map_copy[cx][cy] + 1
            if game_map_copy[cx + 1][cy] == 0:
                queue.append([cx + 1, cy])
                game_map_copy[cx + 1][cy] = game_map_copy[cx][cy] + 1
            if game_map_copy[cx - 1][cy] == 0:
                queue.append([cx - 1, cy])
                game_map_copy[cx - 1][cy] = game_map_copy[cx][cy] + 1
            queue.pop(0)
            if game_map_copy[end[0]][end[1]] != 0:
                break

        path = [end]
        current = end
        while True:
            x = current[0]
            y = current[1]
            number = game_map_copy[x][y]
            if game_map_copy[x - 1][y] == number - 1:
                path.append((x - 1, y))
                current = [x - 1, y]
            elif game_map_copy[x + 1][y] == number - 1:
                path.append((x + 1, y))
                current = [x + 1, y]
            elif game_map_copy[x][y + 1] == number - 1:
                path.append((x, y + 1))
                current = [x, y + 1]
            elif game_map_copy[x][y - 1] == number - 1:
                path.append((x, y - 1))
                current = [x, y - 1]
            if current == start:
                break
        return path
    else:
        path = []
        return path

run = True
enemy = Enemy(512, 512)
enemy1 = Enemy(512, 512)
enemy2 = Enemy(512, 512)
enemy3 = Enemy(512, 512)
enemy_list = [enemy,enemy1,enemy2,enemy3]
prev_x = 0
prev_y = 0
while run:
    screen.fill((0, 0, 0))
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == 1:
                pygame.draw.rect(screen, (100, 255, 255), (j * block_size , i * block_size, hero_long, hero_big))
    enemy.update(square_x, square_y)
    enemy1.update(square_x, square_y)
    
    prev_x = square_x
    prev_y = square_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                square_y -= 64
            if event.key == pygame.K_s:
                square_y += 64
            if event.key == pygame.K_a:
                square_x -= 64
            if event.key == pygame.K_d:
                square_x += 64

    hero_rect = pygame.Rect(square_x, square_y, hero_big, hero_long)
    hero_rect.x=square_x
    hero_rect.y=square_y
    if hero_rect.collidelistall(enemy_list):
        run = False
    for block_rect in block_rects:
        if hero_rect.colliderect(block_rect):
            square_x = prev_x
            square_y = prev_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(screen, (255, 255, 255), (square_x , square_y, hero_long, hero_big))
    pygame.draw.rect(screen, (0, 0, 0), (enemy.x, enemy.y, hero_long, hero_big))
    pygame.draw.rect(screen, (255,0,0), (enemy1.x, enemy1.y,hero_long, hero_big))
    pygame.draw.rect(screen,(0,0,255), (enemy2.x, enemy2.y, hero_long, hero_big))
    pygame.draw.rect(screen,(0,255,0), (enemy3.x, enemy3.y, hero_long, hero_big))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()