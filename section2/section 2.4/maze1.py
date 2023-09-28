"""
ID: shikha11
LANG: PYTHON3
TASK: maze1
"""

fin = open('maze1.in', 'r')
fout = open('maze1.out', 'w')

w, h = map(int, fin.readline().strip().split())
grid = [[''] * (2 * w + 1) for _ in range(2 * h + 1)]

for r in range(2 * h + 1):
    line = list(fin.readline())
    for c in range(2 * w + 1):
        if c > len(line) - 1:
            grid[r][c] = ' '
        else:
            grid[r][c] = line[c]

adjacency_list = {}
exits = []

# make an adjacency list
for i in range(1, 2 * h + 1, 2):
    for j in range(1, 2 * w + 1, 2):
        grid_r = int((i - 1) / 2)
        grid_c = int((j - 1) / 2)
        adjacency_list[(grid_r, grid_c)] = []
        if grid[i][j - 1] == ' ':
            if j - 1 == 0:
                # if there is an opening at the edges of the maze, the cell is an exit
                exits.append((grid_r, grid_c))
            else:
                adjacency_list[(grid_r, grid_c)].append((grid_r, grid_c - 1))
        if grid[i][j + 1] == ' ':
            if j + 1 == 2 * w:
                exits.append((grid_r, grid_c))
            else:
                adjacency_list[(grid_r, grid_c)].append((grid_r, grid_c + 1))
        if grid[i - 1][j] == ' ':
            if i - 1 == 0:
                exits.append((grid_r, grid_c))
            else:
                adjacency_list[(grid_r, grid_c)].append((grid_r - 1, grid_c))
        if grid[i + 1][j] == ' ':
            if i + 1 == 2 * h:
                exits.append((grid_r, grid_c))
            else:
                adjacency_list[(grid_r, grid_c)].append((grid_r + 1, grid_c))

distances = [[40000] * w for _ in range(h)]
cell_queue = []

for e in exits:
    cell_queue.append(e)
    distances[e[0]][e[1]] = 1
    visited = [[False] * w for _ in range(h)]

    while len(cell_queue) > 0:
        cell = cell_queue.pop(0)

        if visited[cell[0]][cell[1]]:
            continue
        visited[cell[0]][cell[1]] = True

        # add all neighbors to the queue
        for neighbour in adjacency_list[cell]:
            if not visited[neighbour[0]][neighbour[1]]:
                distances[neighbour[0]][neighbour[1]] = min(distances[neighbour[0]][neighbour[1]],
                                                            distances[cell[0]][cell[1]] + 1)
                cell_queue.append(neighbour)

max_dist = 0
for r in range(h):
    for c in range(w):
        if distances[r][c] > max_dist:
            max_dist = distances[r][c]

fout.write(str(max_dist) + '\n')
