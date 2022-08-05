import pygame

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = square

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] == True:
            self.y = self.y - 10
        if keystate[pygame.K_w] == True:
            self.y = self.y - 10
        if keystate[pygame.K_DOWN] == True:
            self.y = self.y + 10
        if keystate[pygame.K_s] == True:
            self.y = self.y + 10
        if keystate[pygame.K_RIGHT] == True:
            self.x = self.x + 10
        if keystate[pygame.K_d] == True:
            self.x = self.x + 10
        if keystate[pygame.K_LEFT] == True:
            self.x = self.x -10
        if keystate[pygame.K_LEFT] == True:
            self.x = self.x -10
        if keystate[pygame.K_a] == True:
            self.x = self.x -10
        if keystate[pygame.K_SPACE] == True:
            self.x=10

class Treugolnik:
  
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = treugolnik_image
        
    def update(self):
        pass
        # keystate = pygame.key.get_pressed()
        # if self.x >= width * 0.8:
            # self.y = self.y + 1
    


class Treugolnik2:
  
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = treugolnik_two_image
        
    def update(self):
        self.y = self.y + 1


class Ugol6:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ugol6_image
        
    def update(self):
        self.y = self.y + 1

pygame.init()
fps = 60
clock = pygame.time.Clock()
block_size = 64

treugolnik_image = pygame.image.load("assets/зеленый треугольник.png")
treugolnik_image = pygame.transform.scale(treugolnik_image, (block_size, block_size))
square = pygame.image.load("красный квадрат.png")
square = pygame.transform.scale(square, (block_size, block_size))
treugolnik_two_image = pygame.image.load("assets/синий треугольник.png")
treugolnik_two_image = pygame.transform.scale(treugolnik_two_image, (block_size, block_size))
ugol6_image = pygame.image.load("assets/черный шестиугольник пнг.png")
ugol6_image = pygame.transform.scale(ugol6_image, (block_size, block_size))
width, height = 640, 480

screen = pygame.display.set_mode((width, height))

hero = Hero(100, 100)
show_triangle = False
show_ugol6 = False
run = True
# Game loop.
while run:
    screen.fill((0, 0, 0))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if hero.x >= width * 0.8:
        show_triangle = True
        triangle = Treugolnik(width * 0.8, 1) 

    if show_triangle == True:
        triangle.update()    
        screen.blit(triangle.image, (triangle.x, triangle.y))

    if hero.x >= width * 0.8:
        show_ugol6= True
        ugol6 = Ugol6(width * 0.5, 100) 

    if show_ugol6 == True:
        ugol6.update()    
        screen.blit(ugol6.image, (ugol6.x, ugol6.y))

    hero.update()
    t2 = Treugolnik2(45, 300)    
    t2.update()
    screen.blit(t2.image, (t2.x, t2.y))       
    screen.blit(hero.image, (hero.x,hero.y))
    pygame.display.flip()
    clock.tick(fps)

    # if show_treugolnik2 == True:

# Treugolnik_two = Treugolnik_two(100, 100)
pygame.quit()