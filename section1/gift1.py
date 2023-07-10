"""
ID: shikha11
LANG: PYTHON3
TASK: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

np = int(fin.readline().strip())
group = dict()

for i in range(np):
  name = fin.readline().strip()
  group[name] = 0


while True:
    member = fin.readline().strip()
    if not member:
        break
    total, friends = map(int,fin.readline().strip().split())
    if friends != 0:
        group[member] -= total - (total % friends)
        for i in range(int(friends)):
          friend = fin.readline().strip()
          group[friend] += int(total) // int(friends)


for name in group:
  fout.write(name + ' ' + str(group[name]) + '\n')