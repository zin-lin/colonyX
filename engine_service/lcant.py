# Author : Zin Lin Htun
# Leaf Cutter Ant class, type :: agent
import ant_agent
# Types : Minim, Minor, Scout, Mediae, Major


class LeafCutterAnt(ant_agent.Agent):
    health = 2
    status = 1
    name = ''
    rank = 1
    age = 1
    queen = False
    scout = True
    cat = ""

    # Constructor
    def __init__(self, coord, name='JB', health=2, status=1, queen=False, cat="Minim"):
        super().__init__(coord)
        self.name = name
        self.health = health
        self.status = status
        self.queen = queen
        self.cat = cat

    def move(self, msg="move up"):
        if msg == "move up":
            self.coord.move_up(2)

        elif msg == "move down":
            self.coord.move_down(2)

        elif msg == "move left":
            self.coord.move_left(2)

        elif msg == "move right":
            self.coord.move_right(2)

        elif msg == "move left up":
            self.coord.move_left_up(2)

        elif msg == "move right up":
            self.coord.move_right_up(2)

        elif msg == "move left down":
            self.coord.move_left_down(2)

        elif msg == "move right down":
            self.coord.move_right_down(2)
