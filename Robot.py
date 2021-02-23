import random


class Robot:
    directions = ['up', 'right', 'down', 'left']

    def __init__(self, color='gray', body=0, weapon=3, robot_id=0):
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

    def move_to(self, x, y):
        self.corX = x
        self.corY = y

    def change_body_randomly(self):
        print(*self.inventory_body)
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
        for weapon in self.weapon_equipped:
            if weapon.type == 0:  # basic shoot
                if self.direction == 'up':
                    affected_area.append({'x': self.corX, 'y': self.corY + 1, 'damage': 1})
                    affected_area.append({'x': self.corX, 'y': self.corY + 2, 'damage': 1})
                if self.direction == 'right':
                    affected_area.append({'x': self.corX + 1, 'y': self.corY, 'damage': 1})
                    affected_area.append({'x': self.corX + 2, 'y': self.corY, 'damage': 1})
                if self.direction == 'down':
                    affected_area.append({'x': self.corX, 'y': self.corY - 1, 'damage': 1})
                    affected_area.append({'x': self.corX, 'y': self.corY - 2, 'damage': 1})
                if self.direction == 'left':
                    affected_area.append({'x': self.corX - 1, 'y': self.corY, 'damage': 1})
                    affected_area.append({'x': self.corX - 2, 'y': self.corY, 'damage': 1})
            elif weapon.type == 1:  # Laser
                if self.direction == 'up':
                    for y_addiction in range(1, 6 - self.corY):
                        affected_area.append({'x': self.corX, 'y': self.corY + y_addiction, 'damage': 1})
                if self.direction == 'right':
                    for x_addiction in range(1, 6 - self.corX):
                        affected_area.append({'x': self.corX + x_addiction, 'y': self.corY, 'damage': 1})
                if self.direction == 'down':
                    for y_addiction in range(1, self.corY):
                        affected_area.append({'x': self.corX, 'y': self.corY - y_addiction, 'damage': 1})
                if self.direction == 'left':
                    for x_addiction in range(1, self.corX):
                        affected_area.append({'x': self.corX - x_addiction, 'y': self.corY, 'damage': 1})
            elif weapon.type == 2:  # Sword
                if self.direction == 'up':
                    affected_area.append({'x': self.corX - 1, 'y': self.corY + 1, 'damage': 2})
                    affected_area.append({'x': self.corX, 'y': self.corY + 1, 'damage': 2})
                    affected_area.append({'x': self.corX + 1, 'y': self.corY + 1, 'damage': 2})
                if self.direction == 'right':
                    affected_area.append({'x': self.corX + 1, 'y': self.corY + 1, 'damage': 2})
                    affected_area.append({'x': self.corX + 1, 'y': self.corY, 'damage': 2})
                    affected_area.append({'x': self.corX + 1, 'y': self.corY - 1, 'damage': 2})
                if self.direction == 'down':
                    affected_area.append({'x': self.corX - 1, 'y': self.corY - 1, 'damage': 2})
                    affected_area.append({'x': self.corX, 'y': self.corY - 1, 'damage': 2})
                    affected_area.append({'x': self.corX + 1, 'y': self.corY - 1, 'damage': 2})
                if self.direction == 'left':
                    affected_area.append({'x': self.corX - 1, 'y': self.corY + 1, 'damage': 2})
                    affected_area.append({'x': self.corX - 1, 'y': self.corY, 'damage': 2})
                    affected_area.append({'x': self.corX - 1, 'y': self.corY - 1, 'damage': 2})
            elif weapon.type == 3:  # Explosion
                affected_area.append({'x': self.corX - 1, 'y': self.corY + 1, 'damage': 1})
                affected_area.append({'x': self.corX, 'y': self.corY + 1, 'damage': 1})
                affected_area.append({'x': self.corX + 1, 'y': self.corY + 1, 'damage': 1})
                affected_area.append({'x': self.corX + 1, 'y': self.corY, 'damage': 1})
                affected_area.append({'x': self.corX + 1, 'y': self.corY - 1, 'damage': 1})
                affected_area.append({'x': self.corX - 1, 'y': self.corY - 1, 'damage': 1})
                affected_area.append({'x': self.corX, 'y': self.corY - 1, 'damage': 1})
                affected_area.append({'x': self.corX - 1, 'y': self.corY, 'damage': 1})
                affected_area.append({'x': self.corX - 1, 'y': self.corY - 1, 'damage': 1})
            elif weapon.type == 4:  # Dual Laser
                if self.direction == 'up' or self.direction == 'down':
                    for y in range(1, 6):
                        if self.corY != y:
                            affected_area.append({'x': self.corX, 'y': y, 'damage': 1})
                if self.direction == 'left' or self.direction == 'right':
                    for x in range(1, 6):
                        if self.corX != x:
                            affected_area.append({'x': x, 'y': self.corY, 'damage': 1})

        return affected_area

    def __str__(self):
        return str(self.color) + ' x: ' + str(self.corX) + ' y: ' + str(self.corY)


class Body:
    types = ['Simple', 'Hard', 'Light', 'Battle']

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
    Robot_red = Robot(color='red', robot_id=1, weapon=3)
    Robot_red.inventory_body.append(Body())
    Robot_red.inventory_body.append(Body(body_type=1))
    Robot_red.inventory_body.append(Body(body_type=2))
    Robot_red.change_body_randomly()
    Robot_red.change_body_randomly()
    Robot_red.change_body_randomly()
    Robot_red.move_to(3, 3)
    affected_area = Robot_red.get_shot_info()
    pass
