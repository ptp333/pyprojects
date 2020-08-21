import pygame
import random
import math
from pygame import mixer

# initialization
pygame.init()

# create the game screen
screen = pygame.display.set_mode((800, 513))  # (w,h)

# game background image
background = pygame.image.load('background.jpg')

# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# game window caption and icon
pygame.display.set_caption("COVID-19 WAR")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# set player position, image and movement
playerImg = pygame.image.load('attacker.png')
playerX = 370
playerY = 430
playerX_change = 0

# set enemy position, image and movement
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('virus.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(5, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# ready - You can't see the bullet on the screen
# ready - The bullet is currently moving
# set bullet position, image and movement
bulletImg = pygame.image.load('drop.png')
bulletX = 0
bulletY = 430
bulletX_change = 0
bulletY_change = 7
bullet_state = 'ready'


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render('Score : ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# movement of player
def player(x, y):
    screen.blit(playerImg, (x, y))


# movement of enemy
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    # set game background color as black with RGB value
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Handling game movement with keys
        if event.type == pygame.KEYDOWN:
            # if keystroke is pressed check whether its right or left and set changing movement
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                # print("Left Arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                # print("Right Arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    # Get the current X co-ordinates of the player
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                # print("Keystroke has been released")

    # player movement
    playerX += playerX_change

    # To stop player at boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # To stop enemy at boundaries and changes movement
    for i in range(no_of_enemies):

        # Game over
        if enemyY[i] > 400:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        # enemy movement
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            bulletY = 430
            bullet_state = 'ready'
            score_value += 1
            # print(score_value)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(5, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 430
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
