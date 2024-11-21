# Author : Zin Lin Htun
# resource base class


class Resource:
    portions = 0
    size = 0

    # Constructor
    def __init__(self, portions, size):
        self.portions = portions
        self.size = size
