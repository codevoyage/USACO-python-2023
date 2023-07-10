"""
ID: shikha11
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

years = int(fin.readline().strip())
days = [0, 0, 0, 0, 0, 0, 0]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

for year in range(1900, 1900 + years):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28

    for month in range(12):
        days[(day + 13) % 7] += 1
        day = (day + days_in_month[month]) % 7

for i in range(7):
    if (i > 0):
        fout.write(" ")
    fout.write(str(days[(6 + i) % 7]))
fout.write("\n")

