import collections
import sys
import numpy as np

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
steps = 64 if len(sys.argv) < 3 else int(sys.argv[2])
# The first pass determines that [131 + k, 131 * 2 + k, 131 * 3 + k, ...] is a quadratic
period = 131 if len(sys.argv) < 4 else int(sys.argv[3])

out = 0

grid = []

starting = None

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

def add(a, b):
  return (a[0] + b[0], a[1] + b[1])

for line in open(fname):
  line = line.strip()
  if 'S' in line:
    starting = (len(grid), line.index('S'))
    line = line.replace('S', '.')
  grid += [line]

last = collections.defaultdict(int)
possible = set([starting])

max_delta = 0
max_delta_i = 0
frame = []
frame_x = []
last_delta = 0

for i in range(steps):
  i = i + 1
  nxt = set()
  for p in possible:
    for d in dirs:
      pp = add(p, d)
      if grid[pp[0] % len(grid)][pp[1] % len(grid[0])] == '.':
        nxt.add(pp)
  if i > 50 and i % period == steps % period:
    frame += [len(nxt)]
    frame_x += [i // period]
    print(i, len(nxt))
  '''
  # First time through: look for places where the second derivative is constant
  if i > 50:
    frame += [len(nxt)]
  for j in range(len(frame) // 4 - 100, len(frame) // 4):
    if j < 10:
      continue
    if (frame[-3 * j] - 2 * frame[-2 * j] + frame[-1 * j]) == (frame[-4 * j] - 2 * frame[-3 * j] + frame[-2 * j]):
      print('candidate: %d' % j)
  '''
  possible = list(nxt)
  if len(frame) >= 3:
    break

'''
now solve the linear equation
'''
a = np.array([
  [1, x, x ** 2] for x in frame_x
])
b = np.array(frame)
sol = np.linalg.solve(a, b)

sol = [int(x) for x in sol]
print(sol)
print(sol[0] + sol[1] * (steps // period) + sol[2] * (steps // period) ** 2)

'''
for i in range(len(grid)):
  out = ''
  for j in range(len(grid[0])):
    if (i, j) in possible:
      out += 'O'
    else:
      out += grid[i][j]
  print(out)
'''

'''
Output:
65 3837
196 33344
327 91909
458 179532

a * (x)

'''
