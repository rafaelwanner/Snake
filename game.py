import pygame
import random
from sys import exit
from snake import *

pygame.init()

#constant values
background_color = (139, 177, 167)
font_color = (255, 0, 0)
width = 800
height = 600
margin = 20

#fonts
small_font = pygame.font.Font("font.ttf", 20)
large_font = pygame.font.Font("font.ttf", 55)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#checks if snake ate the food
def eat():
    x_min = food.x - food.dim/2
    x_max = food.x + food.dim/2
    y_min = food.y - food.dim/2
    y_max = food.y + food.dim/2
    head = snake.snake[0]
    if x_min <= head.x <= x_max:
        if y_min <= head.y <= y_max:
            return True
    return False

def check_gameover():
    head = snake.snake[0]
    if head.x > width or head.x < 0 or head.y < 0 or head.y > height:
        end = True
        while end:
            get_key_input()
            snake.draw(screen)
            food.display(screen)
            screen.blit(large_font.render("You loose!", -1, font_color), (275, 200))
            screen.blit(large_font.render("Score: " + str(snake.snake_length() - 1), -1, font_color), (300, 320))
            pygame.display.update()

def display_score():
    text = small_font.render("Score: " + str(snake.snake_length() - 1), -1, font_color)
    screen.blit(text, (10, 10))


def food_eaten():
    x_min = food.x - food.dim/2
    x_max = food.x + food.dim/2
    y_min = food.y - food.dim/2
    y_max = food.y + food.dim/2
    head = snake.snake[0]
    if x_min <= head.x <= x_max:
        if y_min <= head.y <= y_max:
            return True
    return False

#checks for key input
def get_key_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        snake.move_right()
    if keys[pygame.K_LEFT]:
        snake.move_left()
    if keys[pygame.K_UP]:
        snake.move_up()
    if keys[pygame.K_DOWN]:
        snake.move_down()

snake = Snake()
running = True
food_gone = True
while running:

    get_key_input()
    screen.fill(background_color)
    snake.draw(screen)

    #a new food spaws
    if food_gone:
        x = random.randint(margin, width - margin)
        y = random.randint(margin, height - margin)
        food = Part(x, y, color=(234, 50, 111))
        snake.add()
        food_gone = False

    food.display(screen)
    snake.move()
    check_gameover()
    display_score()
    food_gone = food_eaten()
    pygame.display.update()
    pygame.time.wait(20)
