# Author : Zin Lin Htun
# Helpers static class
import math

from engine_service.background.colony import *
from engine_service.resources.resource import Resource
from engine_service.background.coordinate import Coordinate


class Helpers:
    def __init__(self):
        return

    # find colony from colonies
    @staticmethod
    def _find_colony(colonies=None, cid=""):
        if colonies is None:
            colonies = [Colony(1, "ants-1", 0, [])]

        # find colony
        for colony in colonies:
            if colony.id == cid:
                return colony
        return None

    # find ants in a colony
    @staticmethod
    def _find_ant(colony=None, aid=""):
        if colony is None:
            colony = Colony(1, "ants-1", 0, [])

        # find colony
        for ant in colony.ants:
            if ant.id == aid:
                return ant
        return None

    # find resource in resources
    @staticmethod
    def _find_resource(resources=None, rid=""):
        if resources is None:
            resources = [Resource(3, 3, Coordinate(0, 0), "")]

        # find colony
        for res in resources:
            if res.id == rid:
                return res
        return None

    # process found data from grid
    @staticmethod
    def process_data(string, colonies=None, resources=None, coord=None):
        pheromone_id = ""
        ant = None   # if ant
        colony = None
        resource = None

        # set colony if None
        if colonies is None:
            colonies = [Colony(1, "ants-1", 0,  [])]

        data = string.split(",")  # split using ,
        pheromone_id = data[0]
        colony_id = data[1]
        ant_id = data[2]
        res_id = data[3]

        # find ant if exist
        if colony_id is not "":
            colony = Helpers._find_colony(colonies, colony_id)
            if colony is not "":
                ant = Helpers._find_ant(colony, ant_id)

        if res_id is not "":
            resource = Helpers._find_resource(resources, res_id)

        return {'pheromone_id': pheromone_id, 'colony_id': colony_id, 'ant': ant, 'resource': resource, 'coord': coord}

    # public method for finding ants
    @staticmethod
    def find_ant(colony=None, ant_id=""):
        return Helpers._find_ant(colony, ant_id)

    # public method for finding resource
    @staticmethod
    def find_resource(resources=None, rid=""):
        if resources is None:
            resources = [Resource(3, 3, Coordinate(0, 0), "")]

        # find colony
        ind = 0
        for res in resources:
            if res.id == rid:
                return ind
            ind += 1
        return None

    # finding euclidian distances between the two coordinates
    @staticmethod
    def euclidian(a: Coordinate, b: Coordinate):
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)
        # Compute the Euclidean distance
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance

        
