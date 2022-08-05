import pygame
import time
 

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = enemy_image
        self.speed_h = 3
        self.speed_v = 0
        self.rect = pygame.Rect(self.x, self.y, block_size, block_size)
        self.hp = 100

    def update(self, hero_x, hero_y):
        if hero_x - self.x > 0:
            self.x = self.x + self.speed_h
        else:
            self.x = self.x - self.speed_h
            self.speed_v = self.speed_v + gravity

        self.y = self.y + self.speed_v
        self.rect.x = self.x - camera_x
        self.rect.y = self.y



class Bullet:
    def __init__(self, x, y, master):
        self.x = x
        self.y = y
        self.speed = 10
        self.image = bullet_image
        self.rect = pygame.Rect(x, y, block_size // 10, block_size // 10)
        self.master = master

    def update(self):
        self.x = self.x + self.speed
        self.rect.x = self.x
        self.rect.y = self.y


class Weapon:
    def __init__(self, x, y, master):
        self.x = x
        self.y = y
        self.image = weapon_image
        self.bullets = []
        self.start = time.time()
        self.interval = 2
        self.master = master

    def update(self):
        if keystate[pygame.K_q]:
            self.shoot()
            
        for bullet in hero_bullets:
            bullet.update()
            screen.blit(bullet.image, (bullet.x - camera_x, bullet.y))
            if bullet.x - camera_x > width + 100:
                hero_bullets.remove(bullet)


        for bullet in enemy_bullets:
            bullet.update()
            screen.blit(bullet.image, (bullet.x - camera_x, bullet.y))
            if bullet.x - camera_x > width + 100:
                enemy_bullets.remove(bullet)


    def shoot(self):
        if time.time() - self.start > self.interval:
            if self.master == "hero":
                hero_bullets.append(Bullet(self.x, self.y, "hero"))
            elif self.master == "enemy":
                enemy_bullets.append(Bullet(self.x, self.y, "enemy"))
            self.start = time.time()

    
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
enemy_image = pygame.image.load("assets/stay_right.png")
hero_right = pygame.transform.scale(hero_right, (block_size, block_size))
block = pygame.transform.scale(block, (block_size, block_size))
bullet_image = pygame.transform.scale(bullet_image, (block_size // 10, block_size // 10))
weapon_image = pygame.transform.scale(weapon_image, (block_size // 3, block_size // 3))
enemy_image = pygame.transform.scale(enemy_image, (block_size, block_size))

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


hero_x = width * 0.5
hero_y = 200
camera_x = 0
 
hero_rect = pygame.Rect(hero_x, hero_y, block_size, block_size)
enemy = Enemy(500, 100)
weapon = Weapon(hero_x, hero_y, "hero")

block_rects = []
hero_bullets = []
enemy_bullets = []
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

    for rect in block_rects:
        if hero_rect.colliderect(rect):
            hero_y = rect.y - block_size
            speed_v = 0
            jump_is_allowed = True
        if enemy.rect.colliderect(rect):
            enemy.y = rect.y - block_size
            enemy.speed_v = 0

    weapon.x = hero_x + 25
    weapon.y = hero_y + 25
    for rect in block_rects:
        screen.blit(block, (rect.x - camera_x, rect.y))
    for bullet in hero_bullets:
        if bullet.rect.colliderect(enemy.rect):
            hero_bullets.remove(bullet)
            enemy.hp = enemy.hp - 10
    pygame.draw.circle(screen, (0, 0, 0), (hero_x - camera_x, hero_y), 3)
    pygame.draw.rect(screen, (0, 0, 0), (enemy.rect.x, enemy.rect.y, block_size, block_size), 3)
    screen.blit(enemy.image, (enemy.x - camera_x, enemy.y))
    screen.blit(hero_right, (hero_x - camera_x, hero_y))
    screen.blit(weapon.image, (weapon.x - camera_x, weapon.y))
    enemy.update(hero_x, hero_y)
    weapon.update()
    print(enemy.hp)

    pygame.display.flip()

    clock.tick(fps)
pygame.quit()