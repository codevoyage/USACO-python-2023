"""
ID: shikha11
LANG: PYTHON3
TASK: subset
"""

fin = open('subset.in', 'r')
fout = open('subset.out', 'w')

n = int(fin.readline().strip())
total = n * (n + 1) // 2 # Sum of all numbers from 1 to n

# If the sum of all numbers from 1 to n is odd, then there is no way to divide the numbers into two subsets of equal sum
if total % 2 == 1:
    fout.write('0\n')
    exit()

# If the sum of all numbers from 1 to n is even, then the sum of each subset must be total // 2
total = total // 2

dp = [[0] * (total + 1) for _ in range(n + 1)]

dp[0][0] = 1

for subset_number in range(1, n + 1):
    for subset_sum in range(total + 1):
        if subset_sum > subset_number * (subset_number + 1) // 2:
            break

        dp[subset_number][subset_sum] = dp[subset_number - 1][subset_sum]

        if subset_sum - subset_number >= 0:
            dp[subset_number][subset_sum] += dp[subset_number - 1][subset_sum - subset_number]

fout.write(f'{dp[n][total]//2}\n')
