"""
ID: shikha11
LANG: PYTHON3
TASK: inflate
"""

fin = open('inflate.in', 'r')
fout = open('inflate.out', 'w')

M, N = map(int, fin.readline().strip().split())

points = [0] * N
minutes = [0] * N
max_points = [0] * (M + 1)

for p in range(N):
    points[p], minutes[p] = map(int, fin.readline().strip().split())
    t = minutes[p]
    for time in range(t, M + 1):
        max_points[time] = max(max_points[time], max_points[time - t] + points[p])


fout.write(str(max_points[M]) + '\n')
fout.close()
