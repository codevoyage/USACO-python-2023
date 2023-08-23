"""
ID: shikha11
LANG: PYTHON3
TASK: hamming
"""

fin = open('hamming.in', 'r')
fout = open('hamming.out', 'w')

N, B, D = map(int, fin.readline().split())


def count_ones_in_binary(num):
    count = 0
    while num > 0:
        if num & 1 == 1:
            count += 1
        num >>= 1

    return count


max_decimal = pow(2, B)


def find_hamming_numbers(start_num, numbers_to_find, hamming_numbers):
    if numbers_to_find == 0:
        return True

    for number in range(start_num, max_decimal):
        is_hamming = True
        for hamming_num in hamming_numbers:
            xor = hamming_num ^ number

            ones = count_ones_in_binary(xor)

            if ones < D:
                is_hamming = False
                break

        if not is_hamming:
            continue

        hamming_numbers.append(number)
        found_sol = find_hamming_numbers(number + 1, numbers_to_find - 1, hamming_numbers)
        if found_sol:
            return hamming_numbers
        else:
            hamming_numbers.remove(number)


hamming_numbers_sol = find_hamming_numbers(1, N-1, [0])

for i in range(N):
    fout.write(f'{hamming_numbers_sol[i]}')
    if i < N - 1 and (i + 1) % 10 != 0:
        fout.write(' ')
    elif i < N - 1:
        fout.write('\n')

fout.write('\n')
