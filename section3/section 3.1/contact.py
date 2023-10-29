"""
ID: shikha11
LANG: PYTHON3
TASK: contact
"""

# Read input and open output file
with open('contact.in', 'r') as fin, open('contact.out', 'w') as fout:
    A, B, N = map(int, fin.readline().strip().split())

    # Initialize variables
    sequence = ''
    sequences = {}

    # Read and process the input
    for line in fin:
        if line[0] not in ('0', '1'):
            break
        sequence += line.strip()

    # Count subsequences
    for position in range(len(sequence)):
        for length in range(A, B + 1):
            if position + length > len(sequence):
                break
            subsequence = sequence[position:position + length]
            sequences[subsequence] = sequences.get(subsequence, 0) + 1

    # Sort the sequences by count in descending order
    sorted_sequences = sorted(sequences.items(), key=lambda item: item[1], reverse=True)

    for _ in range(N):
        if not sorted_sequences:
            break

        max_sequences = [sorted_sequences[0]]
        max_len = max_sequences[0][1]
        sorted_sequences.pop(0)

        while sorted_sequences and sorted_sequences[0][1] == max_len:
            max_sequences.append(sorted_sequences[0])
            sorted_sequences.pop(0)

        # Sort the sequences within the same count by length and binary value
        sorted_numbers = sorted(max_sequences, key=lambda x: (len(x[0]), int(x[0], 2)))

        # Write the result to the output file
        fout.write(str(max_len) + '\n')
        for i, (subseq, _) in enumerate(sorted_numbers):
            if i % 6 == 0 and i != 0:
                fout.write('\n')
            if i % 6 != 0:
                fout.write(' ')
            fout.write(subseq)
        fout.write('\n')
