import pygame
import random

# TASK
# redo collision and then delete version 1's enemy and bullet code

#initialize the pygame
pygame.init()

# creating the screen (width, height) like x and y axis
screen = pygame.display.set_mode((800, 700))

# background image
background = pygame.image.load('space.png')

# Title and icon
pygame.display.set_caption('Space invaders')
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xchange = 0
        self.ychange = 0
        self.img = pygame.image.load('space-ship.png')
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, 64,64), 4)

# player initial position
player = Player(350, 600)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xchange = 0.3
        self.ychange = 20
        self.img = pygame.image.load('alien.png')
        
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, 64,64), 4)

emy = Enemy(random.randint(0, 736), random.randint(60, 200))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ychange = 0.5
        self.state = "ready"
        self.img = pygame.image.load('bullet.png') 
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, 32,32), 4)
        blt.state = "fire"
    
    # def shoot(self, fire_rate):
    #     self.y += fire_rate
    
    # def off_screen(self, height):
    #     return self.y <= height and self.y >= 0
    
    def collision(self, hit):
        return collided(self, hit)
    
blt = Bullet(player.x, player.y)

def collided(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2, (offset_x, offset_y)) != None
    
    

# enemy
enemyImg = pygame.image.load('alien.png')
enemy_hitbox = enemyImg.get_rect()
# enemy's random spawn coordinates
enemy_cord_x = random.randint(0, 736)
enemy_cord_y = random.randint(60, 200)
enemy_cord_Xchange = 0.3
enemy_cord_Ychange = 20

# bullet
bulletImg = pygame.image.load('bullet.png')
bullet_hitbox = bulletImg.get_rect()
bullet_cord_x = 0
bullet_cord_y = 600
bullet_cord_Ychange = 0.5
bullet_state = "ready"

def enemy(x, y):
    # blit for copying content from one surface to another
    # in other words, it draws the image in the specified pixels on the screen
    # Syntax : blit(source, destination, area=None, special_flags=0) -> Rect
    screen.blit(enemyImg, (x, y))
    # pygame.draw.rect(enemyImg, (255,255,255), enemy_hitbox, 4)

enemies_defeated = 0

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))
    # pygame.draw.rect(bulletImg, (255,255,255), bullet_hitbox, 4)

def collision_triggered(enemy_cord_x, enemy_cord_y, bullet_cord_x, bullet_cord_y):
    
    # of the bullet reach a certain mid point of the enemy, it'll trigger collision
    
    # distance = math.sqrt((math.pow(enemy_cord_x - enemy_cord_y, 2)) + (math.pow(bullet_cord_x - bullet_cord_y, 2)))
    # if distance < 27:
    #     return True
    # else:
    #     return False
    
    # because mid point and colliderect isn't working, this will have to do
    if int(bullet_cord_y) == enemy_cord_y:
        if int(bullet_cord_x) in range(int(enemy_cord_x), int(enemy_cord_x+64)):
            print(bullet_cord_y, " ", enemy_cord_y)
            print(bullet_cord_x, " ", enemy_cord_x, " ", enemy_cord_x+64)
            return True
    else:
        return False
    

running = True
while running:
    
    # RGB color for screen
    screen.fill((255,255,255))
    # background image
    screen.blit(background, (0, 0))
    
    # draw the objects
    player.draw(screen)
    emy.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # check key input
    # KEYDOWN means when key is pressed KEYUP means releasing the pressed key
    # ALT player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.xchange = -0.4
            if event.key == pygame.K_RIGHT:
                player.xchange = 0.4
            if event.key == pygame.K_UP:
                player.ychange = -0.4
            if event.key == pygame.K_DOWN:
                player.ychange = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # give bullet the player's coordinate so it'll fire where it was
                    bullet_cord_x = player.x
                    bullet_cord_y = player.y
                    # call function to fire when space is pressed
                    fire_bullet(bullet_cord_x, bullet_cord_y)
            if event.key == pygame.K_q:
                if blt.state == "ready":
                    blt.x = player.x
                    blt.y = player.y
                    blt.draw(screen)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.ychange = 0         
    # ALT player movement update
    player.x += player.xchange
    player.y += player.ychange
    
    
    # setting up boundaries for player
    # should not exceed max screen size or go into negative
    # when it reaches a certain pixel, it'll spawn it back to the edge
    # x-axis limit
    if player.x <= 0:
        player.x = 0
    elif player.x >= 736:
        # subtract x-axis pixel by the image pixel, otherwise it'll still go off screen
        player.x = 736
    # y-axis limit
    if player.y <= 0:
        player.y = 0
    elif player.y >= 632:
        player.y = 632
        
    # ALT ENEMY boundaries
    emy.x += emy.xchange
    
    if emy.x <= 0:
        # only change y coordinates when it hits the wall, otherwise it'll keep going down
        emy.xchange = 0.3
        emy.y += emy.ychange
    elif emy.x >= 736:
        emy.xchange = -0.3
        emy.y += emy.ychange
    
    if emy.y >= 636:
        emy.x = random.randint(0, 736)
        emy.y = random.randint(60, 200)
        
    # ALT BULLET
    if blt.y <= 0:
        blt.y = player.y
        blt.state = "ready"
    
    if blt.state == "fire":
        blt.draw(screen)
        blt.y -=blt.ychange
    
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
        bullet_cord_y = player.y
        bullet_state = "ready"
    
    if bullet_state == "fire":
        # needs to have the function here in while loop to make it persist in the game
        fire_bullet(bullet_cord_x, bullet_cord_y)
        bullet_cord_y -= bullet_cord_Ychange
    
    # collision
    collision =  collision_triggered(enemy_cord_x, enemy_cord_y, bullet_cord_x, bullet_cord_y)
    if collision:
        bullet_cord_x = player.x
        bullet_state = "ready"
        enemies_defeated += 1
        enemy_cord_x = random.randint(0, 736)
        enemy_cord_y = random.randint(60, 200)
        print(enemies_defeated)
    
    enemy(enemy_cord_x, enemy_cord_y)
    #each time you add anything into the display window, you got to update it
    pygame.display.update()