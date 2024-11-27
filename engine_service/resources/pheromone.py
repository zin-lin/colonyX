# Author : Zin Lin Htun
# Pheromone class
from engine_service.background.coordinate import Coordinate


class Pheromone:
    ant_id = ""
    coord = Coordinate(0, 0)

    # Constructor
    def __init__(self, colony_id, ant_id, coord):
        self.ant_id = ant_id
        self.colony_id = colony_id
        self.coord = coord
