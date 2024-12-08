import time
from engine_service.agents.lcant import LeafCutterAnt
from engine_service.background.coordinate import Coordinate
from engine_service.background.environment import *


# add ant, of different type; type == 1: minim, type == 2: queen, type === 3: scout, default: minim
def add_ant(colony, number=1, type=1):
    for i in range(number):
        if type == 1:
            colony.ants.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(),
                                             colony.id, "Bob",
                                             ))

        elif type == 2:
            colony.queen.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(),
                                              colony.id, "Sarah", 4, 1, True, True,
                                              ))

        elif type == 3:
            colony.scouts.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(), colony.id,
                                               "Bob", 2, 1, False, True,
                                               ))
        elif type == 4:
            colony.soldiers.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(), colony.id,
                                               "Bob", 2, 1, False, False, True
                                               ))
        else:
            print('wrong type')


# colonies
colonies = [
    Colony("LC1", "leaf-cutter-1", 16, [], Coordinate(6, 27)),
    Colony("LC2", "leaf-cutter-2", 16, [], Coordinate(16, 23)),
    Colony("LC3", "leaf-cutter-3", 16, [], Coordinate(22, 25)),
]

resources = [
    Tree(Helpers.get_id(), Coordinate(21, 18), 23 ),
    Tree(Helpers.get_id(), Coordinate(11, 23), 23),
]

lc1 = colonies[0]
lc2 = colonies[1]
lc3 = colonies[2]

# env
env = Environment(30, 30)
env.add_colonies(colonies)

# add ant
add_ant(lc1, 10, )
add_ant(lc2, 5, )
add_ant(lc3, 5, )

# add queens
add_ant(lc1, 1, 2)
add_ant(lc2, 1, 2)
add_ant(lc3, 1, 2)

# add scouts
add_ant(lc1, 1, 3)
add_ant(lc2, 1, 3)
add_ant(lc3, 1, 3)

# Uncomment this to test print grid
# Helpers.print_grid(env.grid)


# Uncomment this to test visualisation
env.manage_state(colonies, resources)
Helpers.visualize_grid(env.grid)

import asyncio


async def process_ant(ant, cls, ress, envv):
    """Process an individual ant."""
    if not ant.scout:
        if ant.soldier:
            ant.soldier_perform(cls, ress, envv.grid)
        else:
            ant.perform_turn(cls, ress, envv.grid)

    else:
        if not ant.queen:
            ant.scout_perform(cls, ress, envv.grid)
            print(ant.status)
        else:
            ant.queen_perform(cls, ress, envv.grid)
    envv.manage_state(colonies, resources)


async def process_colony(colony, cls, ress, envv):
    """Process all ants in a colony."""
    tasks = [
        *[process_ant(scout, cls, ress, envv) for scout in colony.scouts],
        *[process_ant(ant, cls, ress, envv) for ant in colony.ants],
        *[process_ant(ant, cls, ress, envv) for ant in colony.soldiers],
        *[process_ant(ant, cls, ress, envv) for ant in colony.queen]
    ]
    await asyncio.gather(*tasks)


async def main_loop(cls, ress, envv):
    """Main loop to process colonies and visualize."""
    while True:
        # Create tasks for all colonies
        # input()
        tasks = [process_colony(col, cls, ress, envv) for col in cls]
        await asyncio.gather(*tasks)

        # Print colony summaries
        for col in cls:
            print(f"{col.name} {int(col.res_portion)} {len(col.ants)} ants")

        # deal with Queen's request
        for col in cls:

            queen = col.queen[0]
            if queen.health <=0:
                cls.remove(col)
                continue

            for i in range(queen.mate):
                add_ant(col, 1)
            for i in range(queen.mate_soldier):
                add_ant(col, 1, 4)


            queen.mate = 0
            queen.mate_soldier = 0

        Helpers.visualize_grid(env.grid)

        await asyncio.sleep(0.2)  # Non-blocking delay
        # Helpers.print_grid(envv.grid)


asyncio.run(main_loop(colonies, resources, env))
