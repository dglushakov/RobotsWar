class Robot:
    color = None
    body = None
    weapon = None
    corX = None
    corY = None

    def __init__(self, color='gray', body=0, weapon=0, robot_id=0):
        self.id = robot_id
        self.color = color
        self.body = body
        self.weapon = Weapon.Basic
        self.health_points = 1
        self.movement_speed = 1

    def move_to(self, x, y):
        self.corX = x
        self.corY = y

    def __str__(self):
        return str(self.color) + ' x: ' + str(self.corX) + ' y: ' + str(self.corY)


class Body:
    Simple = 1
    Hard = 2
    Light = 3
    Battle = 4


class Weapon:
    names = ['Basic', 'Laser', 'Sword', 'Explosion', 'Dual Laser']

    Basic = 0
    Laser = 1
    Sword = 2
    Explosion = 3
    Dual_Laser = 4

    def __str__(self):
        return self