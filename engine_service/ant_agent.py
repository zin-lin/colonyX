# Author : Zin Lin Htun
# agent class
from engine_service.coordinate import Coordinate


class Agent:
    health = 2
    status = 1
    name = ''
    rank = 1
    age = 1
    queen = False
    scout = True
    coord = Coordinate(0, 0)

    # Constructor
    def __init__(self, coord, idd, colony_id, health=3, status=1, queen=False, scout=False):
        self.coord = coord
        self.id = idd
        self.colony_id = colony_id
        self.health = health
        self.status = status
        self.scout = scout
        self.queen = queen

    # move around
    def move(self, msg):
        if msg == "move up":
            self.coord.move_up()

        elif msg == "move down":
            self.coord.move_down()

        elif msg == "move left":
            self.coord.move_left()

        elif msg == "move right":
            self.coord.move_right(1)

        elif msg == "move left up":
            self.coord.move_left_up(1)

        elif msg == "move right up":
            self.coord.move_right_up(1)

        elif msg == "move left down":
            self.coord.move_left_down(1)

        elif msg == "move right down":
            self.coord.move_right_down(1)

    # scan around environment
    def scan(self):
        return

    # attack other agents
    def attack(self):
        return

    # leave pheromone trial
    def leave_pheromone(self):
        return
