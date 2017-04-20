# Imports//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import pygame
import intersects


# Initialize game engine///////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.init()


# Window//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
HEIGHT = 725
WIDTH = 1275
SIZE = (WIDTH, HEIGHT)
TITLE = "MAZE"

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SIZE)


# Timer//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
clock = pygame.time.Clock()
refresh_rate = 60


# Colors//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
WHITE = (255, 255, 255)
GREEN = (68, 104, 4)
BLACK = (0, 0, 0)
RED = (68, 0, 0)

# Make a player

player = [26, 26, 20, 20]
player_vx = 0
player_vy = 0
player_speed = 3


# walls man//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
wall1 = [0, 0, 25, 725] #outside walls
wall2 = [0, 0, 1300, 25]
wall3 = [0, 700, 1300, 25]
wall4 = [1250, 0, 25, 375]
wall5 = [1250, 375, 25, 350]

wall6 = [50, 50, 25, 600] # left insides barrier

wall7 = [75, 350, 200, 25] #left upper curl
wall8 = [75, 50, 275, 25]

wall9 = [50, 650, 300, 25]
wall10 = [350, 50, 25, 125]

wall11 = [100, 100, 25, 225]
wall12 = [125, 100, 200, 25]
wall13 = [150, 150, 225, 25]

wall14 = [400, 50, 200, 25] # left upper curl
wall15 = [575, 75, 25, 100]
wall16 = [400, 100, 150, 25]
wall17 = [400, 125, 25, 50]
wall18 = [425, 150, 175, 25]

wall19 = [150, 200, 25, 125] # left start of upper snake
wall20 = [175, 200, 50, 25]
wall21 = [200, 200, 25, 125]
wall22 = [250, 200, 25, 125]
wall23 = [300, 200, 25, 125]
wall24 = [350, 200, 25, 125]
wall25 = [400, 200, 25, 125]
wall26 = [450, 200, 25, 125]
wall27 = [500, 200, 25, 125]
wall28 = [550, 200, 25, 125]
wall29 = [600, 200, 25, 125]
wall30 = [650, 200, 25, 125]
wall31 = [700, 200, 25, 125]
wall32 = [750, 200, 25, 125]
wall33 = [800, 200, 25, 125]
wall34 = [850, 200, 25, 125]
wall35 = [900, 200, 25, 125]
wall36 = [950, 200, 25, 125]
wall37 = [1000, 200, 25, 125]
wall38 = [1050, 200, 25, 125]
wall39 = [1100, 200, 25, 125] # end of upper snake walls

wall40 = [275, 200, 25, 25] # upper snake connectors
wall41 = [375, 200, 25, 25]
wall42 = [475, 200, 25, 25]
wall43 = [575, 200, 25, 25]
wall44 = [675, 200, 25, 25]
wall45 = [775, 200, 25, 25]
wall46 = [875, 200, 25, 25]
wall47 = [975, 200, 25, 25]
wall48 = [1075, 200, 25, 25]
wall49 = [225, 300, 25, 25]
wall50 = [325, 300, 25, 25]
wall51 = [425, 300, 25, 25]
wall52 = [525, 300, 25, 25]
wall53 = [625, 300, 25, 25]
wall54 = [725, 300, 25, 25]
wall55 = [825, 300, 25, 25]
wall56 = [925, 300, 25, 25]
wall57 = [1025, 300, 25, 25] # end of upper snake

wall58 = [1200, 50, 25, 600] # right inside barrier
wall59 = [1000, 350, 200, 25]
wall60 = [300, 350, 675, 25]

wall61 = [1150, 100, 25, 225]

wall62 = [900, 50, 300, 25] # right upper curl
wall63 = [900, 75, 25, 100]
wall64 = [925, 150, 200, 25]
wall65 = [950, 100, 200, 25]

wall66 = [675, 50, 200, 25]
wall67 = [675, 75, 25, 100]
wall68 = [700, 150, 175, 25]
wall69 = [850, 100, 25, 50]
wall70 = [725, 100, 125, 25]

wall71 = [625, 50, 25, 125] # upper  middle wall

wall72 = [625, 550, 25, 125] # lower middle wall

wall73 = [900, 650, 325, 25]
wall74 = [400, 650, 200, 25]
wall75 = [675, 650, 200, 25]

