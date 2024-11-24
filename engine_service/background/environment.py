# Author : Zin Lin Htun
# Environment class


class Environment:
    grid = []

    # Constructor
    def __init__(self, size_x=20, size_y=20):
        # add 0s to every grid point
        for i in range(size_y):
            self.grid.append([])
            for j in range(size_x):
                self.grid[i].append(",,,")
