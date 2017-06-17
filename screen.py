import pyglet
import worm

from pyglet.window import key

window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

player = worm.Worm(x=10, y=10, batch=main_batch)


def init():
    score = 0


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        player.turn_left()
    if symbol == key.RIGHT:
        player.turn_right()


def update(dt):
    player.update(dt)

if __name__ == "__main__":
    # Start it up!
    init()
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/120.0)
    # Tell pyglet to do its thing
    pyglet.app.run()

