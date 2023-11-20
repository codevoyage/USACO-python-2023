"""
ID: shikha11
LANG: PYTHON3
TASK: spin
"""
import math

fin = open('spin.in', 'r')
fout = open('spin.out', 'w')


class Wedge:
    def __init__(self, start, extent):
        self.start = start
        self.extent = extent


class Wheel:
    wedges = []

    def __init__(self, speed, wedges):
        self.speed = speed
        self.wedges = wedges

    def get_position(self, time):
        return int((self.speed * time) % 360)

    def get_open_spaces(self, time):
        open_spaces = []
        offset = self.get_position(time)

        for w in self.wedges:
            start = int((offset + w.start) % 360)
            end = int((start + w.extent) % 360)
            open_spaces.append((start, end))

        return open_spaces


# Function to check if the given arc contains the given point
def contains(interval, point):
    start = interval[0]
    end = interval[1]
    if start < end:
        return start <= point <= end
    elif start > end:
        return not (end < point < start)


# Function to get the intersection of two arcs
def get_intersections(space1, space2):
    s1, e1 = space1
    s2, e2 = space2

    intersections = []

    # Function to get the other end of the arc of the given endpoint
    def get_other_end(endpoint, point):
        if endpoint == "start":
            gap1 = 360 - point + e1 if e1 - point < 0 else e1 - point
            gap2 = 360 - point + e2 if e2 - point < 0 else e2 - point
            return e1 if gap1 < gap2 else e2
        elif endpoint == "end":
            gap1 = 360 - s1 + point if point - s1 < 0 else point - s1
            gap2 = 360 - s2 + point if point - s2 < 0 else point - s2
            return s1 if gap1 < gap2 else s2

    # if the start of the first arc lies on the second arc, find the intersection end point
    if contains(space2, s1):
        p = get_other_end("start", s1)
        intersections.append((s1,p))

    # if the end of the first arc lies on the second arc, find the intersection start point
    if contains(space2, e1):
        p = get_other_end("end", e1)
        intersections.append((p, e1))

    # if the start of the second arc lies on the first arc, find the intersection end point
    if contains(space1, s2):
        p = get_other_end("start", s2)
        intersections.append((s2, p))

    return intersections


def read_wheels_input(fin):
    wheels = []

    for i in range(5):
        line = fin.readline().strip().split()
        wheel_speed = int(line[0])
        num_wedges = int(line[1])
        wedges_list = []

        for j in range(num_wedges):
            start = int(line[2 * j + 2])
            extent = int(line[2 * j + 3])
            wedges_list.append(Wedge(start, extent))

        wheels.append(Wheel(wheel_speed, wedges_list))

    return wheels


def calculate_reset_time(wheels):
    denominator_gcd = wheels[0].speed

    for i in range(1, 5):
        denominator_gcd = math.gcd(denominator_gcd, wheels[i].speed)

    return math.ceil(360 / denominator_gcd)


def find_openings_over_time(wheels, reset_time):
    time = 0

    while time <= reset_time:
        initial_openings = wheels[0].get_open_spaces(time)
        for index in range(1, len(wheels)):
            new_openings = []
            current_openings = wheels[index].get_open_spaces(time)
            for space1 in initial_openings:
                for space2 in current_openings:
                    for new_space in get_intersections(space1, space2):
                        new_openings.append(new_space)
            if len(new_openings) == 0:
                time += 1
                break
            else:
                initial_openings = new_openings

        if len(new_openings) != 0:
            break

    return time, new_openings


def write_output(fout, time, new_openings):
    if len(new_openings) == 0:
        fout.write("none\n")
    else:
        fout.write(str(time) + "\n")


def main():
    wheels = read_wheels_input(fin)
    reset_time = calculate_reset_time(wheels)
    time, new_openings = find_openings_over_time(wheels, reset_time)
    write_output(fout, time, new_openings)


main()
