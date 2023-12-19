import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

switched = False
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

for line in open(fname):
  line = line.strip()
  if not line:
    switched = True
    continue
  if not switched:
    instrs[line[0:line.index('{')]] = line[line.index('{') + 1:-1].split(',')
  else:
    part = {}
    for p in line[1:-1].split(','):
      part[p[0]] = int(p[2:])
    wkf = 'in'
    while wkf != 'A' and wkf != 'R':
      wkf = c(part, instrs, wkf)
    if wkf == 'A':
      out += sum(part.values())

print(out)
