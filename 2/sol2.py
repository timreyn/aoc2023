
count = 0

for line in open('input.txt'):
  works = True
  mins = {'blue': 0, 'green': 0, 'red': 0}
  for seg in line.strip().split(':')[1].split(';'):
    for ball in seg.strip().split(','):
      parts = ball.strip().split(' ')
      amt = int(parts[0])
      color = parts[1]
      mins[color] = max(mins[color], amt)
  count += mins['blue'] * mins['green'] * mins['red']
print(count)
