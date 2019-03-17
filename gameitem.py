import random

class GameItem:

    def __init__(self, x=100, y=100):
        self.x = x
        self.y = y

        self.max_rand_change = 50

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def move_random(self):
        max_delta = self.max_rand_change
        self.move(random.randint(-max_delta, max_delta), random.randint(-max_delta, max_delta))

    def get_coordinates(self):
        return self.x, self.y
