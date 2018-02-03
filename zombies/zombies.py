import math


class Entity(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.last_x = x
        self.last_y = y

    def move_to(self, t_x, t_y):
        x_diff = t_x - self.x
        y_diff = t_y - self.y
        if math.fabs(x_diff) > math.fabs(y_diff):
            self.x += int(x_diff > 0)
        else:
            self.y += int(y_diff > 0)

    def move_away(self, t_x, t_y):
        x_diff = t_x - self.x
        y_diff = t_y - self.y
        if math.fabs(x_diff) > math.fabs(y_diff):
            self.x -= int(x_diff > 0)
        else:
            self.y -= int(y_diff > 0)

    def quadrant_to(self, t_x, t_y):
        angle = math.degrees(math.atan2(t_y, t_x))
        return

    def distance_to(self, p_x, p_y):
        return math.sqrt((self.x - p_x) ** 2 + (self.y - p_y) ** 2)

    def relative_distances(self, E_list):
        return [self.distance_to(e.x, e.y) for e in E_list]

    def get_closest(self, E_list):
        closest_distance = None
        closest_E = None
        for E in E_list:
            if closest_distance is None or self.distance_to(E.x, E.y) < closest_distance:
                closest_distance = self.distance_to(E.x, E.y)
                closest_E = E
        return closest_E


zombie_num = int(input())
person = Entity(0, 0)
zombie_list = []
for n in range(zombie_num):
    coords = input()
    z_x = int(coords.split(' ')[0])
    z_y = int(coords.split(' ')[1])
    zombie_list.append(Entity(z_x, z_y))

moves = 0
dead = False
state_same = False
previous_distances = []
while not dead and not state_same:
    for z in zombie_list:
        if z.x == person.x and z.y == person.y:
            dead = True
            print ('Dead')
            break
    if not dead:
        for z in zombie_list:
            z.move_to(person.x, person.y)
        closest_z = person.get_closest(zombie_list)
        person.move_away(closest_z.x, closest_z.y)
        moves += 1
        if previous_distances == person.relative_distances(zombie_list):
            state_same = True
            break

if state_same:
    print('never')
else:
    print(moves)
