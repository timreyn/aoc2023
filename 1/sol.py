total = 0

for line in open('input.txt'):
  first = None
  last = None
  for x in line.strip():
    if x.isdigit():
      last = int(x)
      if first is None:
        first = int(x)
  total += 10 * first + last

print(total)
