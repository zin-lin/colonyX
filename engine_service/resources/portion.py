# Author : Zin Lin Htun
# leaf class
from engine_service.resources.resource import Resource


class Portion(Resource):

    # Constructor
    def __init__(self, coord, portions, size, **kwargs):
        super().__init__(portions, size, coord, kwargs['id'])
