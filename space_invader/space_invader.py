import pygame
import random
import math

# initialize the pygame
pygame.init()

# creating the screen (width, height) like x and y axis
screen = pygame.display.set_mode((800, 700))

# background image
background = pygame.image.load("space.png")

# Title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)

# player/space ship
playerImg = pygame.image.load("space-ship.png")
# coordinates of where the player will spawn in the screen display pixels
player_cord_x = 350
player_cord_y = 600
player_cord_Xchange = 0
player_cord_Ychange = 0

# enemy
enemyImg = pygame.image.load("alien.png")
enemy_hitbox = enemyImg.get_rect()
# enemy's random spawn coordinates
enemy_cord_x = random.randint(0, 736)
enemy_cord_y = random.randint(60, 200)
enemy_cord_Xchange = 0.3
enemy_cord_Ychange = 20

# bullet
bulletImg = pygame.image.load("bullet.png")
bullet_hitbox = bulletImg.get_rect()
bullet_cord_x = 0
bullet_cord_y = 600
bullet_cord_Ychange = 0.5
bullet_state = "ready"

enemies_defeated = 0


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
    # pygame.draw.rect(enemyImg, (255,255,255), enemy_hitbox, 4)


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    # pygame.draw.rect(bulletImg, (255,255,255), bullet_hitbox, 4)


def collision_triggered(enemy_cord_x, enemy_cord_y, bullet_cord_x, bullet_cord_y):
    if int(bullet_cord_y) == enemy_cord_y:
        if int(bullet_cord_x) in range(int(enemy_cord_x), int(enemy_cord_x + 64)):
            return True
    return False


# Game loop: while its running, it'll go through the events, once its done or you click the close button, it'll quit/close the program
running = True
while running:
    # RGB color for screen
    screen.fill((255, 255, 255))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check key input
        # KEYDOWN means when key is pressed KEYUP means releasing the pressed key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_cord_Xchange = -0.4
            if event.key == pygame.K_RIGHT:
                player_cord_Xchange = 0.4
            if event.key == pygame.K_UP:
                player_cord_Ychange = -0.4
            if event.key == pygame.K_DOWN:
                player_cord_Ychange = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # give bullet the player's coordinate so it'll fire where it was
                    bullet_cord_x = player_cord_x
                    bullet_cord_y = player_cord_y
                    # call function to fire when space is pressed
                    fire_bullet(bullet_cord_x, bullet_cord_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_cord_Xchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_cord_Ychange = 0

    # key inputs will update the player coordinates
    player_cord_x += player_cord_Xchange
    player_cord_y += player_cord_Ychange

    # setting up boundaries for player
    # should not exceed max screen size or go into negative
    # when it reaches a certain pixel, it'll spawn it back to the edge
    # x-axis limit
    if player_cord_x <= 0:
        player_cord_x = 0
    elif player_cord_x >= 736:
        # subtract x-axis pixel by the image pixel, otherwise it'll still go off screen
        player_cord_x = 736
    # y-axis limit
    if player_cord_y <= 0:
        player_cord_y = 0
    elif player_cord_y >= 632:
        player_cord_y = 632

    # enemies' boundaries
    enemy_cord_x += enemy_cord_Xchange

    if enemy_cord_x <= 0:
        enemy_cord_Xchange = 0.3
        # only change y coordinates when it hits the wall, otherwise it'll keep going down
        enemy_cord_y += enemy_cord_Ychange
    elif enemy_cord_x >= 736:
        enemy_cord_Xchange = -0.3
        enemy_cord_y += enemy_cord_Ychange

    # bullet coordinate resets
    if bullet_cord_y <= 0:
        bullet_cord_y = player_cord_y
        bullet_state = "ready"

    if bullet_state == "fire":
        # needs to have the function here in while loop to make it persist in the game
        fire_bullet(bullet_cord_x, bullet_cord_y)
        bullet_cord_y -= bullet_cord_Ychange

    # collision
    collision = collision_triggered(
        enemy_cord_x, enemy_cord_y, bullet_cord_x, bullet_cord_y
    )
    if collision:
        bullet_cord_x = player_cord_x
        bullet_state = "ready"
        enemies_defeated += 1
        enemy_cord_x = random.randint(0, 736)
        enemy_cord_y = random.randint(60, 200)
        print(enemies_defeated)

    # calling player and enemy after the screen loads to display itself
    player(player_cord_x, player_cord_y)
    enemy(enemy_cord_x, enemy_cord_y)

    # each time you add anything into the display window, you got to update it
    pygame.display.update()
