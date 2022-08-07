import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
stop = False
#это база
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        

width, height = 1260, 840
block_size = 64
speed_h = 5
speed_v = 0
gravity = 3
ground = 500
camera_x = 3
block_rects = []
hero_long = 30
hero_big = 30
game_map = [
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "b....b...b.........................b",
    "b.bb...b...........................b",
    "b.bb.b....b........................b",
    "b......b...........................b",
    "b.bbb..............................b",
    "b.bb..b.b..........................b",
    "b.b..b..b..........................b",
    "b.....b............................b",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
]

game_map_bin = []
for i in range(len(game_map)):
    line = []
    for j in range(len(game_map[i])):
        if game_map[i][j] == ".":
            line.append(0)
        elif game_map[i][j] == "b":
            line.append(1)
    game_map_bin.append(line.copy())

for i in range(len(game_map_bin)):
    print(game_map_bin[i])

screen = pygame.display.set_mode((width, height))
block = pygame.image.load("assets/mario_block.png")
block = pygame.transform.scale(block, (block_size, block_size))
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == "b":
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            block_rects.append(rect)

run = True
square_x = 150
square_y = 150
enemy_x = 500
enemy_y = 500
enemy_rect = pygame.Rect(enemy_x, enemy_y, hero_big, hero_long)
hero_rect = pygame.Rect(square_x, square_y, hero_big, hero_long)
camera_x = 0
# Game loop.
o = 0
while run:
    screen.fill((0, 100, 255))
    keystate = pygame.key.get_pressed()
    #ии
    current = queue[0]
    cx = current[0]
    cy = current[1]
    if game_map[cx][cy - 1] == 0:
        queue.append([cx, cy - 1])
        game_map[cx][cy - 1] = game_map[cx][cy] + 1
    if game_map[cx][cy + 1] == 0:
        queue.append([cx, cy + 1])
        game_map[cx][cy + 1] = game_map[cx][cy] + 1
    if game_map[cx + 1][cy] == 0:
        queue.append([cx + 1, cy])
        game_map[cx + 1][cy] = game_map[cx][cy] + 1
    if game_map[cx - 1][cy] == 0:
        queue.append([cx - 1, cy])
        game_map[cx - 1][cy] = game_map[cx][cy] + 1
    queue.pop(0)
    if queue == []:
        break
    #хотьба
    if keystate[pygame.K_d]:
        square_x += 5
    elif keystate[pygame.K_a]:
        square_x -= 5
    elif keystate[pygame.K_w]:
        square_y -= 5
    elif keystate[pygame.K_s]:
        square_y += 5
    
    #выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # хит бокс игрок
    hero_rect.x=square_x
    hero_rect.y=square_y
    #камира
    if square_x - camera_x > width * 0.75:
        camera_x += speed_h
    elif square_x - camera_x < width * 0.25:
        camera_x -= speed_h
    # конфликт
    for block_rect in block_rects:
        screen.blit(block, (block_rect.x - camera_x, block_rect.y))
        pygame.draw.circle(screen, (0, 0, 0), (block_rect.x - camera_x, block_rect.y), 3)
        if hero_rect.colliderect(block_rect):
            square_x = 75
            square_y = 75
    # делает карту
    # for i in range(len(game_map)):
    #     for j in range(len(game_map[i])):
    #         if game_map[i][j] == "b":
                # block_rect = pygame.Rect(block_size * j + 35, block_size * i, block_size - 35, block_size)
                # screen.blit(block, (j * block_size, i * block_size))
    # игрок
    pygame.draw.rect(screen, (255, 255, 255), (square_x - camera_x, square_y, hero_long, hero_big))
    # противник
    pygame.draw.rect(screen, (0, 255, 0),(enemy_x - camera_x, enemy_y, hero_long, hero_big))
    pygame.draw.circle(screen, (255, 255, 0), (hero_rect.x - camera_x, hero_rect.y), 3)
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()