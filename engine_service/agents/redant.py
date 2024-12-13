# Author : Zin Lin Htun
# Red Ant class, type :: agent
from engine_service.agents import ant_agent


class RedAnt(ant_agent.Agent):

    # Constructor
    def __init__(self, coord, idd, colony_id, name='JB', health=2, status=1, queen=False, scout=False, cat="Forager"):
        super().__init__(coord, idd, colony_id, health, status, queen, scout)
        # set values
        self.name = name
        self.health = health
        self.status = status
        self.queen = queen
        self.scout = scout

        # species specifics
        self.species = "RD"

        #  species specific role setting except scouting, that is done in the agent __base__ class
        if cat == "Minor":
            self._scan_reach = 1
            self.damage = 0.5

        elif cat == "Major":
            self._scan_reach = 3

        elif cat == "Mediae":
            self._scan_reach = 2

        else:
            if not self.scout:
                self._scan_reach = 1

    def scan(self):
        return

    def attack(self):
        return

    def leave_pheromone(self):
        return
