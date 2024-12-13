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
        self.knowledge_data = []

        # assign data
        for data in self.scan_data:

            data_object = Helpers.process_data(data, colonies, resources, coords[_count])

            self.knowledge_data.append(data_object)
            _count += 1

