import pyglet
import worm


window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

player = worm.Worm(x=200, y=200, batch=main_batch)


def init():
    score = 0


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    player.update(dt)

if __name__ == "__main__":
    # Start it up!
    init()
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/120.0)
    # Tell pygle to do its thing
    pyglet.app.run()

