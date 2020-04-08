import pygame

blue = (65, 200, 240)

class Snake():

    def __init__(self, size=1):
        self.size = size
        self.snake = [Part(400,200)]
        self.movement = (5, 0)

    def draw(self, screen):
        for part in self.snake:
            pygame.draw.rect(screen, blue, (part.x, part.y, part.dim, part.dim), 0)


    def move_left(self):
        if self.movement != (5, 0):
            self.movement = (-5, 0)

    def move_right(self):
        if self.movement != (-5, 0):
            self.movement = (5, 0)

    def move_up(self):
        if self.movement != (0, 5):
            self.movement = (0, -5)

    def move_down(self):
        if self.movement != (0, -5):
            self.movement = (0, 5)

    def move(self):
        for part in self.snake:
            part.x += self.movement[0]
            part.y += self.movement[1]

    def add(self):
        last_part = self.snake[-1]
        self.snake.append(Part(last_part.x + 20, last_part.y))

class Part():

    def __init__(self, x, y, dim=20):
        self.x = x
        self.y = y
        self.dim = dim

    def display(self, screen):
        pygame.draw.rect(screen, blue, (self.x, self.y, self.dim, self.dim), 0)
