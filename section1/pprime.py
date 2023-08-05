"""
ID: shikha11
LANG: PYTHON3
TASK: pprime
"""
import math

fin = open('pprime.in', 'r')
fout = open('pprime.out', 'w')

A, B = map(int, fin.readline().strip().split())
generated_palindromes = []

len_A = len(str(A))
len_B = len(str(B))


def generate_palindromes():
    for length in range(len_A, len_B + 1):
        half_length = int(length / 2)
        min_num = int(pow(10, half_length - 1))
        max_num = pow(10, half_length)
        palindrome = 0
        for half_num in range(min_num, max_num):
            if palindrome > B:
                return
            if length % 2 == 0:
                palindrome = int(str(half_num) + str(half_num)[::-1])
                generated_palindromes.append(palindrome)
            else:
                for middle in range(10):
                    if half_num == 0:
                        palindrome = middle
                    else:
                        palindrome = int(str(half_num) + str(middle) + str(half_num)[::-1])
                    generated_palindromes.append(palindrome)


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


generate_palindromes()
for pal in generated_palindromes:
    if A <= pal <= B and is_prime(pal):
        fout.write(str(pal) + '\n')
