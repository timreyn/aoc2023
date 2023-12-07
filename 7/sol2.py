import collections
import sys

fname = 'input.txt' if len(sys.argv) < 2 else sys.argv[1]

out = 0
hands = []

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

CARDS = 'J23456789TQKA'

def val(hand):
  freqs = collections.defaultdict(int)
  jacks = 0
  jack_card = 'n/a'
  for h in hand:
    if h == 'J':
      jacks += 1
    else:
      freqs[h] += 1
  if hand == 'JJJJJ':
    freqs['J'] = 5
  elif jacks > 0:
    m = max(freqs.values())
    for h in hand:
      if h != 'J' and freqs[h] == m:
        freqs[h] += jacks
        jack_card = h
        break
  if 5 in freqs.values():
    return FIVE_OF_A_KIND
  elif 4 in freqs.values():
    return FOUR_OF_A_KIND
  elif 3 in freqs.values() and 2 in freqs.values():
    return FULL_HOUSE
  elif 3 in freqs.values():
    return THREE_OF_A_KIND
  elif sorted(list(freqs.values())) == [1, 2, 2] or sorted(list(freqs.values())) == [2, 2]:
    return TWO_PAIR
  elif 2 in freqs.values():
    return ONE_PAIR
  else:
    return HIGH_CARD

def sort_func(hh):
  h = hh[0]
  return val(h) * 13 ** 5 + CARDS.index(h[0]) * 13 ** 4 + CARDS.index(h[1]) * 13 ** 3 + CARDS.index(h[2]) * 13 ** 2 + CARDS.index(h[3]) * 13 ** 1 + CARDS.index(h[4])

for line in open(fname):
  line = line.strip().split(' ')
  hands += [(line[0], int(line[1]))]

already_shown = set()

hands.sort(key=sort_func)
for i, hh in enumerate(hands):
  out += (i + 1) * hh[1]



print(out)
