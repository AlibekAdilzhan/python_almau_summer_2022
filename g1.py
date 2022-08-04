import pygame
 

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 50
        self.image = bullet_image

    def update(self):
        self.x = self.x + self.speed


class Weapon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = weapon_image
        self.bullets = []

    def update(self):
        if keystate[pygame.K_q]:
            self.shoot()
        for bullet in self.bullets:
            bullet.update()
            screen.blit(bullet.image, (bullet.x - camera_x, bullet.y))
            if bullet.x - camera_x > width + 100:
                del bullet

    def shoot(self):
        self.bullets.append(Bullet(self.x, self.y))

    


pygame.init()

fps = 60
clock = pygame.time.Clock()

run = True

# game settings
block_size = 64
speed_h = 5
speed_v = 0
gravity = 1
ground = 400
jump_height = 20
jump_is_allowed = False

width, height = 720, 480
screen = pygame.display.set_mode((width, height))

hero_right = pygame.image.load("assets/SnowMan1_right.png")
block = pygame.image.load("assets/mario_block.png")
bullet_image = pygame.image.load("assets/bullet.png")
weapon_image = pygame.image.load("assets/pistol_right.png")
hero_right = pygame.transform.scale(hero_right, (block_size, block_size))
block = pygame.transform.scale(block, (block_size, block_size))
bullet_image = pygame.transform.scale(bullet_image, (block_size // 10, block_size // 10))
weapon_image = pygame.transform.scale(weapon_image, (block_size // 3, block_size // 3))

game_map = [
    "..............................................",
    "..............................................",
    "..............................................",
    "..............................................",
    "..............................................",
    "bbbbbbbbbbbbbbbbb..............................",
    "..............................................",
    "..............................................",   
]


hero_x = 50
hero_y = 200
camera_x = 0
 
hero_rect = pygame.Rect(hero_x, hero_y, block_size, block_size)
weapon = Weapon(hero_x, hero_y)

block_rects = []
bullets = []
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == "b":
            block_rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            block_rects.append(block_rect)

# Game loop.
while run==True:
    screen.fill((0, 200, 255))
  
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT] == True:
        hero_x = hero_x + speed_h
    elif keystate[pygame.K_LEFT] == True:
        hero_x = hero_x - speed_h
    if keystate[pygame.K_UP] == True and jump_is_allowed:
        jump_is_allowed = False
        speed_v = speed_v - jump_height
    # if keystate[pygame.K_q]:
    #     bullets.append(Bullet(hero_x, hero_y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    speed_v = speed_v + gravity
    hero_y = hero_y + speed_v
    hero_rect.x = hero_x
    hero_rect.y = hero_y
    if hero_x - camera_x > width * 0.8:
        camera_x += speed_h
    if hero_x - camera_x < width * 0.15:
        camera_x -= speed_h
    screen.blit(hero_right, (hero_x - camera_x, hero_y))

    for rect in block_rects:
        if hero_rect.colliderect(rect):
            hero_y = rect.y - block_size
            speed_v = 0
            jump_is_allowed = True

    weapon.x = hero_x + block_size + 30
    weapon.y = hero_y + block_size // 5
    for rect in block_rects:
        screen.blit(block, (rect.x - camera_x, rect.y))
    screen.blit(weapon.image, (weapon.x, weapon.y))
    weapon.update()

    pygame.display.flip()

    clock.tick(fps)
pygame.quit()