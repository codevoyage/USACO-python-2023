"""
ID: shikha11
LANG: PYTHON3
TASK: holstein
"""

fin = open('holstein.in', 'r')
fout = open('holstein.out', 'w')

V = int(fin.readline())
vitamin_requirements = list(map(int, fin.readline().split()))
G = int(fin.readline())
feeds = []
for i in range(G):
    feeds.append(list(map(int, fin.readline().split())))


def are_vitamins_satisfied(vitamin_provided):
    for vitamin in vitamin_provided:
        if vitamin > 0:
            return False
    return True


def find_solution_with_scoops(required_vitamins, solution_feed, start_feed, num_of_scoops):
    if num_of_scoops == 0:
        return

    for feed_type in range(start_feed, G):
        required_vitamins_copy = [0] * V
        for vit in range(V):
            if required_vitamins[vit] > 0:
                required_vitamins_copy[vit] = required_vitamins[vit] - feeds[feed_type][vit]

        solution_feed.append(feed_type)

        if are_vitamins_satisfied(required_vitamins_copy):
            return solution_feed

        sol = find_solution_with_scoops(required_vitamins_copy, solution_feed, feed_type + 1, num_of_scoops - 1)

        if sol:
            return sol

        solution_feed.pop()


solution = None
scoops = 0

while not solution:
    scoops += 1
    solution = find_solution_with_scoops(vitamin_requirements, list(), 0, scoops)

fout.write(f'{scoops} ')
for i in range(len(solution)):
    fout.write(f'{solution[i] + 1}')
    if i < len(solution) - 1:
        fout.write(' ')
fout.write('\n')
