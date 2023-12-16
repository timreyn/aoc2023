import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

def p(a, b):
  return (a[0] + b[0], a[1] + b[1])

def isvalid(a, grid):
  return a[0] >= 0 and a[1] >= 0 and a[0] < len(grid) and a[1] < len(grid[0])

EAST = (0, 1)
WEST = (0, -1)
NORTH = (-1, 0)
SOUTH = (1, 0)

mirrors = {
  '/': {
    EAST: NORTH, NORTH: EAST,
    WEST: SOUTH, SOUTH: WEST,
  },
  '\\': {
    EAST: SOUTH, SOUTH: EAST,
    WEST: NORTH, NORTH: WEST,
  }
}

grid = []

for line in open(fname):
  line = line.strip()
  grid += [list(line)]

mx = 0

for d in (NORTH, SOUTH, EAST, WEST):
  for x in range(len(grid)):
    visited = set()
    visited_pairs = set()

    if d == NORTH:
      queue = [((-1, x), SOUTH)]
    elif d == SOUTH:
      queue = [((len(grid), x), NORTH)]
    elif d == WEST:
      queue = [((x, -1), EAST)]
    elif d == EAST:
      queue = [((x, len(grid[0])), WEST)]

    while queue:
      n = queue.pop(0)
      if n in visited_pairs:
        continue
      visited_pairs.add(n)
      if isvalid(n[0], grid):
        visited.add(n[0])
      nxt = p(n[0], n[1])
      if not isvalid(nxt, grid):
        continue
      val = grid[nxt[0]][nxt[1]]
      if val == '.':
        queue += [(nxt, n[1])]
      elif val == '\\' or val == '/':
        queue += [(nxt, mirrors[val][n[1]])]
      elif val == '-':
        if val in (EAST, WEST):
          queue += [(nxt, val)]
        else:
          queue += [(nxt, EAST), (nxt, WEST)]
      elif val == '|':
        if val in (NORTH, SOUTH):
          queue += [(nxt, val)]
        else:
          queue += [(nxt, NORTH), (nxt, SOUTH)]

    if len(visited) > mx:
      print(len(visited))
      mx = len(visited)
