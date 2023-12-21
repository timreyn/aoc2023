import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
steps = 64 if len(sys.argv) < 3 else int(sys.argv[2])

out = 0

grid = []

starting = None

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

def valid(pt, grid):
  return pt[0] >= 0 and pt[1] >= 0 and pt[0] < len(grid) and pt[1] < len(grid[0])

def add(a, b):
  return (a[0] + b[0], a[1] + b[1])

for line in open(fname):
  line = line.strip()
  if 'S' in line:
    starting = (len(grid), line.index('S'))
    line = line.replace('S', '.')
  grid += [line]

possible = [starting]

for i in range(steps):
  nxt = set()
  for p in possible:
    for d in dirs:
      pp = add(p, d)
      if valid(pp, grid) and grid[pp[0]][pp[1]] == '.':
        nxt.add(pp)
  possible = list(nxt)

for i in range(len(grid)):
  out = ''
  for j in range(len(grid[0])):
    if (i, j) in possible:
      out += 'O'
    else:
      out += grid[i][j]
  print(out)


print(len(possible))
