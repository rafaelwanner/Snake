import pygame
import random
from sys import exit
import pickle
from snake import *

pygame.init()

#loading high scores
try:
    with open('score.dat', 'rb') as file:
        high_score = pickle.load(file)
except:
    high_score = 0

#constant values
background_color = (139, 177, 167)
font_color = (255, 0, 0)
width = 800
height = 600
margin = 20

#music and sounds
pygame.mixer.music.load("game_music.wav")
pygame.mixer.music.play(-1)
eaten = pygame.mixer.Sound("food_eaten.wav")
dead = pygame.mixer.Sound("dead.wav")
#fonts
small_font = pygame.font.Font("font.ttf", 20)
large_font = pygame.font.Font("font.ttf", 55)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#checks if game is over (snake moved into wall)
def check_gameover():
    global high_score
    score = snake.snake_length() - 1
    head = snake.snake[0]
    if head.x > width or head.x < 0 or head.y < 0 or head.y > height:
        dead.play()
        if score > high_score:
            high_score = score
            with open('score.dat', 'wb') as file:
                pickle.dump(high_score, file)
        end = True
        while end:
            check_exit()
            if check_key_pressed():
                break

            snake.draw(screen)
            food.display(screen)
            #message 1
            msg = large_font.render("You lost!", -1, font_color)
            msg_pos = msg.get_rect(center=(width/2, height/3))
            screen.blit(msg, msg_pos)
            #message 2
            if high_score == score:
                msg = large_font.render("Congrats! New high score: " + str(high_score), -1, font_color)
                msg_pos = msg.get_rect(center=(width/2, height/2))
                screen.blit(msg, msg_pos)
            else:
                msg = large_font.render("Score: " + str(score) + "   " + "High score: " + str(high_score), -1, font_color)
                msg_pos = msg.get_rect(center=(width/2, height/2))
                screen.blit(msg, msg_pos)
            #message 3
            msg = small_font.render("Press any key to play again", -1, font_color)
            msg_pos = msg.get_rect(center=(width/2, 2*height/3))
            screen.blit(msg, msg_pos)

            pygame.display.update()
        game_loop()

#displays current score
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
            eaten.play()
            return True
    return False

#checks if user wants to quit the game
def check_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#gets new direction
def get_direction():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        snake.move_right()
    if keys[pygame.K_LEFT]:
        snake.move_left()
    if keys[pygame.K_UP]:
        snake.move_up()
    if keys[pygame.K_DOWN]:
        snake.move_down()

#checks if a key is pressed
def check_key_pressed():
    keys = pygame.key.get_pressed()
    for key in keys:
        if key == 1:
            return True
    return False

#main game loop
def game_loop():
    global snake
    snake = Snake()
    running = True
    food_gone = True
    while running:

        check_exit()
        get_direction()
        screen.fill(background_color)
        snake.draw(screen)

        #a new food spaws
        if food_gone:
            x = random.randint(margin, width - margin)
            y = random.randint(margin, height - margin)
            global food
            food = Part(x, y, color=(234, 50, 111))
            snake.add()
            food_gone = False

        food.display(screen)
        snake.move()
        food_gone = food_eaten()
        check_gameover()
        snake.snake_overlap()
        display_score()
        pygame.display.update()
        pygame.time.wait(20)

game_loop()
