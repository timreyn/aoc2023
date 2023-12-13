import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

active_grid = []

def process_grid(grid):
  ret = 0
  for i in range(1, len(grid)):
    works = True
    for ii in range(len(grid)):
      i_prime = (2 * i - 1) - ii
      if i_prime < 0 or i_prime >= len(grid) or i_prime < ii:
        continue
      for jj in range(len(grid[0])):
        if grid[ii][jj] != grid[i_prime][jj]:
          works = False
    if works:
      ret +=  i * 100
  for j in range(1, len(grid[0])):
    works = True
    for jj in range(len(grid[0])):
      j_prime = (2 * j - 1) - jj
      if j_prime < 0 or j_prime >= len(grid[0]) or j_prime < jj:
        continue
      for ii in range(len(grid)):
        if grid[ii][jj] != grid[ii][j_prime]:
          works = False
    if works:
      ret += j
  print(ret)
  return ret

for line in open(fname):
  line = line.strip()
  if line:
    active_grid += [line]
  else:
    out += process_grid(active_grid)
    active_grid = []

out += process_grid(active_grid)


print(out)
