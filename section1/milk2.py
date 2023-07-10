"""
ID: shikha11
LANG: PYTHON3
TASK: milk2
"""


def does_overlap(a, b):
    if a[0] <= b[0] <= a[1]:
        return True
    elif a[0] <= b[1] <= a[1]:
        return True
    elif b[0] <= a[0] and b[1] >= a[1]:
        return True
    else:
        return False

fin = open ('transform.in', 'r')
fout = open ('milk2.out', 'w')

n = int(fin.readline().strip())
intervals = []

for(i) in range(n):
    start, end = map(int, fin.readline().strip().split())
    intervals.append((start, end))

intervals.sort()

current_interval = intervals[0]
max_milked = current_interval[1] - current_interval[0]
max_idle = 0

for i in range(1, n):
    if does_overlap(current_interval, intervals[i]):
        current_interval= (min(current_interval[0], intervals[i][0]), max(current_interval[1], intervals[i][1]))
    else:
        max_milked= max(max_milked, current_interval[1]-current_interval[0])
        max_idle=max(max_idle, intervals[i][0]-current_interval[1])
        current_interval= intervals[i]

fout.write(str(max_milked) + ' ' + str(max_idle) + '\n')


