"""
ID: shikha11
LANG: PYTHON3
TASK: lamps
"""

fin = open('lamps.in', 'r')
fout = open('lamps.out', 'w')

n = int(fin.readline().strip())
c = int(fin.readline().strip())

on_lamps = set(map(int, fin.readline().strip().split()))
off_lamps = set(map(int, fin.readline().strip().split()))

on_lamps.discard(-1)
off_lamps.discard(-1)


def all_button(lamps_state):
    for i in range(n):
        lamps_state[i] = lamps_state[i] ^ 1
    return lamps_state


def odd_button(lamps_state):
    for i in range(0, n, 2):
        if i >= n:
            break
        lamps_state[i] = lamps_state[i] ^ 1
    return lamps_state


def even_button(lamps_state):
    for i in range(1, n, 2):
        if i >= n:
            break
        lamps_state[i] = lamps_state[i] ^ 1
    return lamps_state


def every_third_button(lamps_state):
    for i in range(0, n, 3):
        if i >= n:
            break
        lamps_state[i] = lamps_state[i] ^ 1
    return lamps_state


def is_state_valid(state):
    for i in range(n):
        if i + 1 in on_lamps and state[i] != 1:
            return False

        if i + 1 in off_lamps and state[i] != 0:
            return False

    return True


def generate_set(set_size, start_from, set_so_far):
    if set_size <= 0:
        set_tuple = tuple(set_so_far)
        all_combinations.append(set_tuple)
        return

    for i in range(start_from, len(buttons)):
        set_so_far.append(i)
        generate_set(set_size - 1, i + 1, set_so_far)
        set_so_far.remove(i)


buttons = [all_button, even_button, odd_button, every_third_button]

solution = set()
all_combinations = []

if c == 0:
    cur_state = [1] * n
    if is_state_valid(cur_state):
        solution.add("".join(map(str, cur_state)))
elif c == 1:
    for func_nums in range(1, 2):
        generate_set(func_nums, 0, [])
elif c == 2:
    for func_nums in range(2, 3):
        generate_set(func_nums, 0, [])
elif c == 3:
    for func_nums in range(1, 4):
        generate_set(func_nums, 0, [])
else:
    for func_nums in range(1, 5):
        generate_set(func_nums, 0, [])

for combo in all_combinations:
    cur_state = [1] * n
    for button_press in combo:
        cur_state = buttons[button_press](cur_state)
    if is_state_valid(cur_state):
        solution.add("".join(map(str, cur_state)))

solution = sorted(solution)

if len(solution) == 0:
    fout.write('IMPOSSIBLE\n')
else:
    for state in solution:
        fout.write(f'{state}\n')
