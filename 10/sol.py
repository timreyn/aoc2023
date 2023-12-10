import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
grid = []

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

def plus(a, b):
  return (a[0] + b[0], a[1] + b[1])

def get(grid, pos):
  return grid[pos[0]][pos[1]]

pipes = {
  '|': (NORTH, SOUTH),
  '-': (EAST, WEST),
  'L': (NORTH, EAST),
  'J': (NORTH, WEST),
  '7': (SOUTH, WEST),
  'F': (SOUTH, EAST),
}

for line in open(fname):
  line = line.strip()
  grid += [line]

positions = []

for i, line in enumerate(grid):
  for j, c in enumerate(line):
    if c == 'S':
      positions += [(i, j)]

for d in [NORTH, SOUTH, EAST, WEST]:
  pos = plus(positions[0], d)
  val = get(grid, pos)
  if val not in pipes:
    continue
  next_positions = [plus(d, pos) for d in pipes[val]]
  if positions[0] in next_positions:
    positions += [pos]
    break

while positions[-1] != positions[0]:
  pos = positions[-1]
  val = get(grid, pos)
  next_positions = [plus(d, pos) for d in pipes[val]]
  positions += [next_positions[0] if next_positions[1] == positions[-2] else next_positions[1]]

print(len(positions) // 2)
