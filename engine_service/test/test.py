import time

from engine_service.agents.bulant import BulletAnt
from engine_service.agents.lcant import LeafCutterAnt
from engine_service.agents.redant import RedAnt
from engine_service.background.coordinate import Coordinate
from engine_service.background.environment import *


# add ant: minim
def add_minim_or_forager(colony, number=1, code="LC"):
    for i in range(number):
        if code == "LC":
            colony.ants.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(),
                                             colony.id, "Bob",
                                             ))


def add_scout(colony, number=1, code="LC"):
    for i in range(number):
        if code == "LC":
            colony.scouts.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y),Helpers.get_id(), colony.id,
                                               "Bob", 2, 1, False, True, ))


def add_minor(colony, number=1, code="LC"):
    if code == "LC":
        colony.ants.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(),
                                         colony.id, "Bob", 2, 1, False, False, "Minor"
                                         ))


# colonies
colonies = [
    Colony("LC1", "leaf-cutter-1", 16, [], Coordinate(6, 27)),
    Colony("LC2", "leaf-cutter-2", 16, [], Coordinate(16, 23)),
    Colony("LC3", "leaf-cutter-3", 16, [], Coordinate(22, 25)),
]

resources = [
    Tree(Helpers.get_id(), Coordinate(21, 18), ),
    Tree(Helpers.get_id(), Coordinate(11, 23), ),
]

lc1 = colonies[0]
lc2 = colonies[1]
lc3 = colonies[2]

# env
env = Environment(36, 36)
env.add_colonies(colonies)

for i in range(10):
    add_minim_or_forager(lc1)

for i in range(1):
    add_scout(lc1)
    add_scout(lc2)
    add_scout(lc3)

for i in range(5):
    add_minim_or_forager(lc2)

for i in range(5):
    add_minim_or_forager(lc3)



# Uncomment this to test print grid
# Helpers.print_grid(env.grid)


# Uncomment this to test visualisation
env.manage_state(colonies, resources)
Helpers.visualize_grid(env.grid)

import asyncio


async def process_ant(ant, cls, ress, envv):
    """Process an individual ant."""
    if not ant.scout:
        if ant.cat == "Minim":
            ant.perform_turn(cls, ress, envv.grid)
    else:
        ant.scout_perform(cls, ress, envv.grid)
        print(ant.status)
    envv.manage_state(colonies, resources)
    Helpers.visualize_grid(env.grid)


async def process_colony(colony, cls, ress, envv):
    """Process all ants in a colony."""
    tasks = [
        *[process_ant(scout, cls, ress, envv) for scout in colony.scouts],
        *[process_ant(ant, cls, ress, envv) for ant in colony.ants]
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
            print(f"{col.name} {col.res_portion} {len(col.ants)} ants")

        await asyncio.sleep(0.2)  # Non-blocking delay
        # Helpers.print_grid(envv.grid)

asyncio.run(main_loop(colonies, resources, env))
