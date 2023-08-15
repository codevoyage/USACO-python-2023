"""
ID: shikha11
LANG: PYTHON3
TASK: frac1
"""

fin = open('frac1.in', 'r')
fout = open('frac1.out', 'w')

N = int(fin.readline())

fraction_values = {}

for denominator in range(1, N + 1):
    for numerator in range(denominator + 1):
        value = numerator/denominator
        if value in fraction_values:
            num, den = fraction_values[value]
            if numerator < num or (numerator == num and denominator < den):
                fraction_values[value] = (numerator, denominator)
        else:
            fraction_values[value] = (numerator, denominator)

sorted_fractions = dict(sorted(fraction_values.items()))

for value in sorted_fractions:
    numerator, denominator = sorted_fractions[value]
    fout.write(f'{numerator}/{denominator}\n')
