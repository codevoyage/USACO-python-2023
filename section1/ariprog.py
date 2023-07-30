"""
ID: shikha11
LANG: PYTHON3
TASK: ariprog
"""

fin = open('ariprog.in', 'r')
fout = open('ariprog.out', 'w')

N = int(fin.readline().strip())
M = int(fin.readline().strip())

bi_squares = set()

for p in range(M + 1):
    for q in range(p, M + 1):
        bi_squares.add(p * p + q * q)

max_bisquare = 2 * M * M

sequences = {}
for start in bi_squares:
    max_difference = int((max_bisquare - start) / (N - 1))
    for b in range(max_difference, 0, -1):
        for length in range(N - 1, -1, -1):
            seq_num = start + length * b
            if seq_num not in bi_squares:
                break

        if length == 0:
            if b not in sequences:
                sequences[b] = []
            sequences[b].append(start)

if sequences == {}:
    fout.write("NONE\n")
else:
    sequences = dict(sorted(sequences.items()))
    for seq in sequences:
        starts = sequences[seq]
        starts.sort()
        for start in starts:
            fout.write(str(start) + " " + str(seq) + "\n")