"""
ID: shikha11
LANG: PYTHON3
TASK: stamps
"""

fin = open('stamps.in', 'r')
fout = open('stamps.out', 'w')

K, N = map(int, fin.readline().strip().split())

while True:
    line = fin.readline()
    if not line or not line[0].isdigit():
        break
    stamps = list(map(int, line.strip().split()))

max_stamp = max(stamps)
max_value = max_stamp * K

# Initialize a 1D array to store the minimum number of coins needed for each value
dp = [float('inf')] * (max_value + 1)
dp[0] = 0

for coin in stamps:
    for value in range(coin, max_value + 1):
        dp[value] = min(dp[value], dp[value - coin] + 1)

n = 0
while n <= max_value and dp[n] <= K:
    n += 1

fout.write(str(n - 1) + '\n')

# max_stamp = max(stamps)
# max_value = max_stamp * K
#
#
# possible = [[False] * (max_value + 1) for _ in range(2)]
# possible[0][0] = True
# for stamp in stamps:
#     possible[0][stamp] = True
#
# c = 1
# for num_coins in range(2, K + 1):
#     for value in range(0, num_coins * max_stamp + 1):
#         possible[c][value] = possible[c - 1][value]
#
#         # if it's possible with lesser number of coins, then move on
#         if possible[c][value]:
#             continue
#
#         # otherwise check if adding any coin will make it possible
#         for coin in stamps:
#             if value - coin >= 0 and possible[c - 1][value - coin]:
#                 possible[c][value] = True
#                 break
#
#     possible[c-1] = possible[1]
#     possible[1] = [False] * (max_value + 1)
#
# n = 0
# while n <= max_value:
#     if possible[0][n]:
#         n += 1
#     else:
#         break
#
# fout.write(str(n - 1) + '\n')
