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

def minus(a, b):
  return (a[0] - b[0], a[1] - b[1])

def get(grid, pos):
  return grid[int(pos[0])][int(pos[1])]

def half(d):
  return (d[0] / 2, d[1] / 2)

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

pipes['S'] = (minus(positions[1], positions[0]), minus(positions[-2], positions[0]))

visited = set()
inside = set()

to_show = []

for i in range(len(grid)):
  i = i * 1.0
  for j in range(len(grid[int(i)])):
    j = j * 1.0
    if (int(i), int(j)) in positions or (i, j) in visited:
      continue
    region = []
    queue = [(i, j)]
    valid = True
    verbose = False
    while queue:
      ii, jj = queue[0]
      queue = queue[1:]
      if (ii, jj) in region:
        continue
      # This region hits the wall
      if (ii < 0.0 or jj < 0.0 or ii >= len(grid) or jj >= len(grid[0])):
        valid = False
        break
      # This is part of the pipe
      if ii == int(ii) and jj == int(jj) and (int(ii), int(jj)) in positions:
        continue
      # This is hitting a horizontal wall
      if ii == int(ii) and jj != int(jj):
        left = (ii, jj - 0.5)
        right = (ii, jj + 0.5)
        if left in positions and right in positions:
          if EAST in pipes[get(grid, left)] and WEST in pipes[get(grid, right)]:
            continue
      # This is hitting a vertical wall
      if ii != int(ii) and jj == int(jj):
        up = (ii - 0.5, jj)
        down = (ii + 0.5, jj)
        if up in positions and down in positions:
          if SOUTH in pipes[get(grid, up)] and NORTH in pipes[get(grid, down)]:
            continue
      region += [(ii, jj)]
      for d in (NORTH, SOUTH, EAST, WEST):
        queue += [plus((ii, jj), half(d))]
    if valid:
      # Figure out if it's inside or outside
      for ii, jj in region:
        if ii == int(ii) and jj == int(jj):
          inside.add((ii, jj))
    for r in region:
      visited.add(r)

for i in range(len(grid)):
  p = ''
  for j in range(len(grid[i])):
    if (i, j) in inside:
      p += 'I'
    else:
      p += '.'
  #print(p)

print(len(inside))
