import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]
times = 1 if len(sys.argv) < 3 else int(sys.argv[2])

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
print(config)

for c, ip in inputs.items():
  conjs[c] = {ipp : LOW for ipp in ip}

sent = {LOW: 0, HIGH: 0}
for i in range(times):
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
      vv = HIGH if LOW in conjs[x].values() else LOW
      for t in c['vals']:
        #print('%d from %s to %s' % (vv, x, t))
        queue += [(t, vv, x)]

print(sent)
print(sent[LOW] * sent[HIGH])
