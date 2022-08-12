from importlib.resources import path
from tkinter.tix import Tree
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


pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)



game_map=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,9,1,1,0,1,1,0,1,1,1,0,1],
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
        self.initial_path = []
        self.chasing = False
        self.first_path = False
        self.start_time = 0
        self.limit = 0
        self.text = my_font.render(str(self.x // block_size) + " " + str(self.y // block_size), False, (0, 0, 0))
    
    def Random(self):
        empty_places = [] 
        index_i = (self.y + 32) // block_size
        index_j = (self.x + 32) // block_size
        start = [index_j, index_i]
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                if game_map[i][j] == 0:
                    empty_places.append([j, i])
        # # empty_places = [[1, 2], [2, 25], [23, 26], ... ]
        random_choice = random.choice(empty_places)
        if self.initial_path == [] and self.first_path == False:
            self.initial_path = djicstra(start, random_choice)
            self.first_path = True
        if self.initial_path == []:
            self.chasing = True
        elif time.time() - self.moved_time > 0.5:
            self.initial_path.pop()
            if self.initial_path != []:
                self.moved_time = time.time()
                if index_i < self.initial_path[-1][0]:
                    self.y += 64
                elif index_i > self.initial_path[-1][0]:
                    self.y -= 64
                elif index_j < self.initial_path[-1][-1]:
                    self.x += 64
                elif index_j > self.initial_path[-1][-1]:
                    self.x -= 64
        self.rect.x = self.x
        self.rect.y = self.y
        self.text = my_font.render(str(index_i) + " " + str(index_j), False, (0, 0, 0))
        self.text_path = my_font.render(str(self.initial_path[-1][0]) + " " + str(self.initial_path[-1][1]), False, (0, 0, 0))

    
    def update(self, x, y):
        global run
        index_i = (self.y + 32) // block_size
        index_j = (self.x + 32) // block_size
        start = [index_j, index_i]
        end = [x// block_size, y//block_size]
        if self.path == []:
            self.limit +=1
            self.path = djicstra(start, end)
        if self.path == []:
            run = False
        elif time.time() - self.moved_time > 0.5:
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
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.limit == 2:
            self.first_path = False
            self.chasing = False
            self.limit = 0

        self.text = my_font.render(str(index_i) + " " + str(index_j), False, (0, 0, 0))
        self.text_path = my_font.render(str(self.path[-1][0]) + " " + str(self.path[-1][1]), False, (0, 0, 0))

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
    if enemy3.chasing == False:
        enemy3.Random()
    else:
        enemy3.update(square_x, square_y)
    
    if enemy.chasing == False:
        enemy.Random()
    else:
        enemy.update(square_x, square_y)
    
    if enemy1.chasing == False:
        enemy1.Random()
    else:
        enemy1.update(square_x, square_y)

    if enemy2.chasing == False:
        enemy2.Random()
    else:
        enemy2.update(square_x, square_y)
    
    print(enemy2.chasing)

    
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
    for i in range(len(enemy_list)):
        npc = enemy_list[i]
        print(i, "-----" ,npc.path)
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
    pygame.draw.rect(screen, (0, 255, 255), (enemy.x, enemy.y, hero_long, hero_big))
    pygame.draw.rect(screen, (255,0,0), (enemy1.x, enemy1.y,hero_long, hero_big))
    pygame.draw.rect(screen,(0,0,255), (enemy2.x, enemy2.y, hero_long, hero_big))
    pygame.draw.rect(screen,(0,255,0), (enemy3.x, enemy3.y, hero_long, hero_big))
    for npc in enemy_list:
        screen.blit(npc.text, (npc.x, npc.y))
        screen.blit(npc.text_path, (npc.x, npc.y + 40))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()