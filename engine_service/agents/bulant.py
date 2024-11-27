# Author : Zin Lin Htun
# Bullet Ant class, type :: agent
from engine_service.agents.ant_agent import Agent
from engine_service.background.coordinate import Coordinate


class BulletAnt(Agent):
    health = 2
    status = 1
    name = ''
    rank = 1
    age = 1
    queen = False
    coord = Coordinate(0, 0)
    cat = "Minim"

    # Constructor
    def __init__(self, coord, idd, colony_id, name='JB', health=3, status=1, queen=False, scout=False,  cat="Minim"):
        super().__init__(coord, idd, colony_id, health, status, queen, scout)
        # setting values
        self.name = name
        self.health = health
        self.status = status
        self.queen = queen
        self.scout = scout
        self.cat = cat

        # species specific
        self.species = "BL"

        #  species specific role setting except scouting, that is done in the agent __base__ class
        if cat == "Minor":
            self.msg = "diplomatic"
            self._scan_reach = 2

        elif cat == "Major":
            self.msg = "aggressive"
            self._scan_reach = 5

        elif cat == "Mediae":
            self.msg = "allocation"
            self._scan_reach = 2

        else:
            if not self.scout:
                self.msg = "allocation"
                self._scan_reach = 1

    # scan environment
    def scan(self):
        return

    # attack other stuff
    def attack(self):
        return

    # leave pheromone trail
    def leave_pheromone(self):
        return
