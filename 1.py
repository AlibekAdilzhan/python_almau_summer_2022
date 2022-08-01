import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
exit = False
 
# game settings
width, height = 720, 640
block_size = 64
speed_h = 5
speed_v = 0
gravity = 3
ground = 500
jump_height = 30
jump_is_allowed = False
camera_x = 3



game_map = [
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "............bbb....bbbb.............................................",
    "................................................................",
    "................................................................",
    "bbbbb bbbbbb bb  bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "................................................................"
]


screen = pygame.display.set_mode((width, height))

hero_right = pygame.image.load("assets/SnowMan1_right.png")
block = pygame.image.load("assets/mario_block.png")
hero_right = pygame.transform.scale(hero_right, (block_size, block_size))
block = pygame.transform.scale(block, (block_size, block_size))

hero_x = 50
hero_y = 100
hero_rect = pygame.Rect(hero_x, hero_y, block_size, block_size)

block_rects = [] 

for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == "b":
            block_rect = pygame.Rect(block_size * j + 35, block_size * i, block_size - 35, block_size)
            block_rects.append(block_rect)
            print(block_size * i, block_size * j, i, j)
# Game loop.
while not exit:
    screen.fill((0, 200, 255))
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_RIGHT]:
        hero_x = hero_x + speed_h
    elif keystate[pygame.K_LEFT]:
        hero_x = hero_x - speed_h
    if (keystate[pygame.K_SPACE] or keystate[pygame.K_UP]) and jump_is_allowed:
        speed_v -= 30
        jump_is_allowed = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
    speed_v += gravity
    hero_y = hero_y + speed_v
    hero_rect.x = hero_x
    hero_rect.y = hero_y
    if hero_x - camera_x > width * 0.75:
        camera_x += speed_h
    elif hero_x - camera_x < width * 0.25:
        camera_x -= speed_h

    # for i in range(len(game_map)):
        # for j in range(len(game_map[i])):
            # if game_map[i][j] == "b":
                # screen.blit(block, [block_size * j - camera_x, block_size * i])
    for rect in block_rects:
        screen.blit(block, [rect.x - camera_x, rect.y])
        
    for rect in block_rects:
        if hero_rect.colliderect(rect):
            hero_y = rect.y - block_size
            speed_v = 0
            jump_is_allowed = True

    screen.blit(hero_right, [hero_x - camera_x, hero_y])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()