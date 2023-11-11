"""
ID: shikha11
LANG: PYTHON3
TASK: kimbits
"""

fin = open('kimbits.in', 'r')
fout = open('kimbits.out', 'w')

N, L, I = map(int, fin.readline().strip().split())

exact_solutions = [[0 for _ in range(L + 1)] for _ in range(N + 1)]
exact_solutions[0][0] = 1
upto_solutions = [[0 for _ in range(L + 1)] for _ in range(N + 1)]
upto_solutions[0] = [1 for _ in range(L + 1)]

for n in range(1, N + 1):
    for l in range(L + 1):
        if l == 0:
            exact_solutions[n][l] = 1
            upto_solutions[n][l] = 1
        else:
            exact_solutions[n][l] = exact_solutions[n - 1][l] + exact_solutions[n - 1][l - 1]
            upto_solutions[n][l] = upto_solutions[n][l - 1] + exact_solutions[n][l]


def generate_kimbit(num_length, max_bits, position):
    if num_length == 0:
        return ""

    if position > upto_solutions[num_length - 1][max_bits]:
        kimbit = "1" + generate_kimbit(num_length - 1, max_bits - 1, position - upto_solutions[num_length - 1][max_bits])
    else:
        kimbit = "0" + generate_kimbit(num_length - 1, max_bits, position)

    return kimbit


result = generate_kimbit(N, L, I)
fout.write(result + '\n')
