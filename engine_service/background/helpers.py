# Author : Zin Lin Htun
# Helpers static class
import math

from engine_service.background.colony import *
from engine_service.background.coordinate import Coordinate
from uuid import uuid4

from engine_service.resources.resource import Resource


class Helpers:
    def __init__(self):
        return

    # get unique id
    @staticmethod
    def get_id():
        return str(uuid4().hex)

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

        for ant in colony.soldiers:
            if ant.id == aid:
                return ant
        return None

    # find resource in resources
    @staticmethod
    def _find_resource(resources, rid=""):

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
        if colony_id != "":
            colony = Helpers._find_colony(colonies, colony_id)
            if colony != "":
                ant = Helpers._find_ant(colony, ant_id)

        if res_id != "":
            resource = Helpers._find_resource(resources, res_id)
        data_object = {'pheromone_id': pheromone_id, 'colony_id': colony_id,
                       'ant': ant, 'res': resource, 'coordinate': coord}

        return data_object

    # public method for finding ants
    @staticmethod
    def find_ant(colony=None, ant_id=""):
        return Helpers._find_ant(colony, ant_id)

    # public method for finding colony
    @staticmethod
    def find_colony(colonies=None, cid=""):
        return Helpers._find_colony(colonies, cid)

    # public method for finding colony index
    @staticmethod
    def find_colony_ind(colonies=None, cid=""):
        if colonies is None:
            colonies = [Colony(1, "ants-1", 0, [])]

            # find colony
        ind = None
        for colony in colonies:
            if colony.id == cid:
                return ind
            ind += 1
        return ind

    # public method for finding resource
    @staticmethod
    def find_resource_ind(resources=None, rid=""):
        if resources is None:
            resources = []

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

    # print grid
    @staticmethod
    def print_grid(grid: list[list[str]]):
        for row in grid:
            for cell in row:
                print(cell, end=' ')
            print(end='\n')

    # print grid in visual
    @staticmethod
    def visualize_grid(grid: list[list[str]]):
        for row in grid:
            for cell in row:
                data = cell.split(',')
                if cell == ",,,,,":
                    print("     ", end=' ')
                elif data[0] != "" and data[1] != "" and data[2] == "" and data[3] == "":
                    print("  ࿚  ", end=' ')
                elif data[1] != "":
                    if data[2] != "":
                        if data[4] == "3":
                            print("  🦗  ", end=' ')
                        else:
                            print("  🐜  ", end=' ')
                    else:
                        print("__O__", end=' ')
                elif data[3] != "":
                    if data[2] != "":
                        if data[4] == "3":
                            print("  🦗  ", end=' ')
                        else:
                            print("  🐜  ", end=' ')
                    else:
                        # print resource
                        if data[5] == "":
                            print("  🌲  ", end=' ')
                        elif data[5] == "1":
                            print("  💦  ", end=' ')
                        elif data[5] == "2":
                            print("  🍗  ", end=' ')
                        else:
                            print("  ❌  ", end=' ')

            print(end='\n')

        # update terminal
        print(flush=True)
