import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
stop = False
#это база
width, height = 1260, 840
block_size = 64
speed_h = 5
speed_v = 0
gravity = 3
ground = 500
camera_x = 3
block_rects = []
game_map = [
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "b..b...b...........................b",
    "b..b....b........................b",
    "b..b..b...b........................b",
    "b..b..b............................b",
    "b..b..b............................b",
    "b..b..b............................b",
    "b.....b............................b",
    "b.....b............................b",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
]

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
hero_rect = pygame.Rect(square_x, square_y, block_size, block_size)
camera_x = 0
# Game loop.
o = 0
while run:
    screen.fill((0, 100, 255))
    keystate = pygame.key.get_pressed()
    #хотьба
    if keystate[pygame.K_d]:
        square_x += 5
    elif keystate[pygame.K_a]:
        square_x -= 5
    elif keystate[pygame.K_w]:
        square_y -= 5
    elif keystate[pygame.K_s]:
        square_y += 5
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # хит бокс ироr
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
        if hero_rect.colliderect(block_rect):
            square_x = 100
            square_y = 100
    # делает карту
    # for i in range(len(game_map)):
    #     for j in range(len(game_map[i])):
    #         if game_map[i][j] == "b":
                # block_rect = pygame.Rect(block_size * j + 35, block_size * i, block_size - 35, block_size)
                # screen.blit(block, (j * block_size, i * block_size))
    pygame.draw.rect(screen, (255, 255, 255), (square_x - camera_x, square_y, 10, 10))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()