"""
ID: shikha11
LANG: PYTHON3
TASK: humble
"""

fin = open('humble.in', 'r')
fout = open('humble.out', 'w')

K, N = map(int, fin.readline().strip().split())
primes = set(map(int, fin.readline().strip().split()))

humble_numbers = set(primes)
last_humble_number = 0

number = 1
while len(humble_numbers) < N:
    number += 1
    if number in humble_numbers:
        continue

    n = number
    for prim in primes:
        if int(n % prim) == 0:
            n = int(n / prim)
            if n in humble_numbers:
                humble_numbers.add(number)
                last_humble_number = number
                break

fout.write(str(last_humble_number) + '\n')