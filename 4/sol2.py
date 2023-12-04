import sys
import collections

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

row = 0
counts = collections.defaultdict(lambda: 1)

for line in open(fname):
  row += 1
  line = line.strip()
  line = line.split(':')[1]
  want = [int(x.strip()) for x in line.split('|')[0].split(' ') if x.strip()]
  have = [int(x.strip()) for x in line.split('|')[1].split(' ') if x.strip()]
  n = len([x for x in want if x in have])
  if n:
    for i in range(n):
      counts[row + i + 1] += counts[row]
  out += counts[row]


print(out)
