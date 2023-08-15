"""
ID: shikha11
LANG: PYTHON3
TASK: sort3
"""
fin = open('sort3.in', 'r')
fout = open('sort3.out', 'w')

N = int(fin.readline())
unordered_list = []
for i in range(N):
    unordered_list.append(int(fin.readline()))

sorted_list = sorted(unordered_list)
swaps = 0

# compute ranges
ranges = []
end = 0
for num in range(1, 4):
    start = end
    for i in range(start, N):
        if sorted_list[i] != num:
            break
    end = i
    if num == 3:
        ranges.append((start, end))
    else:
        ranges.append((start, end - 1))

for i in range(N):
    if unordered_list[i] != sorted_list[i]:
        # swap is needed
        out_of_place_num = unordered_list[i]
        desired_number = sorted_list[i]
        misplaced_num_range = ranges[out_of_place_num - 1]

        swap_found = False
        # check if desired number is in the range of misplaced numbers
        for place in range(misplaced_num_range[0], misplaced_num_range[1] + 1):
            if unordered_list[place] == sorted_list[i]:
                # perform swap
                unordered_list[place] = out_of_place_num
                unordered_list[i] = desired_number
                swaps += 1
                swap_found = True
                break
                
        # if not, check for the desired number in the rest of the list
        if not swap_found:
            for place in range(place, N):
                if unordered_list[place] == desired_number:
                    # perform swap
                    unordered_list[place] = out_of_place_num
                    unordered_list[i] = desired_number
                    swaps += 1
                    break


fout.write(f'{swaps}\n')