wall76 = [100, 400, 25, 225]
wall77 = [125, 600, 200, 25]
wall78 = [350, 575, 25, 100]
wall79 = [150, 550, 225, 25]

wall80 = [575, 550, 25, 100]
wall81 = [675, 550, 25, 100]
wall82 = [900, 550, 25, 100]
wall83 = [400, 550, 200, 25]

wall84 = [700, 550, 175, 25]
wall85 = [925, 550, 200, 25]

wall86 = [400, 600, 150, 25]
wall87 = [725, 600, 150, 25]

wall88 = [400, 625, 25, 25]
wall89 = [850, 625, 25, 25]

wall90 = [950, 600, 200, 25]
wall91 = [1150, 400, 25, 225]

wall92 = [150, 400, 25, 125]# lower snake walls
wall93 = [200, 400, 25, 125]

wall94 = [250, 400, 25, 125]
wall95 = [300, 400, 25, 125]
wall96 = [350, 400, 25, 125]
wall97 = [400, 400, 25, 125]
wall98 = [450, 400, 25, 125]
wall99 = [500, 400, 25, 125]
wall100 = [550, 400, 25, 125]
wall101 = [600, 400, 25, 125]
wall102 = [650, 400, 25, 125]
wall103 = [700, 400, 25, 125]
wall104 = [750, 400, 25, 125]
wall105 = [800, 400, 25, 125]
wall106 = [850, 400, 25, 125]
wall107 = [900, 400, 25, 125]
wall108 = [950, 400, 25, 125]
wall109 = [1000, 400, 25, 125]
wall110 = [1050, 400, 25, 125]
wall111 = [1100, 400, 25, 125]

wall112 = [175, 500, 25, 25]
wall113 = [225, 400, 25, 25]
wall114 = [275, 500, 25, 25]
wall115 = [325, 400, 25, 25]
wall116 = [375, 500, 25, 25]
wall117 = [425, 400, 25, 25]
wall118 = [475, 500, 25, 25]
wall119 = [525, 400, 25, 25]
wall120 = [575, 500, 25, 25]
wall121 = [625, 400, 25, 25]
wall122 = [675, 500, 25, 25]
wall123 = [725, 400, 25, 25]
wall124 = [775, 500, 25, 25]
wall125 = [825, 400, 25, 25]
wall126 = [875, 500, 25, 25]
wall127 = [925, 400, 25, 25]
wall128 = [975, 500, 25, 25]
wall129 = [1025, 400, 25, 25]
wall130 = [1075, 500, 25, 25]



walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12,
         wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24,
         wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36,
         wall37, wall38, wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48,
         wall49, wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57, wall58, wall59, wall60,
         wall61, wall62, wall63, wall64, wall65, wall66, wall67, wall68, wall69, wall70, wall71, wall72,
         wall73, wall74, wall75, wall76, wall77, wall78, wall79, wall80, wall81, wall82, wall83, wall84,
         wall85, wall86, wall87, wall88, wall89, wall90, wall91, wall92, wall93, wall94, wall95, wall96,
         wall97, wall98, wall99, wall100, wall101, wall102, wall103, wall104, wall105, wall106, wall107,
         wall108, wall109, wall110, wall111, wall112, wall113, wall114, wall115, wall116, wall117, wall118,
         wall119, wall120, wall121, wall122, wall123, wall124, wall125, wall126, wall127, wall128, wall129,
         wall130]

coins = []

for x in range(100, 1200, 25):
    coin = [x, 325, 25, 25]
    coins.append(coin)

for x in range(150, 1125, 25):
    coin = [x, 175, 25, 25]
    coins.append(coin)

for x in range(75, 1200, 25):
    coin = [x, 375, 25, 25]
    coins.append(coin)

for x in range(150, 1125, 25):
    coin = [x, 525, 25, 25]
    coins.append(coin)

for x in range(25, 1250, 25):
    coin = [x, 25, 25, 25]
    coins.append(coin)

for x in range(100, 325, 25):
    coin = [x, 75, 25, 25]
    coins.append(coin)

for x in range(400, 575, 25):
    coin = [x, 75, 25, 25]
    coins.append(coin)

