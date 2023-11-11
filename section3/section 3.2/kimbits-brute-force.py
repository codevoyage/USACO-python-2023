"""
ID: shikha11
LANG: PYTHON3
TASK: kimbits
"""

fin = open('kimbits.in', 'r')
fout = open('kimbits.out', 'w')

N, L, I = map(int, fin.readline().strip().split())

numbers = ["0", "1"]
bit_count = [0, 1]

for i in range(2, N + 1):
    old_numbers_len = len(numbers)
    for j in range(old_numbers_len):
        bit = numbers.pop(0)
        numbers.append("0" + bit)
        old_bit_count = bit_count.pop(0)
        bit_count.append(old_bit_count)
        if old_bit_count < L:
            numbers.append("1" + bit)
            bit_count.append(old_bit_count + 1)
    if len(numbers) > I:
        break

numbers = sorted(numbers)
if len(numbers[I - 1]) < N:
    fout.write("0" * (N - len(numbers[I - 1])) + numbers[I - 1] + '\n')
else:
    fout.write(numbers[I - 1] + '\n')
