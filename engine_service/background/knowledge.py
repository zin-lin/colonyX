# Author : Zin Lin Htun
# class Knowledge-base
from engine_service.background.helpers import Helpers


class Knowledge:
    scan_data = []
    msg = ""
    knowledge_data = []

    def __init__(self, scan_data, msg, colonies=None, resources=None,  coords=None):
        self.scan_data = scan_data
        self.msg = msg
        _count = 0

        # assign data
        for data in self.scan_data:

            data_object = Helpers.process_data(self.scan_data, colonies, resources, coords[_count])
            if not (data_object['pheromone_id'] is None and data_object['colony_id'] is None and data_object['ant']
                    is None and data_object['resource'] is None):
                self.knowledge_data.append(data_object)
            _count += 1

