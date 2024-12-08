# Author : Zin Lin Htun
# Leaf Cutter Ant class, type :: agent
from engine_service.agents import ant_agent


# Types : Minim, Minor, Scout, Mediae, Major


class LeafCutterAnt(ant_agent.Agent):

    # Constructor
    def __init__(self, coord, idd, colony_id, name='JB', health=2, status=1, queen=False, scout=False, soldier=False):
        super().__init__(coord, idd, colony_id, health, status, queen, scout)
        # set values
        self.name = name
        self.health = health
        self.status = status
        self.queen = queen
        self.scout = scout
        self.start = True
        self.soldier = soldier
        self.rank = 1

        # species specifics
        self.species = "LC"

        self._scan_reach = 2
        self.msg = "allocate"
        if self.scout:
            self.rank = 2

        elif self.queen:
            self.rank = 100

        elif self.soldier:
            self.rank = 3
