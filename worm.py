import pyglet
import math


class Worm(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(Worm, self).__init__(img=pyglet.resource.image('worm.png'), *args, **kwargs)
        # self.scale = 0.5
        self.speed = 100
        self.x_velocity = 0
        self.y_velocity = 100
        self.orientation = 0
        self.rotation_speed = math.pi / 8

    def update(self, dt):
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt

    def turn_left(self):
        self.set_orientation(self.get_orientation() + self.get_rotation_speed())
        self.x_velocity = self.get_speed() * math.cos(self.get_orientation())
        self.y_velocity = self.get_speed() * math.sin(self.get_orientation())

    def turn_right(self):
        self.set_orientation(self.get_orientation() - self.get_rotation_speed())
        self.x_velocity = self.get_speed() * math.cos(self.get_orientation())
        self.y_velocity = self.get_speed() * math.sin(self.get_orientation())

    def get_speed(self):
        return self.speed

    def get_orientation(self):
        return self.orientation

    def set_orientation(self, angle):
        self.orientation = angle % (2*math.pi)

    def get_rotation_speed(self):
        return self.rotation_speed
