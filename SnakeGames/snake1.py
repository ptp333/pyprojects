import pygame
import time
import random


# pygame window initialization
pygame.init()
clock = pygame.time.Clock()

# RGB color
orange = (255, 123, 7)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 150, 255)

# to set game window size
display_width = 600
display_height = 400
display_window = pygame.display.set_mode((display_width, display_height))

# to set caption
pygame.display.set_caption('Snake Game')
snake_block = 10
snake_list = []


# defines the snake's structure and position
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display_window, orange, [x[0], x[1], snake_block, snake_block])

# main function
def snake_game():
    game_over = False
    game_end = False
    # co-ordinates of the snake
    x1 = display_width / 2
    y1 = display_height / 2
    # when the snakes moves
    x1_change = 0
    y1_change = 0

    # define the length of the snake
    snake_list = []
    length_of_snake = 1
    snake_speed = 15
    # the co-ordinates of food element
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_end:
            display_window.fill(blue)
            font_style = pygame.font.SysFont("comicsansms", 25)
            message = font_style.render("You Lost! Wanna play again? Press P", True, red)
            display_window.blit(message, [display_width / 4, display_height / 3])

            # for displaying scores
            score = length_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms", 35)
            value = score_font.render("Your Score : " + str(score), True, green)
            display_window.blit(value, [display_width / 3, display_height / 5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snake_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                if event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True
        x1 += x1_change
        y1 += y1_change
        display_window.fill(black)
        pygame.draw.rect(display_window, green, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        # when the length of the snake exceeds, delete the snake_list which will end the game
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # when snake hits itself, game ends
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True
        snake(snake_block, snake_list)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


snake_game()
