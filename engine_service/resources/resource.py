# Author : Zin Lin Htun
# resource base class
from engine_service.background.coordinate import Coordinate


class Resource:
    portions = 0
    size = 0
    id = ""
    coord = Coordinate(0, 0)

    # Constructor
    def __init__(self, portions, size, coord, idd):
        self.portions = portions
        self.size = size
        self.coord = coord
        self.id = idd
