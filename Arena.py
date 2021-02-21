import random
from Robot import Robot

aim_directions = ['up', 'right', 'down', 'left']


class Arena:
    ArenaWidth = 6
    ArenaHeight = 6

    RobotsEachTeam = 2
    Robots = []

    def __init__(self):
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

    def make_turn(self):
        for robot in self.Robots:
            if robot.color != 'gray':
                for step in range(robot.movement_speed):
                    direction = random.choice(['x', 'y'])
                    print('try to change ', direction)
                    if direction == 'x':
                        side = random.choice([-1, 1])
                        if not self.is_field_busy(robot.corX + side, robot.corY):
                            robot.move_to(robot.corX + side, robot.corY)
                        else:
                            print('cant go to ', robot.corX + side, robot.corY, ' from ', robot.corX, robot.corY)

                    if direction == 'y':
                        side = random.choice([-1, 1])
                        if not self.is_field_busy(robot.corX, robot.corY + side):
                            robot.move_to(robot.corX, robot.corY + side)
                        else:
                            print('cant go to ', robot.corX, robot.corY + side, ' from ', robot.corX, robot.corY)

                    robot.aim_direction = random.choice(aim_directions)
                    print('robot ', robot.id, ' is eqipped with ', robot.weapon, ' and looks ', robot.aim_direction)

if __name__ == "__main__":
    arena = Arena()
    arena.reset()
    robots = arena.get_robots()
    print(*robots)
    arena.make_turn()
