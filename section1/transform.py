"""
ID: shikha11
LANG: PYTHON3
TASK: transform
"""

fin = open('transform.in', 'r')
fout = open('transform.out', 'w')

n = int(fin.readline().strip())

original = []
transformed = []

for i in range(n):
    original.append(list(fin.readline().strip()))
for i in range(n):
    transformed.append(list(fin.readline().strip()))


def rotate_90(original):
    rotated = []
    for i in range(n):
        rotated.append([])
        for j in range(n):
            rotated[i].append(original[n-1-j][i])
    return rotated


def reflect(original):
    reflected = []
    for i in range(n):
        reflected.append([])
        for j in range(n):
            reflected[i].append(original[i][n - 1 - j])
    return reflected


def check_rotation(og, transformed):
    for i in range(1, 3):
        og = rotate_90(og)
        if og == transformed:
            return i
    return 0


if check_rotation(original, transformed) > 0:
    fout.write(str(check_rotation(original, transformed)) + '\n')
elif reflect(original) == transformed:
    fout.write('4\n')
elif check_rotation(reflect(original), transformed) > 0:
    fout.write('5\n')
elif transformed == original:
    fout.write('6\n')
else:
    fout.write('7\n')
