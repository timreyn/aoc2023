import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

grid = []

def is_valid(pt, grid):
  return pt[0] >= 0 and pt[1] >= 0 and pt[0] < len(grid) and pt[1] < len(grid[0]) and grid[pt[0]][pt[1]] != '#'

def p(a, b):
  return (a[0] + b[0], a[1] + b[1])

for line in open(fname):
  line = line.strip()
  grid += [line]

start_pt = (0, grid[0].index('.'))
cache = {}

cached_walks = {}

def all_neighbors(pt, grid):
  nbrs = []
  for d in [(1,0),(-1,0),(0,1),(0,-1)]:
    if is_valid(p(pt, d), grid):
      nbrs += [p(d, pt)]
  return nbrs


neighbors = collections.defaultdict(list)
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if not is_valid((i,j), grid):
      continue
    nbrs = all_neighbors((i,j), grid)
    if len(nbrs) != 2:
      for pt in nbrs:
        start = (i, j)
        last = start
        dist = 1
        pt_neighbors = all_neighbors(pt, grid)
        while len(pt_neighbors) == 2:
          new_pt = pt_neighbors[0] if pt_neighbors[0] != last else pt_neighbors[1]
          last = pt
          pt = new_pt
          pt_neighbors = all_neighbors(pt, grid)
          dist += 1
        neighbors[start] += [(pt, dist)]

print(neighbors)

def max_distance(pt, neighbors, visited):
  distance = 0
  best = None
  if pt[0] == len(grid) - 1:
    return 0
  for n in neighbors[pt]:
    if n[0] in visited:
      continue
    val = max_distance(n[0], neighbors, visited + [n[0]])
    if val is None:
      continue
    val += n[1]
    if best is None or val > best:
      best = val
  return best

print(max_distance(start_pt, neighbors, [start_pt]))
