"""
ID: shikha11
LANG: PYTHON3
TASK: agrinet
"""

fin = open('agrinet.in', 'r')
fout = open('agrinet.out', 'w')

n = int(fin.readline().strip())
adjacency_matrix = []

# read the input, store it in a matrix. If n is greater than 80, the input will be read from the next line
row = 0
column = 0
while True:
    line = list(map(int, fin.readline().strip().split()))
    if not line:
        break
    adjacency_matrix.append([float('inf')] * n)
    for number in range(len(line)):
        adjacency_matrix[row][column] = line[number]
        column += 1
    if column == n:
        row += 1
        column = 0

# Prim's algorithm: start with a tree containing a single vertex, and add the cheapest edge to the tree in each step
tree = set()

mst_weight = 0
tree.add(0)
while len(tree) < n:
    min_edge = float('inf')
    edge_end = None
    edge_source = None
    for source in tree:
        for end in range(n):
            if source == end:
                continue
            if end not in tree and adjacency_matrix[source][end] < min_edge:
                min_edge = adjacency_matrix[source][end]
                edge_end = end
                edge_source = source
    tree.add(edge_end)
    mst_weight += min_edge

fout.write(str(mst_weight) + '\n')
fout.close()
