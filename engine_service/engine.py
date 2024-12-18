# Main ENTRYPOINT
# Class flask app
# Author: Zin Lin Htun


import asyncio
from flask import *
from flask_cors import *
from engine_service.agents.lcant import LeafCutterAnt
from engine_service.background.environment import *


# add ant, of different type; type == 1: minim, type == 2: queen, type === 3: scout, default: minim
def add_ant(colony, number=1, ant_type=1):
    for i in range(number):
        if ant_type == 1:
            colony.ants.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(),
                                             colony.id, "Bob",
                                             ))

        elif ant_type == 2:
            colony.queen.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(),
                                              colony.id, "Sarah", 4, 1, True, True,
                                              ))

        elif ant_type == 3:
            colony.scouts.append(LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(), colony.id,
                                               "Bob", 2, 1, False, True,
                                               ))
        elif ant_type == 4:
            colony.soldiers.append(
                LeafCutterAnt(Coordinate(colony.coord.x, colony.coord.y), Helpers.get_id(), colony.id,
                              "Bob", 2, 1, False, False, True
                              ))
        else:
            print('wrong type')


# process ant
async def process_ant(ant, cls, ress, envv):
    # Process an individual ant agent.
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


# process colony
async def process_colony(colony, cls, ress, envv):
    # Process all ants in a colony.
    tasks = [
        *[process_ant(scout, cls, ress, envv) for scout in colony.scouts],
        *[process_ant(ant, cls, ress, envv) for ant in colony.ants],
        *[process_ant(ant, cls, ress, envv) for ant in colony.soldiers],
        *[process_ant(ant, cls, ress, envv) for ant in colony.queen]
    ]
    await asyncio.gather(*tasks)


# globals
colonies = []
resources = []
environment = None


# defaults
def create_app_def():
    global environment, colonies, resources

    environment = Environment(25, 25, 3)
    # colonies

    colonies.append(Colony(Helpers.get_id(), 'LC' + str(1), 10, [], Coordinate(1, 1)))
    colonies.append(Colony(Helpers.get_id(), 'LC' + str(2), 10, [], Coordinate(23, 23)))
    colonies.append(Colony(Helpers.get_id(), 'LC' + str(3), 10, [], Coordinate(23, 1)))
    colonies.append(Colony(Helpers.get_id(), 'LC' + str(4), 10, [], Coordinate(1, 23)))

    for col in colonies:
        # add queen
        add_ant(col, 1, 2)

        # add scout
        add_ant(col, 1, 3)

        # add ants
        add_ant(col, 4)

    environment.manage_state(colonies, resources)
    for col in colonies:
        print(col.name + ", " + str(col.coord.x) + ", " + str(col.coord.y))


def create_app_def_1():
    global environment, colonies, resources

    environment = Environment(30, 30, 2)
    # colonies

    # colonies
    colonies = [
        Colony("LC1", "leaf-cutter-1", 16, [], Coordinate(6, 27)),
        Colony("LC2", "leaf-cutter-2", 16, [], Coordinate(16, 23)),
        Colony("LC3", "leaf-cutter-3", 16, [], Coordinate(22, 25)),
    ]

    resources = [
        Tree(Helpers.get_id(), Coordinate(21, 18), 23),
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


# turn
async def turn():
    global environment, colonies, resources

    if environment is None:
        environment = Environment(25, 25, 2)

    tasks = [process_colony(col, colonies, resources, environment) for col in colonies]
    await asyncio.gather(*tasks)

    # deal with Queen's request
    for col in colonies:

        queen = col.queen[0]
        if queen.health <= 0:
            colonies.remove(col)
            continue

        for i in range(queen.mate):
            add_ant(col, 1)
        for i in range(queen.mate_soldier):
            add_ant(col, 1, 4)

        queen.mate = 0
        queen.mate_soldier = 0

    Helpers.visualize_grid(environment.grid)
    await asyncio.sleep(0.5)  # Non-blocking delay


# Flask
app = Flask(__name__, static_folder='./engine_fe/build', static_url_path='/')
CORS(app, origins='*', supports_credentials=True)


# Check method route

@app.route('/check', methods=['GET', 'POST'])
@cross_origin()
def check():
    return jsonify({'msg': 'ping'})


# home route
@app.route('/', methods=['GET', 'POST'])
def home():
    global environment, colonies, resources
    environment = None
    colonies = []
    resources = []

    return app.send_static_file('index.html')


# clear API
@app.route('/clear', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def clear():
    global environment, colonies, resources

    environment = None
    colonies = []
    resources = []


# create game API
@app.route('/api/create_game', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def create_game():
    global environment, colonies, resources

    environment = None
    colonies = []
    resources = []

    size = int(eval(request.form.get('size')))
    col_len = int(eval(request.form.get('col_len')))
    res_num = col_len - 1 if col_len > 1 else 1
    environment = Environment(size, size, res_num, True)

    # colonies

    for i in range(col_len):
        ran_x = randrange(1, size-1)
        ran_y = randrange(1, size-1)
        for col in colonies:
            if col.coord == Coordinate(ran_x, ran_y):
                ran_x = randrange(1, size-1)
                ran_y = randrange(1, size-1)
        # add colonies
        colonies.append(Colony('LC' + str(i + 1), 'LC' + str(i + 1), 30, [], Coordinate(ran_x, ran_y)))

    for col in colonies:
        # add queen
        add_ant(col, 1, 2)

        # add scout
        add_ant(col, 1, 3)

        # add ants
        add_ant(col, 4, 1)

    environment.manage_state(colonies, resources)
    for col in colonies:
        print(col.name + ", " + str(col.coord.x) + ", " + str(col.coord.y))

    return 'OK'


# game API
@app.route('/api/game/', methods=['GET', 'POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def game():
    global environment, colonies

    if environment is None:
        environment = Environment(25, 25, 2, True)

    asyncio.run(turn())

    if len(colonies) == 0:
        return jsonify({'env': [], 'meta': []})

    print(len(environment.grid))

    # meta array
    meta = []
    for col in colonies:
        meta.append([col.id, len(col.queen), len(col.scouts), len(col.ants), len(col.soldiers), col.res_portion])

    return jsonify({'env': environment.grid, 'meta': meta})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=15000)
