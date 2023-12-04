import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

for line in open(fname):
  line = line.strip()


print(out)
