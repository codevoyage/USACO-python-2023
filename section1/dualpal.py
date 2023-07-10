"""
ID: shikha11
LANG: PYTHON3
TASK: dualpal
"""

fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')

N, S = map(int, fin.readline().strip().split())


def is_palindrome(number):
    number = str(number)
    if len(number) == 1:
        return True
    elif len(number) == 2:
        if number[0] == number[1]:
            return True
        else:
            return False
    else:
        if number[0] == number[-1]:
            return is_palindrome(number[1:-1])
        else:
            return False


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def to_base(number, B):
    number = int(number)

    if number == 0:
        return
    elif number < B:
        return digits[number]

    q = number / B
    r = number % B

    return to_base(q, B) + digits[r]


number = S+1
while N > 0:
    pal_count = 0
    for B in range(2, 11):
        if is_palindrome(to_base(number, B)):
            pal_count += 1
            if pal_count == 2:
                fout.write(str(number) + '\n')
                N -= 1
                break
    number += 1
