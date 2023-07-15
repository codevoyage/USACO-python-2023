"""
ID: shikha11
LANG: PYTHON3
TASK: barn1
"""

fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')

M, S, C = map(int, fin.readline().strip().split())
occupied_stalls = []

for i in range(C):
    stall_number = int(fin.readline().strip())
    occupied_stalls.append(stall_number)

occupied_stalls.sort()

start_stall = occupied_stalls[0]
end_stall = occupied_stalls[-1]

gaps = {}
for i in range(C - 1):
    gaps[occupied_stalls[i]] = occupied_stalls[i + 1] - occupied_stalls[i]

gaps = sorted(gaps.items(), key=lambda x: x[1], reverse=True)

total_stalls = end_stall - start_stall + 1

# remove the number of stalls in the largest gaps from the total stalls
for i in range(min(M - 1, len(gaps))):
    total_stalls = total_stalls - (gaps[i][1] - 1)

fout.write(str(total_stalls) + '\n')
