import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

def p(a, b):
  return (a[0] + b[0], a[1] + b[1])

def m(a, b):
  return (a[0] - b[0], a[1] - b[1])

def neg(a):
  return (-1 * a[0], -1 * a[1])

out = 0

bests = {}

grid = []

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

for line in open(fname):
  line = line.strip()
  grid += [[int(x) for x in line]]

changes = 1
best_overall = None
while changes > 0:
  changes = 0
  for i in range(len(grid) - 1, -1, -1):
    for j in range(len(grid[0]) - 1, -1, -1):
      for last_dir in (NORTH, SOUTH, EAST, WEST):
        for ct in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
          if ct == 0 and (i > 0 or j > 0):
            continue
          key = ((i, j), last_dir, ct)
          #print('key: ' + str(key))
          if i == len(grid) - 1 and j == len(grid[0]) - 1 and ct > 3:
            bests[key] = grid[i][j]
          else:
            best_option = None
            best_option_val = None
            for next_dir in (NORTH, SOUTH, EAST, WEST):
              if next_dir == neg(last_dir):
                continue
              next_ct = ct + 1 if last_dir == next_dir else 1
              if next_dir != last_dir and ct <= 3:
                continue
              next_square = p((i, j), next_dir)
              if (next_square, next_dir, next_ct) not in bests:
                continue
              val = bests[(next_square, next_dir, next_ct)]
              #print(best_option_val)
              if best_option_val is None or val < best_option_val:
                best_option = next_dir
                best_option_val = val
            if best_option is not None:
              new_val = grid[i][j] + best_option_val
              if key not in bests or new_val < bests[key]:
                bests[key] = grid[i][j] + best_option_val
                changes += 1
              if i == 0 and j == 0 and (best_overall is None or best_option_val < best_overall) and ct == 0:
                best_overall = best_option_val
  print(changes)

print(best_overall)
