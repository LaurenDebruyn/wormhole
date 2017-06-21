import pyglet
import random


class Obstacle(pyglet.sprite.Sprite):

    def __init__(self, screen, *args, **kwargs):
        super(Obstacle, self).__init__(img=pyglet.resource.image("obstacle.png"), *args, **kwargs)
        self.screen = screen

    def jump(self):
        r = random.Random()
        new_x = r.randint(0, self.screen.width - self.width)
        new_y = r.randint(0, self.screen.height - self.height)
        self.set_position(new_x, new_y)
