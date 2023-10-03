"""
ID: shikha11
LANG: PYTHON3
TASK: cowtour
"""

fin = open('cowtour.in', 'r')
fout = open('cowtour.out', 'w')

n = int(fin.readline().strip())
x = []
y = []

for _ in range(n):
    a, b = map(int, fin.readline().strip().split())
    x.append(a)
    y.append(b)


def compute_distance(p11, p22):
    return ((x[p11] - x[p22]) ** 2 + (y[p11] - y[p22]) ** 2) ** 0.5


adjacency_matrix = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    line = fin.readline().strip()
    for j in range(n):
        if i == j:
            adjacency_matrix[i][j] = 0
        elif line[j] == '1':
            adjacency_matrix[i][j] = compute_distance(i, j)

# for each node, do a dfs to find the component it belongs to
c = 0
component = [-2] * n


def dfs(pasture, comp):
    if component[pasture] != -2:
        return

    component[pasture] = comp
    for neighbor in range(n):
        if component[neighbor] == -2 and adjacency_matrix[pasture][neighbor] != float('inf'):
            dfs(neighbor, comp)


for node in range(n):
    if component[node] == -2:
        dfs(node, c)
        c += 1

# Calculate the shortest paths for nodes in the same component using Floyd-Warshall
for intermediate in range(n):
    comp_intermediate = component[intermediate]
    for source in range(n):
        if component[source] != comp_intermediate:
            continue
        for destination in range(source + 1, n):
            if component[destination] != comp_intermediate:
                continue
            adjacency_matrix[source][destination] = min(
                adjacency_matrix[source][intermediate] + adjacency_matrix[intermediate][
                    destination], adjacency_matrix[source][destination])
            adjacency_matrix[destination][source] = adjacency_matrix[source][destination]

# Compute the diameter of each component and the furthest connected point from every point
diameter = [0] * c
furthest_in_component = [0] * n
for p1 in range(n):
    comp_p1 = component[p1]
    for p2 in range(p1 + 1, n):
        if component[p2] == comp_p1:
            dist_p1_p2 = adjacency_matrix[p1][p2]
            diameter[comp_p1] = max(dist_p1_p2, diameter[comp_p1])
            furthest_in_component[p1] = max(furthest_in_component[p1], dist_p1_p2)
            furthest_in_component[p2] = max(furthest_in_component[p2], dist_p1_p2)

# Go over all pairs of points, and if two are not from the same component, compute the diameter after joining them
new_diameter = float('inf')
for p1 in range(n):
    for p2 in range(p1 + 1, n):
        comp_p1 = component[p1]
        comp_p2 = component[p2]
        if comp_p1 != comp_p2:
            intermediate_diameter = compute_distance(p1, p2)
            joined_diameter = max(diameter[comp_p1], diameter[comp_p2],
                                  intermediate_diameter + furthest_in_component[p1] + furthest_in_component[p2])
            new_diameter = min(new_diameter, joined_diameter)

formatted_number = '{:.6f}'.format(new_diameter)
fout.write(str(formatted_number) + '\n')
fout.close()
