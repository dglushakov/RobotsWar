import random
from Robot import Robot, Weapon, Body


class Arena:
    ArenaWidth = 6
    ArenaHeight = 6

    RobotsEachTeam = 2

    def __init__(self):
        self.loot = []
        print('new arena created')

    def reset(self):
        self.Robots = []
        self.__generate_robots()

    def __generate_robots(self):
        next_id = 1
        for i in range(self.RobotsEachTeam):
            robot_red = Robot(color='red', robot_id=next_id)
            while True:
                x = random.randint(1, self.ArenaWidth)
                y = 6
                if not self.is_field_busy(x, y):
                    break
            robot_red.move_to(x, y)
            self.Robots.append(robot_red)
            next_id += 1

        for i in range(self.RobotsEachTeam):
            robot_blue = Robot(color='blue', robot_id=next_id)
            while True:
                x = random.randint(1, self.ArenaWidth)
                y = 1
                if not self.is_field_busy(x, y):
                    break
            robot_blue.move_to(x, y)
            self.Robots.append(robot_blue)
            next_id += 1

        for i in range(8):
            robot_gray = Robot(color='gray', robot_id=next_id)
            while True:
                x = random.randint(1, self.ArenaWidth)
                y = random.randint(2, self.ArenaHeight - 1)
                if not self.is_field_busy(x, y):
                    break
            robot_gray.move_to(x, y)
            self.Robots.append(robot_gray)
            next_id += 1

    def is_field_busy(self, x, y):
        if x <= 0 or x > self.ArenaWidth:
            return True
        if y <= 0 or y > self.ArenaHeight:
            return True
        for robot in self.Robots:
            if robot.corX == x and robot.corY == y:
                return True
        return False

    def get_robots(self):
        return self.Robots

    def make_turn(self):  # TODO "The first team to play is also random"
        for robot in self.Robots:
            if robot.color != 'gray':  # TODO "The interface should also give the possibility to decide the number of robots present on each side."
                for step in range(
                        robot.movement_speed):
                    direction = random.choice(['x', 'y'])
                    if direction == 'x':
                        side = random.choice([-1, 1])
                        if not self.is_field_busy(robot.corX + side, robot.corY):
                            robot.move_to(robot.corX + side, robot.corY)
                    if direction == 'y':
                        side = random.choice([-1, 1])
                        if not self.is_field_busy(robot.corX, robot.corY + side):
                            robot.move_to(robot.corX, robot.corY + side)
                    for item in self.loot:
                        if item['x'] == robot.corX and item['y'] == robot.corY:
                            if isinstance(item['loot'], Weapon):
                                robot.inventory_weapon.append(item['loot'])
                                self.loot.remove(item)
                            elif isinstance(item['loot'], Body):
                                robot.inventory_body.append(item['loot'])
                                self.loot.remove(item)
                            print('picked up ', *item)

                need_to_change_body = random.randint(0, 1)
                if need_to_change_body:
                    robot.change_body_randomly()
                need_to_change_weapons = random.randint(0, 1)
                if need_to_change_weapons:
                    robot.change_weapons_randomly()
                need_to_change_direction = random.randint(0, 1)
                if need_to_change_direction:
                    robot.change_direction_randomly()

                self.make_shot(robot)

    def make_shot(self, robot):
        affected_area = robot.get_shot_info()
        for cell in affected_area:
            for robot in self.Robots:
                if robot.corX == cell['x'] and robot.corY == cell['y']:
                    damage = cell['damage']
                    not_absorbed_damage = damage - robot.body.hit_points
                    robot.body.hit_points -= damage
                    if not_absorbed_damage > 0:
                        robot.health_points -= not_absorbed_damage
                    print(robot.id, ' damaged for ', cell['damage'])
                    if robot.health_points <= 0:
                        self.make_drop_from_destroyed_robot(robot)
                        self.Robots.remove(robot)
                        print('robot ', robot.id, ' destroyed')

    def make_drop_from_destroyed_robot(self, destroyed_robot):
        weapon_or_body = random.choice([0, 1])
        if weapon_or_body == 0:
            loot = Weapon(random.randint(0, 4))
        else:
            loot = Body(random.randint(0, 3))
        self.loot.append({'x': destroyed_robot.corX, 'y': destroyed_robot.corY, 'loot': loot})
        print('dropped ', *self.loot)


if __name__ == "__main__":
    arena = Arena()
    arena.reset()
    robots = arena.get_robots()
    print(*robots)
    arena.make_turn()
    arena.make_turn()
    arena.make_turn()
    arena.make_turn()
    arena.make_turn()
    arena.make_turn()
