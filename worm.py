import wormSegment
import math
import random


class Worm:

    def __init__(self, screen, x_pos, y_pos, batch_arg):
        self.screen = screen
        self.width = 51
        self.height = 50
        self.x_position = x_pos
        self.y_position = y_pos
        self.batch = batch_arg
        self.x_velocity = 0
        self.y_velocity = 100
        self.speed = 100
        self.orientation = 0
        self.rotation_speed = math.pi / 8
        self.segments = list()
        self.segments.append(wormSegment.WormSegment(self.x_velocity, self.y_velocity, self.speed,
                                                     x=x_pos, y=y_pos, batch=self.batch))

    def update(self, dt):
        self.x_position = self.segments[0].x
        self.y_position = self.segments[0].y
        self.segments[0].update_velocity(self.x_velocity, self.y_velocity)
        self.segments[0].move(dt)

    def restart(self):
        new_x = random.randrange(0, self.screen.width)
        new_y = random.randrange(0, self.screen.height)
        self.segments = []
        self.segments.append(wormSegment.WormSegment(self.x_velocity, self.y_velocity, self.speed,
                                                     x=new_x, y=new_y, batch=self.batch))

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

    def get_segments(self):
        return self.segments

    def add_segment(self):
        last_index = len(self.segments) - 1
        self.segments[last_index].add_segment()
