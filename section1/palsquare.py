"""
ID: shikha11
LANG: PYTHON3
TASK: palsquare
"""

fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')

B = int(fin.readline().strip())


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


for i in range(1, 301):
    square_base = to_base(i ** 2, B)
    if is_palindrome(square_base):
        fout.write(to_base(i, B) + ' ' + square_base + '\n')
