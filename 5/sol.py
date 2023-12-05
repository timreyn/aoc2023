import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

vals = []
newvals = []

for line in open(fname):
  line = line.strip()
  if 'seeds' in line:
    vals = [int(x) for x in line.split(':')[1].strip().split(' ')]
  elif 'map' in line:
    vals = vals + newvals
    newvals = []
  elif not line:
    continue
  else:
    dest_start, source_start, length = [int(x) for x in line.split(' ')]
    used = []
    for val in vals:
      if val >= source_start and val < source_start + length:
        used += [val]
        newvals += [val - source_start + dest_start]
    vals = [val for val in vals if val not in used]

print(min(newvals + vals))
