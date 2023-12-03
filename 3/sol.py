import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

grid = []

for line in open(fname):
  line = line.strip()
  grid += [line + '.']

out = 0

for i, row in enumerate(grid):
  active = 0
  works = False
  for j, ch in enumerate(row):
    if not ch.isdigit():
      if works and active > 0:
        out += active
        print('part ' + str(active))
      elif active > 0:
        print('not part ' + str(active))
      works = False
      active = 0
      continue
    n = int(ch)
    active = active * 10 + n
    for di in (-1, 0, 1):
      for dj in (-1, 0, 1):
        ii = i + di
        jj = j + dj
        if ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[ii]):
          if not grid[ii][jj].isdigit() and grid[ii][jj] != '.':
            works = True
print(out)
