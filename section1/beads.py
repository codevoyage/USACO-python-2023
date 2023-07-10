"""
ID: shikha11
LANG: PYTHON3
TASK: beads
"""

fin = open('transform.in', 'r')
fout = open('beads.out', 'w')

beads = int(fin.readline().strip())
necklace = fin.readline().strip()

max_len = 0

broken_necklace = necklace + necklace

for i in range(len(broken_necklace) - 1):
    color = None
    left = i - 1
    while 0 <= left:
        if not color and broken_necklace[left] != 'w':
            color = broken_necklace[left]
        if broken_necklace[left] == color or broken_necklace[left] == 'w':
            left -= 1
        else:
            break

    color = None
    right = i
    for right in range(i, len(broken_necklace)):
        if not color and broken_necklace[right] != 'w':
            color = broken_necklace[right]
        if broken_necklace[right] == color or broken_necklace[right] == 'w':
            continue
        else:
            break

    max_len = max(max_len, right - left - 1)

fout.write(str(min(max_len, len(necklace))) + '\n')
