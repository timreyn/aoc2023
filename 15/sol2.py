import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

vals = [list() for i in range(256)]

def h(s):
  out = 0
  for c in s:
    out += ord(c)
    out *= 17
    out = out % 256
  return out

for line in open(fname):
  line = line.strip()
  for seg in line.split(','):
    if '-' in seg:
      label = seg[0:seg.index('-')]
      box = h(label)
      vals[box] = [x for x in vals[box] if x[0] != label]
    else:
      label = seg[0:seg.index('=')]
      box = h(label)
      focal_length = int(seg[seg.index('=') + 1:])
      if label in [x[0] for x in vals[box]]:
        vals[box] = [(label, focal_length) if x[0] == label else x for x in vals[box]]
      else:
        vals[box] += [(label, focal_length)]
    #print(seg)
    #print('Box %d: %s' % (box, vals[box]))
for i, box in enumerate(vals):
  for j, lens in enumerate(box):
    out += (i + 1) * (j + 1) * lens[1]

print(out)
