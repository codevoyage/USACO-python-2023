"""
ID: shikha11
LANG: PYTHON3
TASK: crypt1
"""

fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')

N = int(fin.readline().strip())
digits = list(map(int, fin.readline().strip().split()))

allowed_digits = []
for i in range(10):
    allowed_digits.append(0)

for i in digits:
    allowed_digits[i] = 1


def is_valid(n):
    d = n % 10
    if allowed_digits[d] == 1:
        n = int(n / 10)
        if n == 0:
            return True
        else:
            return is_valid(n)
    else:
        return False


def check_partial(n):
    return len(str(n)) == 3 and is_valid(n)


valid_2_digit = []
# generate all possible 2-digit numbers
for i in range(10, 100):
    if is_valid(i):
        valid_2_digit.append(i)

valid_3_digit = []
# generate all possible 3-digit numbers
for i in range(100, 1000):
    if is_valid(i):
        valid_3_digit.append(i)

solutions = 0
for three_digit in valid_3_digit:
    for two_digit in valid_2_digit:
        n1 = two_digit % 10
        n2 = int(two_digit / 10)

        partial1 = three_digit * n1
        partial2 = three_digit * n2

        if not check_partial(partial1) or not check_partial(partial2):
            continue

        product = partial2 * 10 + partial1

        if len(str(product)) != 4 or not is_valid(product):
            continue

        solutions += 1

fout.write(str(solutions) + "\n")
