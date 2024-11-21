# Author : Zin Lin Htun
# Red Ant class, type :: agent
import ant_agent


class RedAnt(ant_agent.Agent):
    health = 2
    status = 1
    name = ''
    rank = 1
    age = 1
    queen = False

    def __init__(self, coord, idd, colony_id, name='JB', health=2, status=1, queen=False, scout=False):
        super().__init__(coord, idd, colony_id)
        self.name = name
        self.health = health
        self.status = status
        self.queen = queen
        self.scout = scout

    def move(self):
        return

    def scan(self):
        return

    def attack(self):
        return

    def leave_pheromone(self):
        return
