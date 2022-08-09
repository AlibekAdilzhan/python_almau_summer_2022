import pygame
from copy import deepcopy


class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pacman_image
        self.rect = pygame.Rect(x, y, block_size // 2, block_size // 2)
        self.previous_x = x
        self.previous_y = y

    def update(self):
        keystate = pygame.key.get_pressed()
        self.previous_x = self.x
        self.previous_y = self.y
        if keystate[pygame.K_LEFT]:
            self.x -= self.speed
        elif keystate[pygame.K_RIGHT]:
            self.x += self.speed
        elif keystate[pygame.K_UP]:
            self.y -= self.speed
        elif keystate[pygame.K_DOWN]:
            self.y += self.speed

        self.rect.x = self.x
        self.rect.y = self.y


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.image = enemy_image
        self.rect = pygame.Rect(x, y, block_size // 2, block_size // 2)
        self.path = []

    def update(self, end):
        start = [(self.x + block_size // 4) // block_size, (self.y + block_size // 4) // block_size]
        if self.path == []:
            self.path = djicstra(start, end)
            self.path.pop()
            self.path.reverse()
        current_dest = self.path[0]
        current_dest = [current_dest[1], current_dest[0]]
        current_i = (self.x + block_size // 4) // block_size
        current_j = (self.y + block_size // 4) // block_size
        if current_i == current_dest[0] and current_j == current_dest[1]:
            self.path.pop(0)
        direction_x = current_dest[0] - current_i
        direction_y = current_dest[1] - current_j
        self.x += direction_x
        self.y += direction_y




def djicstra(start, end):
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

    path = []
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





game_map = [
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

pygame.init()
 
# game settings
block_size = 32
fps = 60
clock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

pacman_image = pygame.image.load("assets/pacman.png")
pacman_image = pygame.transform.scale(pacman_image, (block_size // 2, block_size // 2))
enemy_image = pygame.image.load("assets/ghost.png")
enemy_image = pygame.transform.scale(enemy_image, (block_size // 2, block_size // 2))

rects = []
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == 1:
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            rects.append(rect)

start_position = [1, 1]

pacman = Pacman(block_size * start_position[1], block_size * start_position[0])
enemy = Enemy(block_size * 13, block_size * 10)
run = True
# Game loop.
while run:
    screen.fill((255, 255, 255))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == 1:
                pygame.draw.rect(screen, (0, 150, 100), (j * block_size, i * block_size, block_size, block_size))

    for rect in rects:
        if pacman.rect.colliderect(rect):
            pacman.x = pacman.previous_x
            pacman.y = pacman.previous_y
    pacman.update()
    enemy.update([pacman.x // block_size, pacman.y // block_size])
    screen.blit(pacman.image, (pacman.x, pacman.y))
    screen.blit(enemy.image, (enemy.x, enemy.y))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()