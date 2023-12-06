import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

times = []
bests = []

for line in open(fname):
  line = line.strip()
  key = line.split(':')[0]
  vals = [int(x.strip()) for x in line.split(':')[1].split(' ') if x.strip()]
  if key == 'Time':
    times = vals
  else:
    bests = vals

out = 1
print(times)
print(bests)

for time, best in zip(times, bests):
  ct = 0
  for i in range(time):
    dist = i * (time - i)
    if dist > best:
      ct += 1
  out *= ct
  print(ct)


print(out)
