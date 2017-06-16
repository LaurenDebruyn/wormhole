import pyglet


class Worm(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(Worm, self).__init__(img=pyglet.resource.image('worm.png'), *args, **kwargs)
        self.x_velocity = 10
        self.y_velocity = 10

    def update(self, dt):
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt
