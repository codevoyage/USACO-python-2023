"""
ID: shikha11
LANG: PYTHON3
TASK: msquare
"""

fin = open('msquare.in', 'r')
fout = open('msquare.out', 'w')

target = fin.readline().strip().split()
target = [int(i) for i in target]
mid = 4
target = target[:mid] + target[mid:][::-1]


def A(state):
    return state[mid:] + state[:mid]


def B(state):
    def right_shift(half):
        return [half[-1]] + half[:-1]

    return right_shift(state[:mid]) + right_shift(state[mid:])


def C(state):
    o1, o2, o5, o6 = state[1], state[2], state[5], state[6]
    state[2], state[6], state[1], state[5] = o1, o2, o5, o6
    return state


transformations = {'A': A, 'B': B, 'C': C}

start_state = [1, 2, 3, 4, 8, 7, 6, 5]
if start_state == target:
    fout.write("0\n\n")
    exit(0)

states = set()
queue = [("", start_state)]
solution = None
while queue:
    (history, state) = queue.pop(0)
    for (name, transform) in transformations.items():
        new_state = transform(state)
        if tuple(new_state) in states:
            continue
        if new_state == target:
            solution = history + name
            break
        else:
            queue.append((history + name, new_state))

    if solution is not None:
        break
    states.add(tuple(state))

if solution is None:
    fout.write("NONE\n")
else:
    fout.write(str(len(solution)) + "\n")
    for i in range(0, len(solution), 60):
        line_end = min(i + 60, len(solution[i:]))
        fout.write(solution[i:i + line_end] + "\n")

