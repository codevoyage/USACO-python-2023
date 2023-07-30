"""
ID: shikha11
LANG: PYTHON3
TASK: milk3
"""

fin = open('milk3.in', 'r')
fout = open('milk3.out', 'w')

A, B, C = map(int, fin.readline().strip().split())
max_capacity = (A, B, C)


def is_A_empty(cur_state):
    return cur_state[0] == 0


def pour_into(cur_state, to_jar, from_jar):
    space_in_to_jar = max_capacity[to_jar] - cur_state[to_jar]
    from_state = max(cur_state[from_jar] - space_in_to_jar, 0)
    to_state = min(cur_state[from_jar] + cur_state[to_jar], max_capacity[to_jar])
    next_state = list(cur_state)
    next_state[to_jar] = to_state
    next_state[from_jar] = from_state
    return tuple(next_state)


def queue_next_states(cur_state):
    for from_jar in range(3):
        if cur_state[from_jar] == 0:
            continue
        for j in range(1, 3):
            to_jar = (from_jar + j) % 3
            next_state = pour_into(cur_state, to_jar, from_jar)
            if next_state not in visited_states:
                queued_states.append(next_state)



visited_states = set()
queued_states = list()
current_state = (0, 0, C)
queued_states.append(current_state)

C_capacities = set()
while len(queued_states) > 0:
    cur_state = queued_states.pop(0)
    visited_states.add(cur_state)
    queue_next_states(cur_state)

    if is_A_empty(cur_state):
        C_capacities.add(cur_state[2])

C_capacities = list(C_capacities)
C_capacities.sort()
for i in range(len(C_capacities)):
    fout.write(str(C_capacities[i]))
    if i != len(C_capacities) - 1:
        fout.write(" ")
fout.write("\n")
