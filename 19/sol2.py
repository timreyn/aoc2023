import collections
import copy
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

instrs = {}

def c(part, instrs, wkf):
  for instr in instrs[wkf][:-1]:
    to_check = instr[0]
    op = instr[1]
    cmp = int(instr[2:instr.index(':')])
    dest = instr[instr.index(':') + 1:]
    success = False
    if op == '<':
      success = part[to_check] < cmp
    elif op == '>':
      success = part[to_check] > cmp
    if success:
      return dest
  return instrs[wkf][-1]

todo = [
  {
    'x': {'min': 1, 'max': 4000},
    'm': {'min': 1, 'max': 4000},
    'a': {'min': 1, 'max': 4000},
    's': {'min': 1, 'max': 4000},
    'wkf': 'in',
  }
]

for line in open(fname):
  line = line.strip()
  if not line:
    break
  instrs[line[0:line.index('{')]] = line[line.index('{') + 1:-1].split(',')

while todo:
  part = todo.pop()
  wkf = part['wkf']
  if wkf == 'A':
    sub = 1
    for k in 'xmas':
      sub *= (part[k]['max'] - part[k]['min'] + 1)
    out += sub
    continue
  if wkf == 'R':
    continue
  finished = False
  for instr in instrs[wkf][:-1]:
    if finished:
      break
    to_check = instr[0]
    op = instr[1]
    cmp = int(instr[2:instr.index(':')])
    dest = instr[instr.index(':') + 1:]
    if op == '<':
      if part[to_check]['max'] < cmp:
        # Guaranteed
        part['wkf'] = dest
        todo += [part]
        finished = True
      elif part[to_check]['min'] >= cmp:
        # Impossible
        continue
      else:
        # Fork
        new = copy.deepcopy(part)
        new[to_check]['max'] = cmp - 1
        new['wkf'] = dest
        part[to_check]['min'] = cmp
        todo += [part, new]
        finished = True
    elif op == '>':
      if part[to_check]['min'] > cmp:
        # Guaranteed
        part['wkf'] = dest
        todo += [part]
        finished = True
        break
      elif part[to_check]['max'] <= cmp:
        # Impossible
        continue
      else:
        # Fork
        new = copy.deepcopy(part)
        new[to_check]['min'] = cmp + 1
        new['wkf'] = dest
        part[to_check]['max'] = cmp
        todo += [part, new]
        finished = True
  if not finished:
    part['wkf'] = instrs[wkf][-1]
    todo += [part]


print(out)
