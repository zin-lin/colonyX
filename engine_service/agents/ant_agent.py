# Author : Zin Lin Htun
# agent class
from engine_service.background.coordinate import Coordinate
from engine_service.resources.leaf import *
from engine_service.background.knowledge import *
from engine_service.resources.tree import Tree
from uuid import uuid4
import random

def get_id():
    return str(uuid4().hex)


class Agent:

    # Constructor

    def __init__(self, coord, idd, colony_id, health=3, status=1, queen=False, scout=False):

        self.coord = coord
        # prospected
        self.prospected_coord = None
        self.target_coord = None
        self.id = idd
        self.colony_id = colony_id
        self.health = health
        self.status = status
        self.scout = scout
        self.queen = queen
        self.rank  = 1
        self.msg = ""
        self.res = None
        self._scan_reach = 3
        self._knowledge = None
        self.step =1
        self.found = False

        # important
        self.pheromone_id = ""

        # helper attributes
        self.prev_coord = None

        if self.scout:
            self._scan_reach = 2

    # move around
    def _move(self, coord: Coordinate):
        # print('called')
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
        elif x2 == x1 and y2 < y1:
            msg = "move up"
        elif x2 == x1 and y2 > y1:
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
            self.coord.move_up(self.step)

        elif msg == "move down":
            self.coord.move_down(self.step)

        elif msg == "move left":
            self.coord.move_left(self.step)

        elif msg == "move right":
            self.coord.move_right(self.step)

        elif msg == "move left up":
            self.coord.move_left_up(self.step, self.step)

        elif msg == "move right up":
            self.coord.move_right_up(self.step, self.step)

        elif msg == "move left down":
            self.coord.move_left_down(self.step, self.step)

        elif msg == "move right down":
            self.coord.move_right_down(self.step, self.step)

    # _prospective move
    def _prospective_move(self, coord: Coordinate):
        # print('called')
        msg = ""
        new = Coordinate(self.coord.x, self.coord.y)
        x1 = new.x
        y1 = new.y

        x2 = coord.x
        y2 = coord.y

        # creating command message
        if x2 > x1 and y2 > y1:
            new.move_right_up()
        elif x2 < x1 and y2 < y1:
            new.move_left_down()
        elif x2 == x1 and y2 < y1:
            new.move_up()
        elif x2 == x1 and y2 > y1:
            new.move_down()
        elif x2 < x1 and y2 > y1:
            new.move_left_up()
        elif x2 > x1 and y2 < y1:
            new.move_right_down()
        elif x2 > x1 and y2 == y1:
            new.move_right()
        else:
            new.move_left()

        # commands
        if msg == "move up":
            self.coord.move_up(self.step)

        elif msg == "move down":
            self.coord.move_down(self.step)

        elif msg == "move left":
            self.coord.move_left(self.step)

        elif msg == "move right":
            self.coord.move_right(self.step)

        elif msg == "move left up":
            self.coord.move_left_up(self.step, self.step)

        elif msg == "move right up":
            self.coord.move_right_up(self.step, self.step)

        elif msg == "move left down":
            self.coord.move_left_down(self.step, self.step)

        elif msg == "move right down":
            self.coord.move_right_down(self.step, self.step)

        return new

    # scan around environment
    def _scan(self, colonies, resources, grid = list[list[str]]):

        x = self.coord.x
        y = self.coord.y
        coords = []
        msgs = []


        range_i = (self._scan_reach * 2) + 1
        range_j = (self._scan_reach * 2) + 1
        neg = -self._scan_reach

        for i in range(range_i):
            for j in range(range_j):
                if self.coord.x == neg + j + x  and self.coord.y == neg + i + y:
                    continue
                try:
                    data = grid[neg + i + y][neg + j + x]
                    msgs.append(data)
                    coords.append(Coordinate(neg + j + x, neg + i + y ))
                except IndexError as e:
                    continue
        self._knowledge = None

        self._knowledge = Knowledge(msgs, self.msg, colonies, resources, coords)

    # attack other agents
    def _attack(self):
        return

    # leave pheromone trial
    def _leave_pheromone(self):
        return

    # acquire  resources
    def _acquire_resources(self, resource, resources):
        # print('ac called')
        if self.status == 1:
            if type(resource) is Tree:
                if abs(resource.coord.x - self.coord.x) > 1 or abs(resource.coord.y - self.coord.y) > 1:
                    return
                self.res = Leaf(self.coord, self.rank * 4, self.rank, id=get_id())  # portion is rank *4 while
                # size is the same as # rank, this is because ant can easily carry 4 portions of food
                resource.leaf_count -= self.rank
                if resource.leaf_count <= 0:
                    resources.remove(resource)
            elif type(resource) is Leaf:

                self.res = resource
                resources.pop(Helpers.find_resource_ind(resources, resource.id))
            else:
                log = "nothing"
                return
            self.status = 2

            self.pheromone_id = ""

        return

    # This will be the agent's decision based on the agent knowledge
    def perform_turn(self, colonies, resources, grid=list[list[str]]):
        # universal bit
        self._scan(colonies, resources, grid)  # assign knowledge
        current = Coordinate(self.coord.x, self.coord.y)
        # data management
        ants = []
        res = []
        pheromone = []
        empty = []
        pid = ""
        know_data = self._knowledge.knowledge_data
        for data in know_data:
            # print(data)
            if (data['colony_id'] == self.colony_id) and (data['pheromone_id'] != "") and (data['ant'] is None) and (data['res'] is None):
                # print('called inside')
                if self.pheromone_id == "":
                    # print('called no pher add')
                    pheromone.append(data)

                else:
                    # print('called yes pher add')
                    if self.pheromone_id == data['pheromone_id']:
                        # print('called appended')
                        pheromone.append(data)


            if data['ant'] is not None:
                ants.append(data)

            if data['res'] is not None:
                res.append(data)

            if data['res'] is None and data['pheromone_id'] == "" and data['ant'] is None:
                empty.append(data)

        if self.status == 1:


            # attack decision
            # acquire decision
            should_acquire = None
            try:
                should_acquire = res[0]
            except IndexError as e:
                should_acquire = None

            if should_acquire is not None:
                try:
                    self._acquire_resources(should_acquire['res'], resources)
                except Exception as e:
                    ppe = ('Error' + str(e))


            # move decision
            if  self.pheromone_id != "":
                # max_phe_index = 0
                # max_dis = -1
                # index = 0
                # for phe in pheromone:
                #
                #     dis = Helpers.euclidian(phe['coordinate'], Helpers.find_colony(colonies, self.colony_id).coord)
                #     if dis > max_dis:
                #         max_dis = dis
                #         max_phe_index = index
                #     index += 1
                # print(max_phe_index)
                # should_move_coord = pheromone[max_phe_index]['coordinate']
                should_move_coord = None
                if len(pheromone) > 1:
                    # This is because there will be only two possible pheromone on a trail with scan
                    count = 0
                    for phe in pheromone:
                        if self.prev_coord.x == (phe['coordinate']).x and self.prev_coord.y == (phe['coordinate']).y:
                            # print(str(self.prev_coord.x) + " "+ str(self.prev_coord.y))
                            pheromone.pop(count)
                        count += 1
                try:
                    should_move_coord = pheromone[0]['coordinate']
                except:
                    print('not moving')
                    return

                try:
                    self.target_coord = should_move_coord

                    # get prospective move
                    prop = self._prospective_move(should_move_coord)


                    if self.status == 1:
                        for colony in colonies:
                            for ant in colony.ants:
                                if prop.x == ant.coord.x and prop.y == ant.coord.y:
                                    # print('not moving')
                                    return

                    self._move(should_move_coord)  # move it!  move it!
                    self.prev_coord = current
                except Exception as e:
                    printx = ("self.id " + self.id + " " + self.colony_id + " x: " + str(self.coord.x) + " y: " + str(self.coord.y)+ " Pher_id " +self.pheromone_id
                          + " "
                          )
            else:
                # have no pheromone id yet.
                if self.status == 1:
                    length = len(pheromone)
                    if length == 0:
                        return

                    if length > 1:
                        randex = random.randrange(0, length)
                    else:
                        randex = 0

                    try:


                        should_move_coord = pheromone[randex]['coordinate']
                        self.target_coord = should_move_coord

                        # get prospective move
                        prop = self._prospective_move(should_move_coord)


                        if self.status == 1:
                            for colony in colonies:
                                for ant in colony.ants:
                                    if prop.x == ant.coord.x and prop.y == ant.coord.y:
                                        # print('not moving')
                                        return

                        self._move(should_move_coord)  # move it!  move it!
                        self.prev_coord = current
                        self.pheromone_id = pheromone[randex]['pheromone_id']

                        # print('sucess')

                    except Exception as e:
                        p = "not moving"


        else:
            #  self.msg = "go home" @deprecated system

            x1 = self.coord.x
            y1 = self.coord.y

            colony = Helpers.find_colony(colonies, self.colony_id)
            x2 = colony.coord.x
            y2 = colony.coord.y

            # move decision
            min_home_index = 0
            min_dis = 1000000
            index = 0
            # print(len(empty))
            for emp in empty:

                dis = Helpers.euclidian(emp['coordinate'], Helpers.find_colony(colonies, self.colony_id).coord)
                if dis < min_dis:
                    min_dis = dis
                    min_home_index = index
                index += 1

            try:
                should_move_coord = empty[min_home_index]['coordinate']
                prop = self._prospective_move(should_move_coord)
                if self.status == 2:
                    for col in colonies:
                        for ant in colony.ants:
                            if should_move_coord.x == ant.coord.x and should_move_coord.y == ant.coord.y:
                                # print('not moving')
                                if not (should_move_coord.x == colony.coord.x and should_move_coord.y == colony.coord.y):
                                    return
                    self._move(should_move_coord)  # move it!  move it!

                    if self.coord.x == colony.coord.x and self.coord.y == colony.coord.y:
                        colony.res_portion += self.res.portions
                        self.res = None
                        self.status = 1
                        self.pheromone_id = ""
                        self._scan_reach = 1
                        self.prev_coord = None

            except IndexError as e:
                # print("not moving")
                ms = 9

    # assign resource
    @staticmethod
    def _assign_closet_resource(coord, resources):
        min_res = None
        min_value = 100000
        for res in resources:
            dis = Helpers.euclidian(coord, res.coord)
            if dis < min_value:
                min_value = dis
                min_res = res

        return min_res


    # perform for scout
    def scout_perform(self, colonies, resources, grid):
        self._scan(colonies, resources, grid)
        know_data = self._knowledge.knowledge_data
        current = Coordinate(self.coord.x, self.coord.y)
        empty = []

        for data in know_data:
            if data['pheromone_id'] == "" and (data['ant'] is None) and (data['res'] is None) and (data['colony_id'] == ""):
                empty.append(data)

        # If 1st turn/ leaving nest
        if self.status == 1:
            if self.start:
                randex = 0
                if len(empty) > 0:
                    randex = random.randrange(0, len(empty))

                try:
                    should_move_coord = empty[randex]['coordinate']
                    prop = self._prospective_move(should_move_coord)

                    for res in resources:
                        if prop.x == res.coord.x and prop.y == res.coord.y:
                            return

                        self.target_coord = Agent._assign_closet_resource(prop, resources)
                        self._move(should_move_coord)  # move
                        self.prev_coord = current
                        self.start = False

                except:
                    return

            # if not 1st turn/ leaving nest
            else:
                # move decision
                min_home_index = 0
                min_dis = 1000000
                index = 0
                # print(len(empty))
                for emp in empty:

                    dis = Helpers.euclidian(emp['coordinate'], self.target_coord)
                    if dis < min_dis:
                        min_dis = dis
                        min_home_index = index
                    index += 1

                try:
                    should_move_coord = empty[min_home_index]['coordinate']
                    prop = self._prospective_move(should_move_coord)
                    if self.status == 1:
                        for col in colonies:
                            for ant in colony.ants:
                                if should_move_coord.x == ant.coord.x and should_move_coord.y == ant.coord.y:
                                    # print('not moving')
                                    if not (should_move_coord.x == colony.coord.x and should_move_coord.y == colony.coord.y):
                                        return
                        self._move(should_move_coord)  # move it!  move it!
                        if self.coord.x ==  self.target_coord.x and self.coord.y == self.target_coord.y:

                            self.res = None
                            self.status = 2
                            self._scan_reach = 1
                            self.prev_coord = None
                            self.found = True

                except IndexError as e:
                    ms = 9
        else:
            # status 2

            return



