from pico2d import *
import game_world
import game_framework


class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y, self.velocity = 800, 250, 250
        self.direction = 1

    def get_bb(self):
        # fill here
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.direction == 1:
            self.x += self.velocity * game_framework.frame_time
            if self.x > 1500:
                self.direction = -1
        elif self.direction == -1:
            self.x -= self.velocity * game_framework.frame_time
            if self.x < 100:
                self.direction = 1

    def stop(self):
        pass
