import pygame
import random

#initialize the pygame
pygame.init()

# creating the screen (width, height) like x and y axis
screen = pygame.display.set_mode((800, 700))

# Title and icon
pygame.display.set_caption('Space invaders')
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# player/space ship
playerImg = pygame.image.load('space-ship.png')
# coordinates of where the player will spawn in the screen display pixels
player_cord_x = 350
player_cord_y = 600
player_cord_Xchange = 0
player_cord_Ychange = 0

# enemy
enemyImg = pygame.image.load('alien.png')
# enemy's random spawn coordinates
enemy_cord_x = random.randint(0, 736)
enemy_cord_y = random.randint(60, 200)
enemy_cord_Xchange = 0

def player(x, y):
    # blit for copying content from one surface to another
    # in other words, it draws the image in the specified pixels on the screen
    # Syntax : blit(source, destination, area=None, special_flags=0) -> Rect
    screen.blit(playerImg, (x, y))
    
def enemy(x, y):
    # blit for copying content from one surface to another
    # in other words, it draws the image in the specified pixels on the screen
    # Syntax : blit(source, destination, area=None, special_flags=0) -> Rect
    screen.blit(enemyImg, (x, y))

# Game loop: while its running, it'll go through the events, once its done or you click the close button, it'll quit/close the program
running = True
while running:
    
    # RGB color for screen
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # check key input
        # KEYDOWN means when key is pressed KEYUP means releasing the pressed key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_cord_Xchange = -0.2
            if event.key == pygame.K_RIGHT:
                player_cord_Xchange = 0.2
            if event.key == pygame.K_UP:
                player_cord_Ychange = -0.2
            if event.key == pygame.K_DOWN:
                player_cord_Ychange = 0.2
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_cord_Xchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_cord_Ychange = 0
    
    # key inputs will update the player coordinates
    player_cord_x += player_cord_Xchange
    player_cord_y += player_cord_Ychange
    
    # setting up boundaries
    if player_cord_x <= 0:
        player_cord_x = 0
    elif player_cord_x >= 736:
        # subtract x-axis pixel by the image pixel, otherwise it'll still go off screen
        player_cord_x = 736
    
    if player_cord_y <= 0:
        player_cord_y = 0
    elif player_cord_y >= 632:
        player_cord_y = 632
    
    # calling player and enemy after the screen loads to display itself
    player(player_cord_x, player_cord_y)
    enemy(enemy_cord_x, enemy_cord_y)
    
    #each time you add anything into the display window, you got to update it
    pygame.display.update()