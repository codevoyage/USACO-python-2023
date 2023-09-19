"""
ID: shikha11
LANG: PYTHON3
TASK: concom
"""

# Open input and output files
fin = open('concom.in', 'r')
fout = open('concom.out', 'w')

# number of companies
n = int(fin.readline().strip())

# matrices for percentage ownership and control
percent = [[0] * 101 for _ in range(101)]
control = [[0] * 101 for _ in range(101)]

# Read ownership data and populate the 'percent' matrix
for _ in range(n):
    i, j, p = map(int, fin.readline().strip().split())
    percent[i][j] = p


# Function to update control relationships recursively
def update_control(owner, new_company):
    if control[owner][new_company] == 1:
        # This update has already happened, return
        return

    control[owner][new_company] = 1

    # Add all shares of the new company to the owning company
    for company in range(1, 101):
        if company == owner or company == new_company:
            continue
        percent[owner][company] += percent[new_company][company]

        # If a new company is found as a result of new shares, update control
        if percent[owner][company] > 50:
            update_control(owner, company)

    # Update the owners of the owning company about the new company
    for company in range(1, 101):
        if company == owner or company == new_company:
            continue
        if control[company][owner] == 1:
            update_control(company, new_company)


# Iterate through all pairs of companies
for c1 in range(1, 101):
    for c2 in range(1, 101):
        if c1 == c2:
            continue

        # If percentage ownership is greater than 50, add c1 as controller to c2
        if percent[c1][c2] > 50:
            update_control(c1, c2)
            continue

        # Otherwise, check if the total combined ownership of c2 by companies owning c1 is greater than 50
        pc = 0
        for c3 in range(1, 101):
            if percent[c1][c3] > 50:
                pc += percent[c3][c2]

        if pc > 50:
            percent[c1][c2] = pc
            update_control(c1, c2)


# Write the results to the output file
for c1 in range(1, 101):
    for c2 in range(1, 101):
        if control[c1][c2] == 1 and c1 != c2:
            fout.write('{} {}\n'.format(c1, c2))

fin.close()
fout.close()
