import pyglet
import worm
import obstacle
import collisionSolver

from pyglet.window import key

score = 0

window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

obstacles = set()
player = worm.Worm(x=10, y=10, batch=main_batch)
collision_solver = collisionSolver.CollissionSolver(player, obstacles)


def init():
    new_obstacle = obstacle.Obstacle(window, x=100, y=100, batch=main_batch)
    obstacles.add(new_obstacle)
    collision_solver.add_obstacles(obstacles)


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
    collision = collision_solver.collision_detection()
    if collision:
        global score
        score += 1
        print("hit " + str(score))
        collision.jump()
    player.update(dt)

if __name__ == "__main__":
    # Start it up!
    init()
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/120.0)
    # Tell pyglet to do its thing
    pyglet.app.run()
