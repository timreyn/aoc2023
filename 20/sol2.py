import collections
import math
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

LOW = 0
HIGH = 1

OFF = 3
ON = 4

config = {}
flips = {}
inputs = collections.defaultdict(list)
conjs = {}

for line in open(fname):
  line = line.strip().split(' -> ')
  if line[0] == 'broadcaster':
    config['broadcaster'] = {'type': 'broadcaster', 'vals': line[1].split(', ')}
  elif line[0][0] == '%':
    config[line[0][1:]] = {'type': 'flip', 'vals': line[1].split(', ')}
    flips[line[0][1:]] = OFF
    for x in line[1].split(', '):
      inputs[x] += [line[0][1:]]
  elif line[0][0] == '&':
    config[line[0][1:]] = {'type': 'conj', 'vals': line[1].split(', ')}
    conjs[line[0][1:]] = {}

for c, ip in inputs.items():
  conjs[c] = {ipp : LOW for ipp in ip}

sent = {LOW: 0, HIGH: 0}

#Each is cyclical; we're looking for the lcm of when each is seen with a HIGH for the first time, because during that cycle all of them will have a HIGH.
firsts = {}
i = 0

while len(firsts) < 4:
  i += 1
  queue = [('broadcaster', LOW, None)]

  while queue:
    x, v, prev = queue.pop(0)
    sent[v] += 1
    if x == 'output':
      continue
    if x not in config:
      continue
    c = config[x]
    if c['type'] == 'broadcaster':
      for t in c['vals']:
        #print('%d from %s to %s' % (LOW, x, t))
        queue += [(t, LOW, x)]
    elif c['type'] == 'flip':
      if v == LOW:
        flips[x] = 7 - flips[x]
        for t in c['vals']:
          #print('%d from %s to %s' % (flips[x] - 3, x, t))
          queue += [(t, flips[x] - 3, x)]
    elif c['type'] == 'conj':
      conjs[x][prev] = v
      if x == 'll' and sum(conjs[x].values()) >= 1:
        for k in conjs[x]:
          if conjs[x][k] == HIGH and k not in sent:
            firsts[k] = i
      vv = HIGH if LOW in conjs[x].values() else LOW
      for t in c['vals']:
        #print('%d from %s to %s' % (vv, x, t))
        queue += [(t, vv, x)]

print(math.lcm(*list(firsts.values())))
