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
    if ch != '*':
      continue
    used = set()
    vals = []
    for di in (-1, 0, 1):
      for dj in (-1, 0, 1):
        ii = i + di
        jj = j + dj
        if not (ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[ii])):
          continue
        if (ii, jj) in used:
          continue
        if not grid[ii][jj].isdigit():
          continue
        jjj = jj
        while jjj > 0 and grid[ii][jjj - 1].isdigit():
          jjj -= 1
        value = 0
        while jjj < len(grid[ii]) and grid[ii][jjj].isdigit():
          value = value * 10 + int(grid[ii][jjj])
          used.add((ii, jjj))
          jjj += 1
        vals += [value]
    if len(vals) == 2:
      out += vals[0] * vals[1]
print(out)
