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

i_vals = []
j_vals = []

for line in open(fname):
  line = line.strip().split(' ')
  d = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[line[2][-2]]
  ct = int(line[2][2:-2], 16)
  old = active
  active = p(active, t(ct, dirs[d]))
  if active[0] not in i_vals:
    i_vals += [active[0]]
  if active[1] not in j_vals:
    j_vals += [active[1]]

i_vals += [(i + 1) for i in i_vals]
j_vals += [(j + 1) for j in j_vals]

i_vals.sort()
j_vals.sort()

edges = set()

for line in open(fname):
  line = line.strip().split(' ')
  d = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[line[2][-2]]
  ct = int(line[2][2:-2], 16)
  old = active
  active = p(active, t(ct, dirs[d]))
  ii = i_vals.index(old[0])
  jj = j_vals.index(old[1])
  while i_vals[ii] != active[0] or j_vals[jj] != active[1]:
    (ii, jj) = p(dirs[d], (ii, jj))
    edges.add((ii, jj))

inside = set()
outside = set()
min_i = 0
min_j = 0
max_i = len(i_vals) - 1
max_j = len(j_vals) - 1

for i in range(len(i_vals)):
  for j in range(len(j_vals)):
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

inside.update(edges)
for x in inside:
  out += (i_vals[x[0] + 1] - i_vals[x[0]]) * ((j_vals[x[1] + 1] - j_vals[x[1]]))
print(out)
