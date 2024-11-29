# Author : Zin Lin Htun
# Leaf Cutter Ant class, type :: agent
from engine_service.agents import ant_agent


# Types : Minim, Minor, Scout, Mediae, Major


class LeafCutterAnt(ant_agent.Agent):

    # Constructor
    def __init__(self, coord, idd, colony_id, name='JB', health=2, status=1, queen=False, scout=False, cat="Minim"):
        super().__init__(coord, idd, colony_id, health, status, queen, scout)
        # set values
        self.name = name
        self.health = health
        self.status = status
        self.queen = queen
        self.cat = cat
        self.scout = scout
        self.start = True

        # species specifics
        self.species = "LC"

        self._scan_reach = 1
        self.msg = "allocate"