for x in range(725, 875, 25):
    coin = [x, 75, 25, 25]
    coins.append(coin)

for x in range(925, 1175, 25):
    coin = [x, 75, 25, 25]
    coins.append(coin)

for x in range(150, 325, 25):
    coin = [x, 125, 25, 25]
    coins.append(coin)

for x in range(950, 1125, 25):
    coin = [x, 125, 25, 25]
    coins.append(coin)

for x in range(425, 550, 25):
    coin = [x, 125, 25, 25]
    coins.append(coin)

for x in range(725, 850, 25):
    coin = [x, 125, 25, 25]
    coins.append(coin)

for x in range(25, 1250, 25):
    coin = [x, 675, 25, 25]
    coins.append(coin)

for x in range(100, 325, 25):
    coin = [x, 625, 25, 25]
    coins.append(coin)

for x in range(425, 575, 25):
    coin = [x, 625, 25, 25]
    coins.append(coin)

for x in range(725, 850, 25):
    coin = [x, 625, 25, 25]
    coins.append(coin)

for x in range(925, 1175, 25):
    coin = [x, 625, 25, 25]
    coins.append(coin)

for x in range(950, 1125, 25):
    coin = [x, 575, 25, 25]
    coins.append(coin)

for x in range(400, 550, 25):
    coin = [x, 575, 25, 25]
    coins.append(coin)

for x in range(725, 875, 25):
    coin = [x, 575, 25, 25]
    coins.append(coin)

for x in range(150, 325, 25):
    coin = [x, 575, 25, 25]
    coins.append(coin)

for y in range(50, 700, 25):
    coin = [25, y, 25, 25]
    coins.append(coin)

for y in range(75, 350, 25):
    coin = [75, y, 25, 25]
    coins.append(coin)

for y in range(75, 150, 25):
    coin = [550, y, 25, 25]
    coins.append(coin)

for y in range(75, 150, 25):
    coin = [925, y, 25, 25]
    coins.append(coin)

for y in range(75, 150, 25):
    coin = [700, y, 25, 25]
    coins.append(coin)

for y in range(125, 325, 25):
    coin = [125, y, 25, 25]
    coins.append(coin)

for y in range(75, 150, 25):
    coin = [325, y, 25, 25]
    coins.append(coin)

for y in range(50, 175, 25):
    coin = [375, y, 25, 25]
    coins.append(coin)

for y in range(50, 175, 25):
    coin = [600, y, 25, 25]
    coins.append(coin)

for y in range(50, 175, 25):
    coin = [650, y, 25, 25]
    coins.append(coin)

for y in range(50, 175, 25):
    coin = [875, y, 25, 25]
    coins.append(coin)

for y in range(125, 325, 25):
    coin = [1125, y, 25, 25]
    coins.append(coin)

for y in range(400, 600, 25):
    coin = [1125, y, 25, 25]
    coins.append(coin)

for y in range(400, 650, 25):
    coin = [1175, y, 25, 25]
    coins.append(coin)

for y in range(75, 325, 25):
    coin = [1175, y, 25, 25]
    coins.append(coin)

