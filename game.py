import pygame
import random
from snake import *

black = (0, 0, 0)
height = 800
width = 600
pygame.init()

screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("Snake Game")

def eat():
    x_min = food.x - food.dim/2
    x_max = food.x + food.dim/2
    y_min = food.y - food.dim/2
    y_max = food.y + food.dim/2
    pos = snake.snake[0]
    if x_min <= pos.x <= x_max:
        if y_min <= pos.y <= y_max:
            return True
    return False


snake = Snake()
running = True
start = True
eaten = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        snake.move_right()
    if keys[pygame.K_LEFT]:
        snake.move_left()
    if keys[pygame.K_UP]:
        snake.move_up()
    if keys[pygame.K_DOWN]:
        snake.move_down()

    screen.fill(black)
    snake.draw(screen)

    if eaten:
        x = random.randint(20, height - 20)
        y = random.randint(20, width - 20)
        food = Part(x, y)
        snake.add()
        eaten = False

    eaten = eat()
    food.display(screen)
    snake.move()





    pygame.display.update()
