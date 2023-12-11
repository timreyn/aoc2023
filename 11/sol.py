import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

grid = []

big_rows = []
big_cols = []

for line in open(fname):
  line = line.strip()
  grid += [list(line)]

for i in range(len(grid)):
  if '#' not in grid[i]:
    big_rows += [i]

for j in range(len(grid[0])):
  if '#' not in [grid[i][j] for i in range(len(grid))]:
    big_cols += [j]

big_rows.reverse()
big_cols.reverse()

for r in big_rows:
  grid.insert(r, ['.' for i in range(len(grid[0]))])

for c in big_cols:
  for r in grid:
    r.insert(c, '.')

galaxies = []

for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] == '#':
      galaxies += [(i,j)]

for x in range(len(galaxies)):
  g1 = galaxies[x]
  for y in range(len(galaxies)):
    if y <= x:
      continue
    g2 = galaxies[y]
    out += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

print(out)
