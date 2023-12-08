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

val = 'AAA'
step = 0

while val != 'ZZZ':
  if dirs[step % len(dirs)] == 'L':
    val = lines[val][0]
  else:
    val = lines[val][1]
  step += 1

print(step)
