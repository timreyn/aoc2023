import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

def p(a, b):
  return (a[0] + b[0], a[1] + b[1])

def t(a, b):
  return (a * b[0], a * b[1])

def is_valid(a, min_i, min_j, max_i, max_j):
  return a[0] >= min_i and a[1] >= min_j and a[0] <= max_i and a[1] <= max_j

dirs = {
  'U': (-1, 0),
  'R': (0, 1),
  'D': (1, 0),
  'L': (0, -1)
}

def neighbors(a, min_i, min_j, max_i, max_j):
  for d in dirs:
    x = p(dirs[d], a)
    if is_valid(x, min_i, min_j, max_i, max_j):
      yield x

active = (0, 0)
edges = set()
edges.add(active)

min_i = 0
min_j = 0
max_i = 0
max_j = 0

for line in open(fname):
  line = line.strip().split(' ')
  d = line[0]
  ct = int(line[1])
  for i in range(ct):
    active = p(active, dirs[d])
    edges.add(active)
    max_i = max(max_i, active[0])
    max_j = max(max_j, active[1])
    min_i = min(min_i, active[0])
    min_j = min(min_j, active[1])

inside = set()
outside = set()

for i in range(min_i, max_i + 1):
  for j in range(min_j, max_j + 1):
    if (i, j) in inside or (i, j) in outside or (i, j) in edges:
      continue
    queue = [(i, j)]
    searched = set()
    found_edge = False
    while queue:
      n = queue.pop()
      if n in searched:
        continue
      searched.add(n)
      if n[0] == min_i or n[1] == min_j or n[0] == max_i or n[1] == max_j:
        found_edge = True
      for nn in neighbors(n, min_i, min_j, max_i, max_j):
        if nn not in searched and nn not in edges:
          queue += [nn]
    for pt in searched:
      if found_edge:
        outside.add(pt)
      else:
        inside.add(pt)
print(len(inside))
print(len(edges))
print(len(inside) + len(edges))

for i in range(max_i + 1):
  pr = ''
  for j in range(max_j + 1):
    if (i, j) in inside:
      pr += 'X'
    elif (i, j) in edges:
      pr += '*'
    else:
      pr += '.'
  print(pr)
