# Author  : Zin Lin Htun
# Colony Class
from engine_service.background.coordinate import Coordinate


class Colony:
    id = ""
    name = ""
    res_portion = 0
    ants = []
    coord = Coordinate(0, 0)

    # Constructor
    def __init__(self, idd, name, res_portion, ants, coord=Coordinate(0, 0)):
        self.id = idd
        self.name = name
        self.res_portion = res_portion
        self.ants = ants
        self.coord = coord
