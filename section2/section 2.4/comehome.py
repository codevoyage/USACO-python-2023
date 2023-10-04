"""
ID: shikha11
LANG: PYTHON3
TASK: comehome
"""

fin = open('comehome.in', 'r')
fout = open('comehome.out', 'w')

n = int(fin.readline().strip())

# adjacency matrix
adjacency_matrix = [[float('inf')] * 52 for _ in range(52)]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
has_cow = [False] * 52
input_letters = set()

for _ in range(n):
    pasture1, pasture2, d = fin.readline().strip().split()
    p1 = alphabet.index(pasture1)
    p2 = alphabet.index(pasture2)
    if pasture1.isupper():
        has_cow[p1] = True
    if pasture2.isupper():
        has_cow[p2] = True

    d = int(d)
    adjacency_matrix[p1][p2] = min(adjacency_matrix[p1][p2], d)
    adjacency_matrix[p2][p1] = min(adjacency_matrix[p2][p1], d)

    input_letters.add(p1)
    input_letters.add(p2)

# perform Dijkstra algorithm to get single source shortest path from Z
total_pastures = len(input_letters)
distance = [float('inf')] * 52
visited_pastures = set()

source = alphabet.index('Z')
distance[source] = 0

while len(visited_pastures) < total_pastures:
    # find the min distance node that is not visited
    shortest_distance = float('inf')
    for p in input_letters:
        if p not in visited_pastures and distance[p] < shortest_distance:
            shortest_distance = distance[p]
            visiting_pasture = p

    visited_pastures.add(visiting_pasture)
    distance[visiting_pasture] = shortest_distance

    for neighbour in input_letters:
        # relax the edge distance of all neighbours of the visiting node
        if neighbour not in visited_pastures and adjacency_matrix[visiting_pasture][neighbour] != float('inf'):
            distance[neighbour] = min(distance[neighbour], distance[visiting_pasture] + adjacency_matrix[visiting_pasture][neighbour])


fastest_cow = float('inf')
for i in input_letters:
    if distance[i] < fastest_cow and has_cow[i] and i != source:
        fastest_cow = distance[i]
        cow_home = alphabet[i]

fout.write('{} {}\n'.format(cow_home, fastest_cow))
fout.close()