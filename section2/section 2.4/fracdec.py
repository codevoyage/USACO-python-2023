"""
ID: shikha11
LANG: PYTHON3
TASK: fracdec
"""

fin = open('fracdec.in', 'r')
fout = open('fracdec.out', 'w')

n, d = map(int, fin.readline().strip().split())

position = 0
remainders_seen = {}

remainder = int(n % d)
before_decimal = int(n/d)

if remainder == 0:
    answer = '{:.1f}'.format(before_decimal)
else:
    decimal = ''
    while position < d:
        if remainder in remainders_seen:
            pos = remainders_seen[remainder]
            decimal = decimal[:pos] + '(' + decimal[pos:] + ')'
            answer = str(before_decimal) + '.' + decimal
            break

        remainders_seen[remainder] = position
        n = remainder*10
        remainder = int(n % d)
        quotient = int(n / d)
        decimal = decimal + str(quotient)
        position += 1
        if remainder == 0:
            answer = str(before_decimal) + '.' + decimal
            break


for i in range(0, len(answer), 76):
    fout.write(answer[i:i+76] + '\n')