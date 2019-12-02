import random
from pico2d import *
import game_world
import game_framework
import main_state


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball41x41.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x, self.y = random.randint(0, 1800-1), random.randint(0, 1100-1)

    def get_bb(self):
        # fill here
        return self.real_x - 20, self.real_y - 20, self.real_x + 20, self.real_y + 20

    def set_center_object(self):
        pass

    def draw(self):
        self.image.draw(self.real_x, self.real_y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        boy = main_state.get_boy()
        self.real_x = self.x - boy.bg.window_left
        self.real_y = self.y - boy.bg.window_bottom
        pass

    def stop(self):
        pass