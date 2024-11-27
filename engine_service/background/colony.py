# Author  : Zin Lin Htun
# Colony Class

from engine_service.background.coordinate import Coordinate


class Colony:
    id = ""
    name = ""
    res_portion = 0
    ants = []
    coord = Coordinate(0, 0)
    pheromones = []
    scouts = []
    soldiers = []
    queen = None

    # Constructor
    def __init__(self, idd, name, res_portion, ants, coord=Coordinate(0, 0)):
        self.id = idd
        self.name = name
        self.res_portion = res_portion
        self.ants = ants
        self.coord = coord
        self.pheromones = []
        self.scouts = []
        self.soldiers = []
        self.queen = None

    # remove dead ants
    def remove_dead_ants(self):
        remove_list = []
        for ant in self.ants:
            if ant.health <= 0:
                remove_list.append(ant)

        for ant in remove_list:
            self.ants.remove(ant)