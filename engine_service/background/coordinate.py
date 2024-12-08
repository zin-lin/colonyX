# Author : Zin Lin Htun
# Coordinate class


class Coordinate:
    x = 0
    y = 0

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # operator overloads equals
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # not equal
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    # move left
    def move_left(self, x=1):
        self.x -= x

    # move right
    def move_right(self, x=1):
        self.x += x

    # move up
    def move_up(self, y=1):
        self.y -= y

    # move down
    def move_down(self, y=1):
        self.y += y

    # move left and up
    def move_left_up(self, x=1, y=1):
        self.x -= x
        self.y += y

    # move right and up
    def move_right_up(self, x=1, y=1):
        self.x += x
        self.y += y

    # move left and down
    def move_left_down(self, x=1, y=1):
        self.x -= x
        self.y -= y

    # move right and down
    def move_right_down(self, x=1, y=1):
        self.x += x
        self.y -= y
