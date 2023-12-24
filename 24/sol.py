import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
min_coord = 200000000000000 if len(sys.argv) < 3 else int(sys.argv[2])
max_coord = 400000000000000 if len(sys.argv) < 4 else int(sys.argv[3])

out = 0

stones = []

def intersect(stone_a, stone_b):
  vel_a = stone_a['vel']
  vel_b = stone_b['vel']
  pos_a = stone_a['pos']
  pos_b = stone_b['pos']
  slope_a = vel_a[1] / vel_a[0]
  slope_b = vel_b[1] / vel_b[0]
  if slope_a == slope_b:
    return None, None, None, None

  int_x = (pos_a[1] - pos_b[1] - slope_a * pos_a[0] + slope_b * pos_b[0] ) / (slope_b - slope_a)
  int_ta = (int_x - pos_a[0]) / vel_a[0]
  int_tb = (int_x - pos_b[0]) / vel_b[0]
  int_y = pos_a[1] + int_ta * vel_a[1]
  return (int_x, int_y, int_ta, int_tb)

for line in open(fname):
  line = line.strip()
  pos, vel = line.split(' @ ')
  stones += [
    {
      'pos': tuple(int(x.strip()) for x in pos.split(',')),
      'vel': tuple(int(x.strip()) for x in vel.split(','))
    }
  ]

for i, stone_a in enumerate(stones):
  for j, stone_b in enumerate(stones):
    if i <= j:
      continue
    print(stone_a)
    print(stone_b)
    int_x, int_y, int_ta, int_tb = intersect(stone_a, stone_b)
    print(int_x, int_y, int_ta, int_tb)
    if int_ta is None or int_x < min_coord or int_y < min_coord or int_x > max_coord or int_y > max_coord or int_ta <= 0 or int_tb <= 0:
      print('no intersection')
    else:
      out += 1
      print('cross at %.02f, %.02f' % (int_x, int_y))
    print()

print(out)
