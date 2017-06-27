import pyglet
import queue
import math


class WormSegment(pyglet.sprite.Sprite):

    def __init__(self, x_vel, y_vel, speed, *args, **kwargs):
        super(WormSegment, self).__init__(img=pyglet.resource.image('worm.png'), *args, **kwargs)
        self.x_velocity = x_vel
        self.y_velocity = y_vel
        self.speed = speed
        self.trail = queue.Queue(10)
        for i in range(0, 10):
            self.trail.put((self.x - speed * i, self.y - speed * i))
        self.next_segment = None

    def update_velocity(self, x_vel, y_vel):
        self.x_velocity = x_vel
        self.y_velocity = y_vel

    def move(self, dt):
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt

    def add_segment(self):
        if self.x_velocity == 0:
            orientation = 0
        else:
            orientation = (math.pi * 2 + math.atan(self.y_velocity / self.x_velocity)) % (math.pi * 2)
        print("orientation: " + str(orientation))
        x_orientation = math.cos(orientation)
        y_orientation = math.sin(orientation)
        print("x orientation: " + str(x_orientation) + "  y orientation: " + str(y_orientation))
        new_x = self.x + self.width if x_orientation < 0 else self.x - self.width
        new_y = self.y + self.height if y_orientation < 0 else self.y - self.height
        new_segment = WormSegment(self.x_velocity, self.y_velocity, self.speed,
                                  x=new_x, y=new_y, batch=self.batch)
        self.next_segment = new_segment

    def get_next_segment(self):
        return self.next_segment

