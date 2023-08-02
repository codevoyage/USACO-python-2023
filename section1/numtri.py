"""
ID: shikha11
LANG: PYTHON3
TASK: numtri
"""

fin = open('numtri.in', 'r')
fout = open('numtri.out', 'w')

N = int(fin.readline().strip())
tree = [[int(x) for x in fin.readline().strip().split()] for i in range(N)]
tree_sums = [[0 for x in range(N)] for i in range(N)]
tree_sums[N-1] = tree[N-1]

for row in range(N-2, -1, -1):
    for col in range(row+1):
        tree_sums[row][col] = tree[row][col] + max(tree_sums[row+1][col], tree_sums[row+1][col+1])

fout.write(tree_sums[0][0] + "\n")