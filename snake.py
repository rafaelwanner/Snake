import pygame

blue = (65, 200, 240)

class Snake():

    def __init__(self, size=0):
        self.size = size
        self.snake = [Part(400,200)]
        self.movement = (1, 0)

    def draw(self, screen):
        for part in self.snake:
            pygame.draw.rect(screen, part.color, (part.x, part.y, part.dim, part.dim), 0)

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
        self.snake.insert(0, Part(head.x + self.movement[0]*head.dim, head.y + self.movement[1]*head.dim))
        self.snake.pop()

    def add(self):
        last_part = self.snake[-1]
        self.snake.append(Part(last_part.x + last_part.dim, last_part.y))
        self.size += 1

    def snake_length(self):
        return self.size

    def snake_overlap(self):
        head = self.snake[0]
        for part in self.snake[1:]:
            x_min = part.x - part.dim/2
            x_max = part.x + part.dim/2
            y_min = part.y - part.dim/2
            y_max = part.y + part.dim/2
            if x_min <= head.x <= x_max:
                if y_min <= head.y <= y_max:
                    index = self.snake.index(part)
                    del self.snake[index:self.size]
                    self.size = index
                    break


class Part():

    def __init__(self, x, y, dim=10, color=(0 ,0 ,0)):
        self.x = x
        self.y = y
        self.dim = dim
        self.color = color

    def display(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.dim, self.dim), 0)
