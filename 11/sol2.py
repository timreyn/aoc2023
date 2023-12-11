import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

factor = int(sys.argv[2]) if len(sys.argv) >= 3 else 1000000

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
    dist = 0
    for gg in range(min(g1[0], g2[0]), max(g1[0], g2[0])):
      if gg in big_rows:
        dist += factor
      else:
        dist += 1
    for gg in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
      if gg in big_cols:
        dist += factor
      else:
        dist += 1
    out += dist

print(out)
