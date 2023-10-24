"""
ID: shikha11
LANG: PYTHON3
TASK: humble
"""
import heapq

fin = open('humble.in', 'r')
fout = open('humble.out', 'w')

K, N = map(int, fin.readline().strip().split())
primes = sorted(list(map(int, fin.readline().strip().split())))

humble_numbers = list(primes)
heapq.heapify(humble_numbers)
seen = set()

largest_humble = 0
n = 0
while n < N:
    smallest_humble = heapq.heappop(humble_numbers)
    n += 1
    for prime in primes:
        new_humble = smallest_humble * prime
        if new_humble in seen:
            continue

        # limit the size of the heap to 100000 to prevent memory error
        if len(humble_numbers) > 100000 and new_humble > largest_humble:
            break

        heapq.heappush(humble_numbers, new_humble)
        seen.add(new_humble)
        largest_humble = max(largest_humble, new_humble)

fout.write(str(smallest_humble) + '\n')
