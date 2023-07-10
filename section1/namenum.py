"""
ID: shikha11
LANG: PYTHON3
TASK: namenum
"""

fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')
number = fin.readline().strip()
numbers = list(str(number))

names = open('dict.txt', 'r').read().split('\n')
letters = {'2': ['A', 'B', 'C'],
           '3': ['D', 'E', 'F'],
           '4': ['G', 'H', 'I'],
           '5': ['J', 'K', 'L'],
           '6': ['M', 'N', 'O'],
           '7': ['P', 'R', 'S'],
           '8': ['T', 'U', 'V'],
           '9': ['W', 'X', 'Y']
           }

valid_names = False

# for each name, check if it maps to the number
for name in names:
    # if first letter of the name is less than the first letter of the number, continue
    if list(name)[0] < letters[numbers[0]][0]:
        continue
    # if first letter of the name is greater than the first letter of the number, break
    elif list(name)[0] > letters[numbers[0]][2]:
        break
    else:
        if len(name) == len(numbers):
            name_chars = list(name)
            for i in range(len(name_chars)):
                if name_chars[i] not in letters[numbers[i]]:
                    break
                if i == len(name_chars) - 1:
                    fout.write(name + '\n')
                    valid_names = True

if not valid_names:
    fout.write('NONE\n')
