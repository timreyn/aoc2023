
count = 0

for line in open('input.txt'):
  works = True
  for seg in line.strip().split(':')[1].split(';'):
    for ball in seg.strip().split(','):
      parts = ball.strip().split(' ')
      amt = int(parts[0])
      color = parts[1]
      if color == 'red' and amt > 12:
        works = False
      elif color == 'green' and amt > 13:
        works = False
      elif color == 'blue' and amt > 14:
        works = False
  if works:
    count += int(line.split(':')[0].split(' ')[1])
print(count)