for y in range(50, 700, 25):
    coin = [1225, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [175, y, 25, 25]
    coins.append(coin)

for y in range(200, 300, 25):
    coin = [225, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [275, y, 25, 25]
    coins.append(coin)

for y in range(200, 300, 25):
    coin = [325, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [375, y, 25, 25]
    coins.append(coin)

for y in range(200, 300, 25):
    coin = [425, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [475, y, 25, 25]
    coins.append(coin)

for y in range(200, 300, 25):
    coin = [525, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [575, y, 25, 25]
    coins.append(coin)

for y in range(200, 300, 25):
    coin = [625, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [675, y, 25, 25]
    coins.append(coin)

for y in range(200, 300, 25):
    coin = [725, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [775, y, 25, 25]
    coins.append(coin)

for y in range(200, 300, 25):
    coin = [825, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [875, y, 25, 25]
    coins.append(coin)

for y in range(200, 300, 25):
    coin = [925, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [975, y, 25, 25]
    coins.append(coin)

for y in range(200, 300, 25):
    coin = [1025, y, 25, 25]
    coins.append(coin)

for y in range(225, 325, 25):
    coin = [1075, y, 25, 25]
    coins.append(coin)



for y in range(400, 500, 25):
    coin = [175, y, 25, 25]
    coins.append(coin)

for y in range(425, 525, 25):
    coin = [225, y, 25, 25]
    coins.append(coin)

for y in range(400, 500, 25):
    coin = [275, y, 25, 25]
    coins.append(coin)

for y in range(425, 525, 25):
    coin = [325, y, 25, 25]
    coins.append(coin)

for y in range(400, 500, 25):
    coin = [375, y, 25, 25]
    coins.append(coin)

for y in range(425, 525, 25):
    coin = [425, y, 25, 25]
    coins.append(coin)

for y in range(400, 500, 25):
    coin = [475, y, 25, 25]
    coins.append(coin)

for y in range(425, 525, 25):
    coin = [525, y, 25, 25]
    coins.append(coin)

for y in range(400, 500, 25):
    coin = [575, y, 25, 25]
    coins.append(coin)

for y in range(425, 525, 25):
    coin = [625, y, 25, 25]
    coins.append(coin)

for y in range(400, 500, 25):
    coin = [675, y, 25, 25]
    coins.append(coin)

for y in range(425, 525, 25):
    coin = [725, y, 25, 25]
    coins.append(coin)

for y in range(400, 500, 25):
    coin = [775, y, 25, 25]
    coins.append(coin)

for y in range(425, 525, 25):
    coin = [825, y, 25, 25]
    coins.append(coin)

for y in range(400, 500, 25):
    coin = [875, y, 25, 25]
    coins.append(coin)

for y in range(425, 525, 25):
    coin = [925, y, 25, 25]
    coins.append(coin)

for y in range(400, 500, 25):
    coin = [975, y, 25, 25]
    coins.append(coin)

for y in range(425, 525, 25):
    coin = [1025, y, 25, 25]
    coins.append(coin)

for y in range(400, 500, 25):
    coin = [1075, y, 25, 25]
    coins.append(coin)

for y in range(400, 600, 25):
    coin = [125, y, 25, 25]
    coins.append(coin)

for y in range(400, 650, 25):
    coin = [75, y, 25, 25]
    coins.append(coin)

for y in range(575, 650, 25): #???????????????????????????????
    coin = [325, y, 25, 25]
    coins.append(coin)

for y in range(550, 675, 25):
    coin = [375, y, 25, 25]
    coins.append(coin)

for y in range(575, 650, 25):
    coin = [550, y, 25, 25]
    coins.append(coin)

for y in range(550, 675, 25):
    coin = [600, y, 25, 25]
    coins.append(coin)

for y in range(550, 675, 25):
    coin = [650, y, 25, 25]
    coins.append(coin)

for y in range(575, 650, 25): 
    coin = [700, y, 25, 25]
    coins.append(coin)

for y in range(550, 675, 25):
    coin = [875, y, 25, 25]
    coins.append(coin)

for y in range(575, 650, 25): #???????????????????????????????
    coin = [925, y, 25, 25]
    coins.append(coin)


# Game loop/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if up:
        player_vy = -player_speed
    elif down:
        player_vy = player_speed
    else:
        player_vy = 0

    if left:
        player_vx = -player_speed
    elif right:
        player_vx  = player_speed
    else:
        player_vx = 0

    # Game Logic (Check for Collitions)
    ''' moves player in horizontal direction'''    
    player[0] += player_vx

    '''wall horizontal collisions'''
    for w in walls:
        if intersects.rect_rect(player, w):
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]

    '''moves player in vertical direction'''
    player[1] += player_vy

    '''wall vertical collisions'''
    for w in walls:
        if intersects.rect_rect(player, w):
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]# Drawing Code


    if (len(coins) == 0):
        print("You Win")
                
    screen.fill(BLACK)


    '''coin intersects'''
    for c in coins:
        if intersects.rect_rect(player, c):
            coins.remove(c)

    

    for w in walls: #draw walls
        pygame.draw.rect(screen, GREEN, w)

    for c in coins:
        pygame.draw.rect(screen, WHITE, c)


    pygame.draw.rect(screen, RED, player)

    # Update window
    pygame.display.update()
    clock.tick(refresh_rate)
    

# Close window and quit//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.quit()


    
