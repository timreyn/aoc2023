import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

dirs = None
lines = {}

for line in open(fname):
  line = line.strip()
  if not dirs:
    dirs = line
    continue
  if not line:
    continue
  line = line.split('=')
  start = line[0].strip()
  targets = [x.strip() for x in line[1].strip()[1:-1].split(',')]
  lines[start] = targets

vals = [x for x in lines.keys() if x.endswith('A')]
step = 0

successes = [list() for v in vals]

while True:
  if dirs[step % len(dirs)] == 'L':
    i = 0
  else:
    i = 1
  step += 1
  vals = [lines[v][i] for v in vals]
  for i, v in enumerate(vals):
    if v.endswith('Z'):
      successes[i] += [step]
  if False in [len(s) > 2 for s in successes]:
    continue
  break

print(successes)

# Observe that all of these are cyclic -- each set is [k, 2k, 3k, ...]

import math

print(math.lcm(*[s[0] for s in successes]))
