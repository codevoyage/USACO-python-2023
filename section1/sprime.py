"""
ID: shikha11
LANG: PYTHON3
TASK: sprime
"""
import math

fin = open('sprime.in', 'r')
fout = open('sprime.out', 'w')

N = int(fin.readline().strip())


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


cur_primes = [2, 3, 5, 7]
next_primes = []

add_digits = [1, 3, 7, 9]
l = 1

while l < N:
    for prime in cur_primes:
        for last in add_digits:
            new_prime = prime * 10 + last
            if is_prime(new_prime):
                next_primes.append(new_prime)
    l += 1
    cur_primes = next_primes
    next_primes = []

for sprime in cur_primes:
    fout.write(str(sprime) + '\n')
