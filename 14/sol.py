import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

grid = []

for line in open(fname):
  line = line.strip()
  grid += [list(line)]

for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] == 'O':
      ii = i
      while ii >= 1 and grid[ii - 1][j] == '.':
        ii -= 1
      grid[i][j] = '.'
      grid[ii][j] = 'O'
      out += len(grid) - ii

for row in grid:
  print(''.join(row))

print(out)
