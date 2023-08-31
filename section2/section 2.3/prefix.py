"""
ID: shikha11
LANG: PYTHON3
TASK: prefix
"""

fin = open('prefix.in', 'r')
fout = open('prefix.out', 'w')

primitives_set = set()
line = fin.readline().strip()
while line != '.':
    primitives_set.update(line.split())
    line = fin.readline().strip()

lines = []  # Create an empty list to store lines
while line != '':
    line = fin.readline().strip()
    lines.append(line)  # Append each line to the list
sequence = ''.join(lines)  # join lines to form a sequence

sequence_length = len(sequence)
max_primitive_length = max([len(primitive) for primitive in primitives_set])
longest_starting_at = [0] * sequence_length

if sequence[-1] in primitives_set:
    longest_starting_at[-1] = 1

for i in range(sequence_length - 2, -1, -1):
    for j in range(i, i + max_primitive_length + 1):
        sub_sequence = sequence[i:j + 1]
        sub_sequence_len = j - i + 1

        if j + 1 >= sequence_length:
            break

        if sub_sequence in primitives_set:
            longest_starting_at[i] = max(longest_starting_at[i], sub_sequence_len + longest_starting_at[j + 1])

fout.write(f'{longest_starting_at[0]}\n')
