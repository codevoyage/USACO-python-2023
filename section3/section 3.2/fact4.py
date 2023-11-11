"""
ID: shikha11
LANG: PYTHON3
TASK: fact4
"""

fin = open('fact4.in', 'r')
fout = open('fact4.out', 'w')

N = int(fin.readline().strip())

last_digits = 1
for multiplier in range(2, N + 1):
    product = last_digits * multiplier
    while product % 10 == 0:
        product //= 10

    last_digits = int(str(product)[-3:])

fout.write(str(last_digits)[-1] + '\n')
