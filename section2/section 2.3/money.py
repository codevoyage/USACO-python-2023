"""
ID: shikha11
LANG: PYTHON3
TASK: money
"""

fin = open('money.in', 'r')
fout = open('money.out', 'w')

v, n = map(int, fin.readline().strip().split())
coins = list(map(int, fin.read().strip().split()))

# number of ways to make change for amount i using coins[0..j]
ways = [[0] * (n + 1) for _ in range(v + 1)]
ways[0][0] = 1

for c in range(1, v + 1):
    for value in range(n + 1):
        ways[c][value] = ways[c - 1][value]

        coin = coins[c - 1]
        if coin > value:
            continue

        if c == 1 and int(value % coin) == 0:
            ways[c][value] = 1
        else:
            ways[c][value] += ways[c][value - coin]


fout.write(str(ways[v][n]) + '\n')
