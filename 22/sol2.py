import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

def overlaps(b1, b2):
  for bb in b1:
    if bb in b2:
      return True
  return False

def dropped(brick):
  return set([(x, y, z-1) for x, y, z in brick])

def can_drop(brick, all_bricks):
  dped = dropped(brick)
  for p in dped:
    if p[2] < 1:
      return False
  for bb in all_bricks:
    if brick == bb:
      continue
    if overlaps(dped, bb):
      return False
  return True


bricks = []

for line in open(fname):
  line = line.strip()
  ee1, ee2 = line.split('~')
  e1 = [int(x) for x in ee1.split(',')]
  e2 = [int(x) for x in ee2.split(',')]
  pts = []
  for x in range(min(e1[0], e2[0]), max(e1[0], e2[0] + 1)):
    for y in range(min(e1[1], e2[1]), max(e1[1], e2[1] + 1)):
      for z in range(min(e1[2], e2[2]), max(e1[2], e2[2] + 1)):
        pts += [(x, y, z)]
  bricks += [set(pts)]

bricks.sort(key=lambda b: min(bb[2] for bb in b))

movements = 1
while movements > 0:
  movements = 0
  for i in range(len(bricks)):
    if can_drop(bricks[i], bricks):
      bricks[i] = dropped(bricks[i])
      movements += 1

sole_supporters = set()
for i, b1 in enumerate(bricks):
  supporters = []
  for j, b2 in enumerate(bricks):
    if i != j and overlaps(dropped(b1), b2):
      supporters += [j]
    if len(supporters) > 1:
      break
  if len(supporters) == 1:
    sole_supporters.add(supporters[0])

for i in sole_supporters:
  bricks2 = bricks[0:i] + bricks[i+1:]
  moving = set()
  movements = 1
  while movements > 0:
    movements = 0
    for j in range(len(bricks2)):
      if can_drop(bricks2[j], bricks2):
        bricks2[j] = dropped(bricks2[j])
        moving.add(j)
        movements += 1
  print(len(moving))
  out += len(moving)

print(out)
