import pyglet
import math

from pyglet.window import key


class Worm(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(Worm, self).__init__(img=pyglet.resource.image('worm.png'), *args, **kwargs)
        self.scale = 0.5
        self.x_velocity = 100
        self.y_velocity = 100

        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt

    def turn_left(self):
        self.set_angle(self.get_angle() + self.get_turning_angle())
        self.x_velocity = self.get_speed() * math.cos(self.get_angle())
        self.y_velocity = self.get_speed() * math.sin(self.get_angle())

    def turn_right(self):
        self.set_angle(self.get_angle() - self.get_turning_angle())
        self.x_velocity = self.get_speed() * math.cos(self.get_angle())
        self.y_velocity = self.get_speed() * math.sin(self.get_angle())

    def get_speed(self):
        return math.sqrt(math.pow(self.x_velocity, 2) + math.pow(self.y_velocity, 2))

    def get_angle(self):
        return self.angle

    def set_angle(self, new_angle):
        self.angle = new_angle % (2*math.pi)

    angle = 0.0

    def get_turning_angle(self):
        return self.turning_angle

    turning_angle = math.pi / 16
