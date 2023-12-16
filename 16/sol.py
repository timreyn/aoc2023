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

visited = set()
visited_pairs = []

for line in open(fname):
  line = line.strip()
  grid += [list(line)]

# Because there's a mirror top left.
queue = [((0, 0), SOUTH)]

while queue:
  n = queue.pop(0)
  if n in visited_pairs:
    continue
  visited_pairs += [n]
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

print(len(visited))

for v in visited:
  if not isvalid(v, grid):
    print('xxx')
    print(v)

for i in range(len(grid)):
  out = ''
  for j in range(len(grid[i])):
    if (i, j) in visited:
      out += '#'
    else:
      out += '.'
  print(out)
