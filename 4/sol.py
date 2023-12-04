import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

for line in open(fname):
  line = line.strip()
  line = line.split(':')[1]
  want = [int(x.strip()) for x in line.split('|')[0].split(' ') if x.strip()]
  have = [int(x.strip()) for x in line.split('|')[1].split(' ') if x.strip()]
  n = len([x for x in want if x in have])
  if n:
    out += 2 ** (n - 1)


print(out)
