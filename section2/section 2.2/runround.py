"""
ID: shikha11
LANG: PYTHON3
TASK: runround
"""

fin = open('runround.in', 'r')
fout = open('runround.out', 'w')

n = int(fin.readline().strip())


def is_runround(num):
    num_str = str(num)
    num_len = len(num_str)
    visited = set()

    current = 0

    while current not in visited:
        visited.add(current)
        current = (int(num_str[current]) + current) % num_len

    return len(visited) == num_len and current == 0


def are_numbers_unique(num):
    num_str = str(num)
    unique = set(num_str)
    return len(unique) == len(num_str)


def contains_0(num):
    return '0' in str(num)


while True:
    n += 1
    if contains_0(n) or not are_numbers_unique(n):
        continue
    if is_runround(n):
        break

fout.write(f'{n}\n')
