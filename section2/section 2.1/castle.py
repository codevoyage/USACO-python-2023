"""
ID: shikha11
LANG: PYTHON3
TASK: castle
"""
import copy

fin = open('castle.in', 'r')
fout = open('castle.out', 'w')

M, N = map(int, fin.readline().split())
total_units = M * N


def get_neighbour_unit_number(unit_number, direction):
    neighbour_unit = -1
    if direction == 'N':
        neighbour_unit = unit_number - M
        if neighbour_unit < 0:
            neighbour_unit = -1
    elif direction == 'S':
        neighbour_unit = unit_number + M
        if neighbour_unit >= total_units:
            neighbour_unit = -1
    elif direction == 'E':
        neighbour_unit = unit_number + 1
        if neighbour_unit % M == 0:
            neighbour_unit = -1
    elif direction == 'W':
        neighbour_unit = -1 if unit_number % M == 0 else unit_number - 1

    return neighbour_unit


def assign_neighbours(unit_neighbours):
    # assign neighbours to the unit
    for unit_number in range(total_units):
        wall_total = units[unit_number]
        if wall_total == 0:
            for surface in range(4):
                neighbour_unit_no = get_neighbour_unit_number(unit_number, 'WNES'[surface])
                unit_neighbours[unit_number][surface] = neighbour_unit_no
        while wall_total > 0:
            for exp in range(1, 5):
                if wall_total % pow(2, exp) == pow(2, exp - 1):
                    # wall exists
                    wall_total -= pow(2, exp - 1)
                else:
                    neighbour_unit_no = get_neighbour_unit_number(unit_number, 'WNES'[exp - 1])
                    unit_neighbours[unit_number][exp - 1] = neighbour_unit_no

    return unit_neighbours


class FloodFill:
    unit_neighbours = []
    assigned_rooms = []
    total_rooms = 0
    largest_room = 0
    queue = []
    room_sizes = []

    def __init__(self, unit_neighbours):
        self.assigned_rooms = [-1 for _ in range(total_units)]
        self.unit_neighbours = unit_neighbours

    def run(self):
        for unit_number in range(total_units):
            if self.assigned_rooms[unit_number] == -1:
                # start a new room since there is a node that has not been visited
                self.queue.append(unit_number)
                while len(self.queue) > 0:
                    # visit all units in the queue, assign them to the same room
                    unit_to_assign = self.queue.pop()
                    self.assigned_rooms[unit_to_assign] = self.total_rooms
                    for neighbour in range(4):
                        neighbour_number = self.unit_neighbours[unit_to_assign][neighbour]
                        if neighbour_number != -1 and self.assigned_rooms[neighbour_number] == -1:
                            self.queue.append(neighbour_number)
                # increment total rooms, since all units in the queue are in the same room
                self.total_rooms += 1

        self._compute_room_sizes()

    def _compute_room_sizes(self):
        self.room_sizes = [0 for _ in range(self.total_rooms)]
        for i in range(self.total_rooms):
            room_size = self.assigned_rooms.count(i)
            self.room_sizes[i] = room_size
            if room_size > self.largest_room:
                self.largest_room = room_size


units = []
for _ in range(N):
    units.extend(map(int, fin.readline().split()))

# initialize neighbouring_units with 4 -1s for each unit
neighbouring_units = [[-1 for _ in range(4)] for _ in range(total_units)]
neighbouring_units = assign_neighbours(neighbouring_units)

# run flood_fill for original plan
flood_fill = FloodFill(neighbouring_units)
flood_fill.run()

# find the largest room by combining two rooms
assigned_rooms = flood_fill.assigned_rooms
room_sizes = flood_fill.room_sizes
max_room_size = flood_fill.largest_room
largest_possible_room_size = 2*max_room_size
# wall farthest from the west, then south, then north, then east
dir_key = {'N': 1, 'E': 2, 'S': 3, 'W': 0}
rooms_already_combined = set()
largest_room_found = False

# start from the unit on the bottom left, and go up, then right
for column in range(M):
    if largest_room_found:
        break
    for row in range(N - 1, -1, -1):
        if largest_room_found:
            break
        unit = column + row * M
        for side in "NE":
            neighbour_unit_number = get_neighbour_unit_number(unit, side)
            # if valid neighbour and if there is a wall between neighbours, then remove the wall
            if neighbouring_units[unit][dir_key[side]] == - 1 and neighbour_unit_number != -1:
                # if a wall between two rooms has already been removed, then don't remove the wall to check again
                if (unit, neighbour_unit_number) in rooms_already_combined or (
                        neighbour_unit_number, unit) in rooms_already_combined:
                    continue
                # if two units are in the same room, then don't remove the wall
                if assigned_rooms[unit] == assigned_rooms[neighbour_unit_number]:
                    continue

                # otherwise, calculate the size of the combined room
                combined_room_size = room_sizes[assigned_rooms[unit]] + room_sizes[assigned_rooms[neighbour_unit_number]]
                rooms_already_combined.add((unit, neighbour_unit_number))

                if combined_room_size > max_room_size:
                    max_room_size = combined_room_size
                    max_room = (row + 1, column + 1, side)
                if max_room_size == largest_possible_room_size:
                    largest_room_found = True
                    break

fout.write(str(flood_fill.total_rooms) + '\n')
fout.write(str(flood_fill.largest_room) + '\n')
fout.write(str(max_room_size) + '\n')
fout.write(str(max_room[0]) + ' ' + str(max_room[1]) + ' ' + max_room[2] + '\n')

