"""
ID: shikha11
LANG: PYTHON3
TASK: ttwo
"""

fin = open('ttwo.in', 'r')
fout = open('ttwo.out', 'w')


class Position:

    def __init__(self, row, column, direction):
        self.row = row
        self.column = column
        self.direction = direction

    def __eq__(self, other):
        return self.column == other.column and self.row == other.row

    def move(self):
        next_dir = self.direction
        row = self.row
        col = self.column

        if self.direction == 'N':
            row = self.row - 1
            next_dir = 'E'
        elif self.direction == 'E':
            col = self.column + 1
            next_dir = 'S'
        elif self.direction == 'S':
            row = self.row + 1
            next_dir = 'W'
        elif self.direction == 'W':
            col = self.column - 1
            next_dir = 'N'

        if 0 <= row < 10 and 0 <= col < 10 and grid[row][col] != '*':
            self.row = row
            self.column = col
        else:
            self.direction = next_dir


grid = []
for i in range(10):
    grid.append(list(fin.readline().strip()))
    for j in range(10):
        if grid[i][j] == 'F':
            farmer = Position(i, j, 'N')
        elif grid[i][j] == 'C':
            cows = Position(i, j, 'N')

count = 0
while not cows.__eq__(farmer) and count < 160000:
    cows.move()
    farmer.move()
    count += 1

if not cows.__eq__(farmer):
    count = 0

fout.write(str(count) + '\n')