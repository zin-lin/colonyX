class BulletAnt:
    health = 2
    status = 1
    name = ''
    rank = 1
    age = 1
    queen = False

    def __init__(self, name='JB', health=2, status=1, queen=False):
        self.name = name
        self.health = health
        self.status = status
        self.queen = queen

    def move(self):
        return

    def scan(self):
        return

    def attack(self):
        return

    def leave_pheromone(self):
        return
