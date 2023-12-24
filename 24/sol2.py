import collections
import sys
import math
import numpy as np

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

stones = []

for line in open(fname):
  line = line.strip()
  pos, vel = line.split(' @ ')
  stones += [
    {
      'pos': tuple(int(x.strip()) for x in pos.split(',')),
      'vel': tuple(int(x.strip()) for x in vel.split(','))
    }
  ]

'''
First compute which velocities are possible.

If you have:
stone: x_s, vx_s
starting: x, vx

if x > x_s then we must have vx < vx_s, otherwise they will not cross in the future.

This leads to:
-A small number of possible values for each vx, vy, vz that are in the range of the stones' velocities
-If x is larger than the x value of every stone, then vx is smaller than any stone's velocity
-If x is smaller than the x value of every stone, then vx is larger than any stone's velocity

"valids" captures the first case; "ranges" captures the second.
'''

valids = [[], [], []]
ranges = [[], [], []]

for i in range(3):
  print('dim %d' % i)
  std = sorted(stones, key=lambda s: s['pos'][i])
  min_possible = None
  max_possible = None
  for k in range(len(std) + 1):
    if k == 0:
      print('x < %d: vx > %d' % (std[0]['pos'][i], max([std[j]['vel'][i] for j in range(len(stones))])))
      ranges[i] += [max([std[j]['vel'][i] for j in range(len(stones))])]
    elif k == len(std):
      print('x > %d: vx < %d' % (std[-1]['pos'][i], min([std[j]['vel'][i] for j in range(len(stones))])))
      ranges[i] += [min([std[j]['vel'][i] for j in range(len(stones))])]
    else:
      min_below = min([std[j]['vel'][i] for j in range(k)])
      max_above = max([std[j]['vel'][i] for j in range(k, len(std))])
      if min_below > max_above + 1:
        print('%d < x < %d: %d < vx < %d' % (std[k]['pos'][i], std[k+1]['pos'][i], max_above, min_below))
        for x in range(max_above, min_below + 1):
          valids[i] += [x]
        if min_possible is None or max_above < min_possible:
          min_possible = max_above
        if max_possible is None or min_below > max_possible:
          max_possible = min_below

print(valids)
print(ranges)

offsets = collections.defaultdict(lambda x: [list() for i in range(len(stones))])

'''
Construct a 5x5 linear equation to compute when the first 5 coordinates (x0, y0, z0, x1, y1) are crossed.

x + vx * t = x0 + vx0 * t
=>
x + (vx - vx0) * t = x0

=>

1 0 0 vx-vx0 0   x   x1
0 1 0 vy-vy0 0   y = y1
0 0 1 vz-vz0 0 * z   z1
1 0 0 0 vx-vx1   t1  x2
0 1 0 0 vy-vy1   t2  y2

Then, if a solution is found (with positive t and integer values), check whether there is an intersection between the rock and each of the other stones. If any miss, return None.
'''


def check(vx, vy, vz, stones):
  v0 = stones[0]['vel']
  v1 = stones[1]['vel']

  vnorm1 = tuple(si - vi for si, vi in zip((vx, vy, vz), stones[0]['vel']))
  vnorm2 = tuple(si - vi for si, vi in zip((vx, vy, vz), stones[1]['vel']))
  pos0 = stones[0]['pos']
  pos1 = stones[1]['pos']
  a = np.array([[1, 0, 0, vx - v0[0], 0],
                [0, 1, 0, vy - v0[1], 0],
                [0, 0, 1, vz - v0[2], 0],
                [1, 0, 0, 0, vx - v1[0]],
                [0, 1, 0, 0, vy - v1[1]]])
  b = np.array([pos0[0], pos0[1], pos0[2], pos1[0], pos1[1]])
  try:
    sol = np.linalg.solve(a, b)
  except:
    # Matrices that are not invertible fall in this bucket
    return None
  x, y, z, t1, t2 = sol
  # Non-integer solutions
  if abs(x - round(x)) > 1e-4 or abs(y - round(y)) > 1e-4 or abs(z - round(z)) > 1e-4:
    return None
  x = round(x)
  y = round(y)
  z = round(z)
  # Negative times (should be avoided by earlier checks for valid / ranges, but double-checking here)
  if t1 < 0 or t2 < 0:
    return None
  for s in stones:
    for idx in range(3):
      if s['vel'][idx] != (vx, vy, vz)[idx]:
        t = (s['pos'][idx] - (x, y, z)[idx]) / (s['vel'][idx] - (vx, vy, vz)[idx]) * -1
        break
    for idx in range(3):
      if s['pos'][idx] + s['vel'][idx] * t != (x, y, z)[idx] + (vx, vy, vz)[idx] * t:
        return None
  return x, y, z, t1, t2


'''
Now the main loop:
-Loop through all possible values of vx, vy, vz
---in particular, start with (max absolute value = 1), then 2, then 3, ...
-Check if that vx, vy, vz is possible

In the real solution, 'ranges' isn't needed. So we could have just iterated through the possible valid values, rather than this complicated loop that allows for unbounded vx, vy, vz.

But, in the example, it is (vx is smaller than the velocity of any of the stones' x velocities).
'''
v1 = 0
while True:
  v1 += 1
  print(v1)
  for v2 in range(v1 + 1):
    for v3 in range(v2 + 1):
      for absvx, absvy, absvz in ((v1, v2, v3), (v1, v3, v2), (v2, v1, v3), (v2, v3, v1), (v3, v1, v2), (v3, v2, v1)):
        for vx in (absvx, absvx * -1):
          if vx not in valids[0] and vx < ranges[0][0] and vx > ranges[0][1]:
            continue
          for vy in (absvy, absvy * -1):
            if vy not in valids[1] and vy < ranges[1][0] and vy > ranges[1][1]:
              continue
            for vz in (absvz, absvz * -1):
              if vz not in valids[2] and vz < ranges[2][0] and vz > ranges[2][1]:
                continue
              sol = check(vx, vy, vz, stones)
              if sol is not None:
                print(sol[0] + sol[1] + sol[2])
                print(sol)
                print((vx, vy, vz))
                quit()
