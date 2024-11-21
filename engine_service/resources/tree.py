# Author : Zin Lin Htun
# tree class offering leaves
from leaf import *


class Tree:
    leave_count = 0

    # Constructor, parameter: count
    def __init__(self, count=10000):
        self.leave_count = count
