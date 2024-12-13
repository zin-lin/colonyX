# Author : Zin Lin Htun
# tree class offering leaves
from engine_service.resources.resource import *


class Meat(Resource):
    gram = 0

    # Constructor, parameter: count
    def __init__(self, idd, coord, count=10000):
        super().__init__(0, 0, coord, idd)
        self.gram = count

