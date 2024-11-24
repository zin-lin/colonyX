# Author : Zin Lin Htun
# agent class
from engine_service.background.coordinate import Coordinate
from engine_service.resources.leaf import *
from engine_service.background.knowledge import *
from engine_service.resources.tree import Tree
from uuid import uuid4


def get_id():
    return str(uuid4().hex)


class Agent:
    #  attributes
    health = 2
    status = 1
    name = ''
    rank = 1
    age = 1
    damage = 0
    id = None

    # flags
    queen = False  # if queen/female
    scout = False  # if a scout type, scout cannot grow to other categories, cannot carry food, but can drop pheromone
    res = None  # null
    species = None

    # communication
    coord = Coordinate(0, 0)
    msg = ""  # broadcasting message
    _knowledge = None
    _scan_reach = 1  # step, this will be used in scanning, attacking and moving

    # Constructor
    def __init__(self, coord, idd, colony_id, health=3, status=1, queen=False, scout=False):
        self.coord = coord
        self.id = idd
        self.colony_id = colony_id
        self.health = health
        self.status = status
        self.scout = scout
        self.queen = queen

        if self.scout:
            self._scan_reach = 4

    # move around
    def _move(self, coord: Coordinate):
        msg = ""
        x1 = self.coord.x
        y1 = self.coord.y

        x2 = coord.x
        y2 = coord.y

        # creating command message
        if x2 > x1 and y2 > y1:
            msg = "move right up"
        elif x2 < x1 and y2 < y1:
            msg = "move left down"
        elif x2 == x1 and y2 > y1:
            msg = "move up"
        elif x2 == x1 and y2 < y1:
            msg = "move down"
        elif x2 < x1 and y2 > y1:
            msg = "move left up"
        elif x2 > x1 and y2 < y1:
            msg = "move right down"
        elif x2 > x1 and y2 == y1:
            msg = "move right"
        else:
            msg = "move left"

        # commands
        if msg == "move up":
            self.coord.move_up(self._scan_reach)

        elif msg == "move down":
            self.coord.move_down(self._scan_reach)

        elif msg == "move left":
            self.coord.move_left(self._scan_reach)

        elif msg == "move right":
            self.coord.move_right(self._scan_reach)

        elif msg == "move left up":
            self.coord.move_left_up(self._scan_reach, self._scan_reach)

        elif msg == "move right up":
            self.coord.move_right_up(self._scan_reach, self._scan_reach)

        elif msg == "move left down":
            self.coord.move_left_down(self._scan_reach, self._scan_reach)

        elif msg == "move right down":
            self.coord.move_right_down(self._scan_reach, self._scan_reach)

    # scan around environment
    def _scan(self, colonies, resources, grid):

        x = self.coord.x
        y = self.coord.y
        coords = []
        msgs = []
        if grid == "":
            grid = [[], []]

        range_i = (self._scan_reach * 2) + 1
        range_j = (self._scan_reach * 2) + 1
        neg = -self._scan_reach
        for i in range(range_i):
            for j in range(range_j):
                try:
                    data = grid[neg+i+y][neg+j+x]
                    msgs.append(data)
                    coords.append((x, y))
                except IndexError as e:
                    continue
        self._knowledge = Knowledge(msgs, self.msg, colonies, resources, coords)

    # attack other agents
    def _attack(self):
        return

    # leave pheromone trial
    def _leave_pheromone(self):
        return

    # acquire  resources
    def _acquire_resources(self, resource: Resource or Leaf or Tree, resources: list[Resource or Leaf or Tree]):
        if type(resource) is Tree:
            self.res = Leaf(self.coord, self.rank*4, self.rank, id=get_id())  # portion is rank *4 while
            # size is the same as # rank, this is because ant can easily carry 4 portions of food
            resource.leaf_count -= self.rank
        else:
            self.res = resource
            resources.pop(Helpers.find_resource(resources, resource.id))

    # This will be the agent's decision based on the agent knowledge
    def perform_turn(self, colonies, resources, grid=""):
        self._scan(grid,  colonies, resources)  # assign knowledge

        # data management
        ants = []
        res = []
        pheromone = []

        know_data = self._knowledge.knowledge_data
        for data in know_data:
            if data['pheromone_id'] == self.colony_id and data['ant'] is None and data['res'] is None:
                pheromone.append(data)

            if data['ant'] is not None:
                ants.append(data)

            if data['res'] is not None:
                ants.append(data)

        # attack decision
        # acquire decision
        should_acquire = None
        try:
            should_acquire = res[0]
        except IndexError as e:
            should_acquire = None

        self._acquire_resources(should_acquire, resources)

        # move decision
        max_phe_index = 0
        max_dis = -1
        index = 0
        for phe in pheromone:
            dis = Helpers.euclidian(phe['coordinate'], self.coord)
            if dis > max_dis:
                max_dis = dis
                max_phe_index = index

            index += 1
        should_move_coord = pheromone[index]
        self._move(should_move_coord)  # move it!  move it!


