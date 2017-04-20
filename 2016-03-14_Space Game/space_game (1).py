#  Space Game (for test)

import pygame
import intersects

pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 500
TITLE = "Space Game"
FPS = 60

# Make the window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 150)

# Physics
H_SPEED = 5
JUMP_POWER = 10
GRAVITY = 0.3

# Images
astronaut_img = pygame.image.load("astronaut.png")
astronaut_img = pygame.transform.scale(astronaut_img, [60, 80])

        
class SpaceMan():

    def __init__(self, x, y, img):
        self.img = img
        self.x = x
        self.y = y
        self.w = img.get_width()
        self.h = img.get_height()
        
        self.vx = 0
        self.vy = 0

    def get_rect(self):
        return [self.x, self.y, self.w, self.h]

    def jump(self, ground):
        self.y += 1

        if intersects.rect_rect(self.get_rect(), ground.get_rect()):
            self.vy = -JUMP_POWER

        self.y -= 1

    def move(self, vx):
        self.vx += vx

    def stop(self):
        self.vx = 0       
        
    def update(self, ground):
        self.x += self.vx
        self.y += self.vy

        self.vy += GRAVITY

        if self.x < 0:
            self.x = 0
        elif self.x + self.w > WIDTH:
            self.x = WIDTH - self.w
            
        if self.y < 0:
            self.y = 0
        elif self.y + self.h > ground.y:
            self.y = ground.y - self.h
        
    def draw(self):
        #pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h])
        screen.blit(self.img, [self.x, self.y])


class Ground():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = YELLOW

    def get_rect(self):
        return [self.x, self.y, self.w, self.h]
        
    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h])


# Make game objects
player = SpaceMan(500, 50, astronaut_img)
ground = Ground(0, 400, 800, 100)


# game loop
done = False

while not done:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-H_SPEED)
            elif event.key == pygame.K_RIGHT:
                player.move(H_SPEED)
            elif event.key == pygame.K_SPACE:
                player.jump(ground)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.stop()
            elif event.key == pygame.K_RIGHT:
                player.stop()

    # game logic
    player.update(ground)

    #drawing
    screen.fill(BLACK)
    player.draw()
    ground.draw()
    
    # update screen
    pygame.display.update()
    clock.tick(FPS)


# close window on quit
pygame.quit ()
