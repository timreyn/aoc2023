import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

for line in open(fname):
  line = [int(x) for x in line.strip().split(' ')]
  delta_stack = [line[0]]
  deltas = [x for x in line]
  while True:
    deltas = [deltas[i + 1] - deltas[i] for i in range(len(deltas) - 1)]
    delta_stack += [deltas[0]]
    if len(set(deltas)) == 1:
      break
  vals = []
  active = 0
  delta_stack.reverse()
  for d in delta_stack:
    active = d - active
  out += active


print(out)
