"""
ID: shikha11
LANG: PYTHON3
TASK: ride
"""
import string

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

comet, group = fin.read().splitlines()

letter_postion = dict(zip(string.ascii_uppercase, range(1,27)))

comet_code = 1
for letter in comet:
  comet_code = comet_code * letter_postion[letter]

group_code = 1
for letter in group:
  group_code = group_code * letter_postion[letter]

sum = 'GO' if comet_code % 47 == group_code % 47 else 'STAY'

fout.write (str(sum) + '\n')
fout.close()
