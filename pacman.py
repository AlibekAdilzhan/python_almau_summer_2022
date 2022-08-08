import pygame
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
    [1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
fps = 60
clock = pygame.time.Clock()
width, height = 1280, 960
screen = pygame.display.set_mode((width, height))
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == 1:
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            block_rects.append(rect)
run = True
# Game loop.
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def update(self):
        self.x -= 4 


enemy = Enemy(512, 512)
prev_x = 0
prev_y = 0
while run:
    screen.fill((0, 0, 0))
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == 1:
                pygame.draw.rect(screen, (100, 255, 255), (j * block_size , i * block_size, hero_long, hero_big))
    
    prev_x = square_x
    prev_y = square_y
    prev1_x = enemy_x
    prev1_y = enemy_y
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
    enemy_rect = pygame.Rect(enemy_x, enemy_y, hero_big, hero_long)
    enemy_rect.x = enemy_x
    enemy_rect.y = enemy_y
    hero_rect = pygame.Rect(square_x, square_y, hero_big, hero_long)
    hero_rect.x=square_x
    hero_rect.y=square_y
    for block_rect in block_rects:
        if enemy_rect.colliderect(block_rect):
            enemy_x = prev1_x
            enemy_y = prev1_y
    for block_rect in block_rects:
        if hero_rect.colliderect(block_rect):
            square_x = prev_x
            square_y = prev_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    enemy.update()
    pygame.draw.rect(screen, (255, 255, 255), (square_x , square_y, hero_long, hero_big))
    pygame.draw.rect(screen, (0, 0, 255), (enemy.x, enemy.y, hero_long, hero_big))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()