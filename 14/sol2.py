import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
steps = 1000000000 if len(sys.argv) < 3 else int(sys.argv[2])

out = 0
vals = []

grid = []
saved_grids = []

rotations = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for line in open(fname):
  line = line.strip()
  grid += [list(line)]

next_x = -1

for x in range(steps):
  if next_x > 0:
    x = next_x
    next_x += 1
  for d in rotations:
    out = 0
    for i in range(len(grid)):
      if d[0] == 1:
        i = len(grid) - i - 1
      for j in range(len(grid[i])):
        if d[1] == 1:
          j = len(grid[0]) - j - 1
        if grid[i][j] == 'O':
          ii = i
          jj = j
          n_ii = ii + d[0]
          n_jj = jj + d[1]
          while n_ii >= 0 and n_ii < len(grid) and n_jj >= 0 and n_jj < len(grid[0]) and grid[n_ii][n_jj] == '.':
            ii = n_ii
            jj = n_jj
            n_ii = ii + d[0]
            n_jj = jj + d[1]
          grid[i][j] = '.'
          grid[ii][jj] = 'O'
          out += len(grid) - ii
  print(out)
  vals += [out]
  s = str(grid)
  if s in saved_grids and next_x == -1:
    v = saved_grids.index(s)
    print(x, v)
    next_x = steps - 1
    while next_x % (x - v) != v % (x - v):
      next_x -= 1
    print('skipping to %d' % (next_x + 1))
    next_x += 1
    continue
  if x == steps:
    break
  saved_grids += [str(grid)]

  #for row in grid:
  #  print(''.join(row))
  #print()
