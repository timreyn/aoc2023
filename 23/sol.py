import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

grid = []

dirs = {
  '>': (0, 1),
  '<': (0, -1),
  'v': (1, 0),
  '^': (-1, 0)
}

def neg(pt):
  return (-1 * pt[0], -1 * pt[1])

def is_valid(pt, grid):
  return pt[0] >= 0 and pt[1] >= 0 and pt[0] < len(grid) and pt[1] < len(grid[0]) and grid[pt[0]][pt[1]] != '#'

def p(a, b):
  return (a[0] + b[0], a[1] + b[1])

for line in open(fname):
  line = line.strip()
  grid += [line]

start = (0, grid[0].index('.'))
cache = {}

def max_distance(pt, grid, last_dir):
  global cache
  if (pt, last_dir) in cache:
    return cache[(pt, last_dir)]
  out = max_distance_impl(pt, grid, last_dir)
  cache[(pt, last_dir)] = out
  return out

def max_distance_impl(pt, grid, last_dir):
  global cache
  dist_travelled = 0
  while True:
    if (pt, last_dir) in cache:
      #print('%s: returning cached %s' % (str(pt), str(cache[(pt, last_dir)])))
      return cache[(pt, last_dir)] + dist_travelled
    if pt[0] == len(grid) - 1:
      return dist_travelled
    possible_nexts = []
    for arrow, d in dirs.items():
      if grid[pt[0]][pt[1]] != '.' and grid[pt[0]][pt[1]] != arrow:
        continue
      if d == neg(last_dir):
        continue
      nxt = p(pt, d)
      if not is_valid(nxt, grid):
        #print('%s: cant go to %s' % (str(pt), str(nxt)))
        continue
      possible_nexts += [d]
    #print('%s: possible %s' % (str(pt), str(possible_nexts)))
    if len(possible_nexts) == 0:
      return None
    elif len(possible_nexts) == 1:
      dist_travelled += 1
      pt = p(possible_nexts[0], pt)
      last_dir = possible_nexts[0]
    else:
      best = -1
      best_dir = None
      for d in possible_nexts:
        nxt = p(pt, d)
        new_dist = max_distance(nxt, grid, d)
        print('%s: forked recursion to %s: %d' % (str(pt), str(nxt), (new_dist if new_dist is not None else -1)))
        if new_dist is not None and new_dist > best:
          best = new_dist
          best_dir = d
      if best >= 0:
        print('%s: winner: %s %d' % (str(pt), str(best_dir), best + dist_travelled))
        #print('%s: recursion result %d' % (str(pt), best + dist_travelled))
        return best + dist_travelled + 1
      else:
        #print('%s: unsuccessful' % str(pt))
        return None

print(max_distance(start, grid, (0, 0)))
