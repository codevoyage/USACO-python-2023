"""
ID: shikha11
LANG: PYTHON3
TASK: preface
"""

fin = open('preface.in', 'r')
fout = open('preface.out', 'w')

n = int(fin.readline().strip())

roman_dict = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
    5000: "W",
    10000: "Z"
}


def roman_numeral(n):
    if n == 0:
        return []

    len_num = len(str(n))
    base = pow(10, len_num - 1)
    remainder = int(n % base)
    n = n - remainder
    mid = 5 * base
    roman = []

    if base <= n < mid:
        higher = mid
    else:
        higher = pow(10, len_num)

    if higher - n == base:
        roman.append(roman_dict[base])
        roman.append(roman_dict[higher])
    else:
        if n >= mid:
            roman.append(roman_dict[mid])
            n = n - mid
        while n > 0:
            roman.append(roman_dict[base])
            n = n - base

    if remainder == 0:
        return roman

    return roman + roman_numeral(remainder)


count_chars = {}
for num in range(1, n + 1):
    roman = roman_numeral(num)
    for char in roman:
        if char not in count_chars:
            count_chars[char] = 1
        else:
            count_chars[char] += 1

for char in roman_dict.values():
    if char in count_chars:
        fout.write(f'{char} {count_chars[char]}\n')
