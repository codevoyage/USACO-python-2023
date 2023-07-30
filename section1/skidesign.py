"""
ID: shikha11
LANG: PYTHON3
TASK: skidesign
"""

fin = open('skidesign.in', 'r')
fout = open('skidesign.out', 'w')

n = int(fin.readline().strip())
hills = []

min_hill = 101
max_hill = -1

for i in range(n):
    height = int(fin.readline().strip())
    hills.append(height)

    min_hill = height if height < min_hill else min_hill
    max_hill = height if height > max_hill else max_hill

least_money = 25000000
for lowest in range(min_hill, max_hill - 16):
    window = (lowest, lowest + 17)
    money = 0
    for hill in hills:
        if hill < window[0] or hill > window[1]:
            diff = min(abs(window[0]-hill), abs(hill-window[1]))
            money = money + diff*diff

    least_money = min(least_money, money)


fout.write(str(least_money) + '\n')


