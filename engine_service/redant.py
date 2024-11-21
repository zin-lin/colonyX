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

    def __init__(self, coord, name='JB', health=2, status=1, queen=False):
        super().__init__(coord)
        self.name = name
        self.health = health
        self.status = status
        self.queen = queen

    def move(self):
        return

    def scan(self):
        return

    def attack(self):
        return

    def leave_pheromone(self):
        return
