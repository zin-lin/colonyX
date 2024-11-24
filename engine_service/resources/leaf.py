# Author : Zin Lin Htun
# leaf class
from resource import Resource


class Leaf(Resource):

    # Constructor
    def __init__(self, coord, portions, size, **kwargs):
        super().__init__(portions, size, coord, kwargs['id'])
