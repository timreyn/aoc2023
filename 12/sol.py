import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0

cached = {}

def calc(line, vals):
  global cached
  if (line, vals) in cached:
    return cached[(line, vals)]
  out = calcimpl(line, vals)
  cached[(line, vals)] = out
  return out

def calcimpl(line, vals):
  if not line:
    if vals:
      return 0
    else:
      return 1
  if line.startswith('.'):
    return calc(line[1:], vals)
  if line.startswith('#'):
    if len(vals) > 0 and vals[0] <= len(line):
      substr = line[:vals[0]]
      rem = line[vals[0]:]
      if '.' in substr or rem.startswith('#'):
        return 0
      else:
        return calc(rem[1:], vals[1:])
    else:
      return 0
  if line.startswith('?'):
    return calc(line[1:], vals) + calc('#' + line[1:], vals)

for line in open(fname):
  line = line.strip().split(' ')
  c = calc(line[0], tuple(int(x) for x in line[1].split(',')))
  out += c
  print(line, c)


print(out)
