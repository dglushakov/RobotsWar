import random


class Robot:
    # id = None
    # color = None
    # body = None
    # weapon_equipped = []
    # corX = None
    # corY = None
    # inventory_body = []
    # inventory_weapon = []
    # weapon_slots = None
    # direction = None
    directions = ['up', 'right', 'down', 'left']

    def __init__(self, color='gray', body=0, weapon=0, robot_id=0):
        self.id = robot_id
        self.color = color
        self.body = Body(body)
        self.weapon_slots = 1
        self.weapon_equipped = []
        self.weapon_equipped.append(Weapon(weapon))
        self.health_points = 1
        self.movement_speed = 1
        self.direction = self.directions[2]

        self.inventory_body = []
        self.inventory_weapon = []
        #
        # rand_body = random.randint(0, 3)
        # test_body = Body(rand_body)
        # self.inventory_body.append(test_body)
        #
        # rand_weapon = random.randint(0, 4)
        # test_weapon = Weapon(rand_weapon)
        # self.inventory_weapon.append(test_weapon)

    def move_to(self, x, y):
        self.corX = x
        self.corY = y

    def change_body_randomly(self):
        if len(self.inventory_body) > 0:
            self.health_points = 1
            self.movement_speed = 1
            self.weapon_slots = 1
            self.body = random.choice(self.inventory_body)
            self.health_points += self.body.hit_points
            self.movement_speed += self.body.movement_speed
            self.weapon_slots += self.body.weapon_slots
            print('body equipped', self.body)

    def change_weapons_randomly(self):
        if len(self.inventory_weapon) > 0:
            self.weapon_equipped = []
            for weapon_slot in range(self.weapon_slots):
                self.weapon_equipped.append(random.choice(self.inventory_weapon))
            print('robot ', self.id, ' has ', self.weapon_slots)
            print('weapon equipped ', *self.weapon_equipped)

    def change_direction_randomly(self):
        self.direction = random.choice(self.directions)

    def get_shot_info(self):  # return x,y,damage
        affected_area = []
        for weapon in self.weapon_equipped:  # TODO add another weapon types
            if weapon.type == 0:  # basic shoot
                if self.direction == 'up':
                    affected_area.append({'x': self.corX, 'y': self.corY - 1, 'damage': 1})
                    affected_area.append({'x': self.corX, 'y': self.corY - 2, 'damage': 1})
                if self.direction == 'right':
                    affected_area.append({'x': self.corX + 1, 'y': self.corY, 'damage': 1})
                    affected_area.append({'x': self.corX + 2, 'y': self.corY, 'damage': 1})
                if self.direction == 'down':
                    affected_area.append({'x': self.corX, 'y': self.corY + 1, 'damage': 1})
                    affected_area.append({'x': self.corX, 'y': self.corY + 2, 'damage': 1})
                if self.direction == 'left':
                    affected_area.append({'x': self.corX - 1, 'y': self.corY, 'damage': 1})
                    affected_area.append({'x': self.corX - 2, 'y': self.corY, 'damage': 1})
        return affected_area

    def __str__(self):
        return str(self.color) + ' x: ' + str(self.corX) + ' y: ' + str(self.corY)


class Body:
    types = ['Simple', 'Hard', 'Light', 'Battle']
    hit_points = None
    movement_speed = None
    weapon_slots = None

    def __init__(self, body_type=0):
        self.type = body_type
        self.weapon_slots = 0
        self.movement_speed = 0
        if body_type == 0:
            self.hit_points = 2
        elif body_type == 1:
            self.hit_points = 5
        elif body_type == 2:
            self.hit_points = 3
            self.movement_speed = 1
        elif body_type == 3:
            self.hit_points = 2
            self.weapon_slots = 1

    def __str__(self):
        return self.types[self.type]


class Weapon:
    types = ['Basic', 'Laser', 'Sword', 'Explosion', 'Dual Laser']
    damage = None

    def __init__(self, weapon_type=0):
        self.type = weapon_type
        if weapon_type == 0:
            self.damage = 1
        elif weapon_type == 1:
            self.damage = 1
        elif weapon_type == 2:
            self.damage = 2
        elif weapon_type == 3:
            self.damage = 1
        elif weapon_type == 4:
            self.damage = 1

    def __str__(self):
        return self.types[self.type]


if __name__ == '__main__':
    Robot_red = Robot(color='red', robot_id=1, weapon=1)
    Robot_red1 = Robot(color='red', robot_id=2)
    pass
