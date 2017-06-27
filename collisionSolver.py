from math import sqrt, pow


class CollissionSolver:

    def __init__(self, player_arg, obstacles_arg=None):
        self.obstacles = set()
        if obstacles_arg:
            for obstacle in obstacles_arg:
                self.obstacles.add(obstacle)
        self.player = player_arg

    def collision_detection_player_square(self, obstacle):
        for segment in self.player.get_segments():
            if obstacle.x - segment.width < segment.x < obstacle.x + obstacle.width and \
                   obstacle.y - segment.height < segment.y < obstacle.y + obstacle.height:
                return True
        return False

    def collision_detection(self):
        for obstacle in self.obstacles:
            if self.collision_detection_player_square(obstacle):
                return obstacle
        return None

    def distance(self, other):
        return sqrt(pow(self.player.x - other.x, 2) + pow(self.player.y - other.y, 2))

    def add_obstacles(self, new_obstacles):
        for new_obstacle in new_obstacles:
            if new_obstacle not in self.obstacles:
                self.obstacles.add(new_obstacle)
            else:
                return False

        return True

    def remove_obstacle(self, old_obstacle):
        if old_obstacle in self.obstacles:
            self.obstacles.remove(old_obstacle)
            return True
        return False
