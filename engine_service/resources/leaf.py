# Author : Zin Lin Htun
# leaf class
from resource import Resource


class Leaf(Resource):

    # Constructor
    def __init__(self, portions, size, **kwargs):
        super().__init__(portions, size)
