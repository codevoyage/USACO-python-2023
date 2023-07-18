"""
ID: shikha11
LANG: PYTHON3
TASK: combo
"""

fin = open('combo.in', 'r')
fout = open('combo.out', 'w')

N = int(fin.readline().strip())
john = list(map(int, fin.readline().strip().split()))
master = list(map(int, fin.readline().strip().split()))

total_combinations = []


def get_dial_number(n, i):
    if n + i == -1:
        fn = N - 1
        if fn == 0:
            fn = N
    elif n + i == 0:
        fn = N
    elif n + i > N:
        fn = (n + i) % N
    else:
        fn = n + i

    return fn


for i in range(-2, 3):
    first_john = get_dial_number(john[0], i)
    first_master = get_dial_number(master[0], i)
    for j in range(-2, 3):
        second_john = get_dial_number(john[1], j)
        second_master = get_dial_number(master[1], j)
        for k in range(-2, 3):
            third_john = get_dial_number(john[2], k)
            third_master = get_dial_number(master[2], k)

            total_combinations.append((first_john, second_john, third_john))
            total_combinations.append((first_master, second_master, third_master))

total_combinations_set = set(total_combinations)

fout.write(str(len(total_combinations_set)) + '\n')
