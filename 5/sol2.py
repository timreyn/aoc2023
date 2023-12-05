import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

# Ranges are closed.
ranges = []
newranges = []

for line in open(fname):
  line = line.strip()
  if 'seeds' in line:
    vals = [int(x) for x in line.split(':')[1].strip().split(' ')]
    ranges = [(vals[2*i], vals[2*i] + vals[2*i + 1] - 1) for i in range(len(vals) // 2)]
  elif 'map' in line:
    ranges = ranges + newranges
    newranges = []
  elif not line:
    continue
  else:
    dest_start, source_start, length = [int(x) for x in line.split(' ')]
    source_end = source_start + length - 1
    used = []
    range_idx = 0
    while range_idx < len(ranges):
      rg = ranges[range_idx]
      range_idx += 1
      start = rg[0]
      end = rg[1]
      if start <= source_end and source_start <= end:
        if source_start > start:
          before = (start, source_start - 1)
          ranges += [before]
        if source_end < end:
          after = (source_end + 1, end)
          ranges += [after]
        overlapping = (max(start, source_start), min(end, source_end))
        new_overlapping = tuple(x - source_start + dest_start for x in overlapping)
        newranges += [new_overlapping]
        used += [rg]
    ranges = [range for range in ranges if range not in used]

print(min([r[0] for r in newranges + ranges]))
