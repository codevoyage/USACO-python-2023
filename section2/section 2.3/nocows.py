"""
ID: shikha11
LANG: PYTHON3
TASK: nocows
"""

fin = open('nocows.in', 'r')
fout = open('nocows.out', 'w')

n, k = map(int, fin.readline().strip().split())

max_nodes_for_height = pow(2, k) - 1

# number of trees with height h and total nodes n
exact_height = [[0] * (n + 1) for _ in range(k + 1)]

# number of trees with height atmost h and total nodes n
atmost_height = [[0] * (n + 1) for _ in range(k + 1)]

exact_height[1][1] = 1
atmost_height[1][1] = 1

for height in range(2, k + 1):
    min_nodes_for_height = 2 * height - 1
    max_nodes_for_height = pow(2, height) - 1

    for total_nodes in range(1, max_nodes_for_height + 1, 2):
        if total_nodes > n:
            break

        atmost_height[height][total_nodes] = atmost_height[height - 1][total_nodes]

        if total_nodes < min_nodes_for_height:
            continue

        # max nodes in tree of height h-1
        max_child_nodes = pow(2, height - 1) - 1
        total_configs = 0

        for left_nodes in range(1, max_child_nodes + 1, 2):
            right_nodes = total_nodes - left_nodes - 1

            if right_nodes < 1:
                # right child tree should have atleast 1 node
                break

            if right_nodes > max_child_nodes:
                # right child tree is full and a tree is not possible
                continue

            # add the number of trees with left child having height h-1 and right child having height atmost h-2
            total_configs += exact_height[height - 1][left_nodes] * atmost_height[height-2][right_nodes]

            # add the number of trees with right child having height h-1 and left child having height atmost h-2
            total_configs += exact_height[height - 1][right_nodes] * atmost_height[height-2][left_nodes]

            # add the number of trees with both children having height h-1
            total_configs += exact_height[height - 1][left_nodes] * exact_height[height - 1][right_nodes]

        exact_height[height][total_nodes] = total_configs
        atmost_height[height][total_nodes] += total_configs

fout.write(f'{exact_height[k][n] % 9901}\n')
