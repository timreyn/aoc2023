import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

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
    out += h(seg)


print(out)
