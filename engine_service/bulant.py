# Author : Zin Lin Htun
# Bullet Ant class, type :: agent
import ant_agent
import coordinate


class BulletAnt(ant_agent.Agent):
    health = 2
    status = 1
    name = ''
    rank = 1
    age = 1
    queen = False
    coord = coordinate.Coordinate(0, 0)

    def __init__(self, coord, idd, colony_id, name='JB', health=3, status=1, queen=False, scout=False):
        super().__init__(coord, idd, colony_id)
        self.name = name
        self.health = health
        self.status = status
        self.queen = queen
        self.scout = scout

    def move(self, msg="move up"):
        if msg == "move up":
            self.coord.move_up(3)

        elif msg == "move down":
            self.coord.move_down(3)

        elif msg == "move left":
            self.coord.move_left(3)

        elif msg == "move right":
            self.coord.move_right(3)

        elif msg == "move left up":
            self.coord.move_left_up(3)

        elif msg == "move right up":
            self.coord.move_right_up(3)

        elif msg == "move left down":
            self.coord.move_left_down(3)

        elif msg == "move right down":
            self.coord.move_right_down(3)

    # scan environment
    def scan(self):
        return

    # attack other stuff
    def attack(self):
        return

    # leave pheromone trail
    def leave_pheromone(self):
        return
