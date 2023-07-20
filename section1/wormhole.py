"""
ID: shikha11
LANG: PYTHON3
TASK: wormhole
"""

fin = open('wormhole.in', 'r')
fout = open('wormhole.out', 'w')


def is_loop(starting_point, paired_dict, visited_wormholes):
    # if visiting a wormhole that has already been visited, then we have a loop
    if starting_point in visited_wormholes:
        return True

    visited_wormholes.append(starting_point)

    # start walking in +x direction from the starting point, check to see if we can find a wormhole
    current_position = starting_point
    current_row = wormholes_rows[current_position[1]]
    for x in range(len(current_row)):
        if current_row[x] == current_position[0]:
            if x == len(current_row) - 1:
                next_x = None
            else:
                next_x = current_row[x + 1]
            break

    if next_x is None:
        return False
    else:
        next_wormhole = (next_x, current_position[1])
        visited_wormholes.append((next_wormhole, current_position[1]))
        return is_loop(paired_dict[next_wormhole], paired_dict, visited_wormholes)


def is_infinite_combination(generated_combination):
    # check for a loop by starting at each wormhole in the generated combination
    for wmhole in generated_combination:
        starting_point = wmhole
        if is_loop(starting_point, generated_combination, []):
            return True


def pair_wormholes(wormhole_status, generated_combination):
    wormhole_seeking_pair = None
    # find the wormhole that is seeking a pair
    for wormhole_ready_to_pair in wormhole_status:
        if wormhole_ready_to_pair[1] == "unpaired":
            wormhole_seeking_pair = wormhole_ready_to_pair
            break

    # if no wormhole is seeking a pair, then we have a combination
    if wormhole_seeking_pair is None and is_infinite_combination(generated_combination):
        global loop_combinations
        loop_combinations += 1
        return

    # if we found a wormhole that is seeking a pair, then find a pair
    for wormhole_ready_to_pair in wormhole_status:
        if wormhole_ready_to_pair[1] == "unpaired" and wormhole_ready_to_pair is not wormhole_seeking_pair:
            # found a suitable pair
            wormhole_seeking_pair[1] = "paired"
            wormhole_ready_to_pair[1] = "paired"

            generated_combination[wormhole_seeking_pair[0]] = wormhole_ready_to_pair[0]
            generated_combination[wormhole_ready_to_pair[0]] = wormhole_seeking_pair[0]

            # pair the rest of the unpaired wormholes
            pair_wormholes(wormhole_status, generated_combination)

            # remove the wormhole from the generated combination
            generated_combination.pop(wormhole_seeking_pair[0])
            generated_combination.pop(wormhole_ready_to_pair[0])

            # unpair the wormholes to try other combinations
            wormhole_seeking_pair[1] = "unpaired"
            wormhole_ready_to_pair[1] = "unpaired"


N = int(fin.readline().strip())
wormholes = []
for i in range(N):
    wormholes.append(tuple(map(int, fin.readline().strip().split())))

wormholes_rows = {}
for wh in wormholes:
    if wh[1] not in wormholes_rows:
        wormholes_rows[wh[1]] = []
    wormholes_rows[wh[1]].append(wh[0])

for rows in wormholes_rows.items():
    sorted(rows[1])

loop_combinations = 0

# track the pairing status of each wormhole
wormholes_status = []
for i in range(N):
    wormholes_status.append([None, None])
    wormholes_status[i][0] = wormholes[i]
    wormholes_status[i][1] = "unpaired"

pair_wormholes(wormholes_status, {})

fout.write(str(loop_combinations) + '\n')
