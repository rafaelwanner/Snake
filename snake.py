import pygame

blue = (65, 200, 240)

class Snake():

    def __init__(self, size=1):
        self.size = size
        self.snake = [Part(400,200)]
        self.movement = (1, 0)

    def draw(self, screen):
        for part in self.snake:
            pygame.draw.rect(screen, blue, (part.x, part.y, part.dim, part.dim), 0)


    def move_left(self):
        if self.movement != (1, 0):
            self.movement = (-1, 0)

    def move_right(self):
        if self.movement != (-1, 0):
            self.movement = (1, 0)

    def move_up(self):
        if self.movement != (0, 1):
            self.movement = (0, -1)

    def move_down(self):
        if self.movement != (0, -1):
            self.movement = (0, 1)

    def move(self):
        head = self.snake[0]
        self.snake.insert(0, Part(head.x + self.movement[0]*head.dim/2, head.y + self.movement[1]*head.dim/2))
        self.snake.pop()

    def add(self):
        last_part = self.snake[-1]
        self.snake.append(Part(last_part.x + last_part.dim, last_part.y))


class Part():

    def __init__(self, x, y, dim=20):
        self.x = x
        self.y = y
        self.dim = dim

    def display(self, screen):
        pygame.draw.rect(screen, blue, (self.x, self.y, self.dim, self.dim), 0)
