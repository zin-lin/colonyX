# Author : Zin Lin Htun
# Environment class
import random

from engine_service.agents.ant_agent import Agent
from engine_service.background.colony import Colony
from engine_service.background.coordinate import Coordinate
from engine_service.background.helpers import Helpers
from engine_service.resources.leaf import Leaf
from engine_service.resources.pheromone import Pheromone
from engine_service.resources.resource import Resource
from engine_service.resources.tree import Tree
from engine_service.resources.meat import Meat
from engine_service.resources.water import Water
from engine_service.resources.obstacle import Obstacle
from random import *


class Environment:
    grid = []
    size = (20, 20)
    res = 0

    # deal with a colony on grid
    def _deal_colony(self, colony):
        x = colony.coord.x
        y = colony.coord.y
        string = self.grid[y][x]
        data = string.split(',')
        data[1] = colony.id
        string = ','.join(data)
        self.grid[y][x] = string

    # deal with an ant on the grid
    def _deal_ant(self, ant, colony):
        x = ant.coord.x
        y = ant.coord.y
        string = self.grid[y][x]
        data = string.split(',')
        data[1] = colony.id
        # print('data[1]' + str(colony.id))
        data[2] = ant.id
        data[4] = str(ant.rank)
        new = ','.join(data)
        self.grid[y][x] = new

    # deal with a pheromone on the grid
    def _deal_pheromone(self, phe):
        x = phe.coord.x
        y = phe.coord.y
        string = self.grid[y][x]
        data = string.split(',')
        data[0] = phe.ant_id
        data[1] = phe.colony_id
        new = ','.join(data)
        self.grid[y][x] = new

    # deal with a piece of resource on the grid
    def _deal_resource(self, resource):
        x = resource.coord.x
        y = resource.coord.y
        string = self.grid[y][x]
        data = string.split(',')
        data[3] = resource.id
        if type(resource) is Tree:
            data[5] = ''
        elif type(resource) is Water:
            data[5] = '1'
        elif type(resource) is Meat:
            data[5] = '2'
        else:
            data[5] = '3'
        new = ','.join(data)
        self.grid[y][x] = new

    # initialisation of state
    def _init_state(self, size_x, size_y):
        self.grid.clear()
        for i in range(size_y):
            self.grid.append([])
            for j in range(size_x):
                self.grid[i].append(",,,,,")
        self.size = (size_x, size_y)

    # Constructor
    def __init__(self, size_x=20, size_y=20, res_size=1):
        # add 0s to every grid point
        self._init_state(size_x, size_y)
        self.obstacles = []
        self.res_size = res_size
        self.res = res_size

    # Add resources to the environment
    def add_resource(self, resources: list[Resource or Leaf or Tree]):
        for resource in resources:
            self._deal_resource(resource)
            self.res_size += 1

    # Add colonies to the environment
    def add_colonies(self, colonies: list[Colony]):
        for colony in colonies:
            self._deal_colony(colony)

    # cleaning up resources and ants
    # @deprecated
    def clean_state(self, colonies: list[Colony], resources: list[Resource or Leaf or Tree]):
        for y in self.grid:
            for string in y:
                data = string.split(',')
                res_ind = Helpers.find_resource_ind(data[3])
                colony = Helpers.find_colony(colonies, data[1])
                ant = Helpers.find_ant(colony, data[2])
                col_ind = Helpers.find_colony_ind(colonies, data[1])

                # fix grid's string issues/problems
                if res_ind is None:
                    data[3] = ""

                if ant is None:
                    data[1] = ""
                    data[2] = ""

                if colony is None:
                    data[2] = ""

                # fix reference issues
                if ant is not None:
                    colony.ants.remove(ant)

                if colony is not None:
                    colonies.remove(colony)

    # Manage State
    def manage_state(self, colonies, resources):
        self._init_state(self.size[0], self.size[1])

        for colony in colonies:
            self._deal_colony(colony)
            # deal with ants

            ants = colony.ants
            pheromones = colony.pheromones
            for phe in pheromones:
                self._deal_pheromone(phe)

            for ant in ants:
                if ant.health > 0:
                    # print(colony.coord.x)
                    if ant.coord.x != colony.coord.x or ant.coord.y != colony.coord.y:
                        self._deal_ant(ant, colony)
                else:
                    try:
                        colony.ants.remove(ant)
                    except:
                        print ('m9')

            for ant in colony.scouts:
                # print(colony.coord.x)
                if ant.coord.x != colony.coord.x or ant.coord.y != colony.coord.y:
                    self._deal_ant(ant, colony)

            for ant in colony.soldiers:
                if ant.health > 0:
                    # print(colony.coord.x)
                    if ant.coord.x != colony.coord.x or ant.coord.y != colony.coord.y:
                        self._deal_ant(ant, colony)
                else:
                    colony.soldiers.remove(ant)

        for resource in resources:
            self._deal_resource(resource)

        # add random obstacles
        self.add_obstacles()

        for ob in self.obstacles:
            self._deal_resource(ob)  # obstacle are of resource type

        # add new resources if necessary
        self.add_random_resources(resources)
        # call block of code again to deal with added resources
        for resource in resources:
            self._deal_resource(resource)

    # Test Pheromone method
    def test_add_pheromone(self, colony, colony2, colony3):
        count_x = 6
        count_y = 7

        phe2 = [
            Pheromone(colony2.id, "22", Coordinate(16, 18)),
            Pheromone(colony2.id, "22", Coordinate(16, 11)),
            Pheromone(colony2.id, "22", Coordinate(16, 12)),
            Pheromone(colony2.id, "22", Coordinate(16, 13)),
            Pheromone(colony2.id, "22", Coordinate(16, 14)),
            Pheromone(colony2.id, "22", Coordinate(16, 15)),
            Pheromone(colony2.id, "22", Coordinate(16, 16)),
            Pheromone(colony2.id, "22", Coordinate(16, 17)),
            Pheromone(colony2.id, "22", Coordinate(16, 19)),
            Pheromone(colony2.id, "22", Coordinate(16, 20)),
            Pheromone(colony2.id, "22", Coordinate(16, 21)),
            Pheromone(colony2.id, "22", Coordinate(16, 22)),
            Pheromone(colony2.id, "28", Coordinate(15, 23)),
            Pheromone(colony2.id, "28", Coordinate(14, 23)),
            Pheromone(colony2.id, "28", Coordinate(13, 23)),
            Pheromone(colony2.id, "28", Coordinate(12, 23)),
        ]

        phe = [
            Pheromone(colony.id, "23", Coordinate(6, 20)),
            Pheromone(colony.id, "23", Coordinate(7, 19)),
            Pheromone(colony.id, "23", Coordinate(8, 18)),
            Pheromone(colony.id, "23", Coordinate(9, 17)),
            Pheromone(colony.id, "23", Coordinate(10, 16)),
            Pheromone(colony.id, "23", Coordinate(11, 15)),
            Pheromone(colony.id, "23", Coordinate(12, 14)),
            Pheromone(colony.id, "23", Coordinate(13, 13)),
            Pheromone(colony.id, "23", Coordinate(14, 12)),
            Pheromone(colony.id, "23", Coordinate(15, 11)),
            Pheromone(colony.id, "23", Coordinate(6, 21)),
            Pheromone(colony.id, "23", Coordinate(6, 22)),
            Pheromone(colony.id, "23", Coordinate(6, 23)),
            Pheromone(colony.id, "23", Coordinate(6, 24)),
            Pheromone(colony.id, "23", Coordinate(6, 25)),
            Pheromone(colony.id, "23", Coordinate(6, 26))
        ]

        phe3 = [
            Pheromone(colony3.id, "24", Coordinate(21, 15)),
            Pheromone(colony3.id, "24", Coordinate(20, 14)),
            Pheromone(colony3.id, "24", Coordinate(19, 13)),
            Pheromone(colony3.id, "24", Coordinate(18, 12)),
            Pheromone(colony3.id, "24", Coordinate(17, 11)),
            Pheromone(colony3.id, "24", Coordinate(22, 16)),
            Pheromone(colony3.id, "24", Coordinate(22, 17)),
            Pheromone(colony3.id, "24", Coordinate(22, 18)),
            Pheromone(colony3.id, "24", Coordinate(22, 19)),
            Pheromone(colony3.id, "24", Coordinate(22, 20)),
            Pheromone(colony3.id, "24", Coordinate(22, 21)),
            Pheromone(colony3.id, "24", Coordinate(22, 22)),
            Pheromone(colony3.id, "24", Coordinate(22, 23)),
            Pheromone(colony3.id, "24", Coordinate(22, 24)),
        ]

        colony.pheromones = phe
        colony2.pheromones = phe2
        colony3.pheromones = phe3

        for p in phe:
            self._deal_pheromone(p)

        for p in phe2:
            self._deal_pheromone(p)

        for p in phe3:
            self._deal_pheromone(p)

    # get empty
    def _get_empties(self):
        emp = []
        # get emptys
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == ",,,,,":
                    emp.append({'y': i, 'x': j})
        return emp

    # add random obstacles
    def _add_random_obstacles(self):
        ans = []  # answer array
        length = len(self.grid)
        emp = self._get_empties()

        for i in range(length//2):
            rand_index = randrange(0, len(emp))
            ran = Obstacle(Helpers.get_id(), Coordinate(emp[rand_index]['x'], emp[rand_index]['y']), 10)
            ans.append(ran)
        print(len(ans))
        return ans

    # deal with random obstacles
    def add_obstacles(self):
        obstacles = self._add_random_obstacles()
        self.obstacles = []
        # print(len(obstacles))
        for obstacle in obstacles:
            self.obstacles.append(obstacle)

    # deal with randomly adding resources
    def add_random_resources(self, resources):
        emp = self._get_empties()
        ans = []
        num = self.res
        length = len(resources)
        diff = num - length
        for i in range(diff):
            rand_index = randrange(0, len(emp))
            ran_type = randrange(0, 3)
            ran_amount = randrange(30, 500)
            ran = None
            if ran_type == 0:
                ran = Tree(Helpers.get_id(), Coordinate(emp[rand_index]['x'], emp[rand_index]['y']), ran_amount)

            elif ran_type == 1:
                ran = Water(Helpers.get_id(), Coordinate(emp[rand_index]['x'], emp[rand_index]['y']), ran_amount)

            else:
                ran = Meat(Helpers.get_id(), Coordinate(emp[rand_index]['x'], emp[rand_index]['y']), ran_amount)
            resources.append(ran)
