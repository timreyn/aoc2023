total = 0

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in open('input.txt'):
  first = None
  last = None
  current_word = ''
  for x in line.strip():
    if x.isdigit():
      current_word = ''
      last = int(x)
      if first is None:
        first = int(x)
    else:
      current_word += x
      for i, digit in enumerate(digits):
        if current_word.endswith(digit):
          last = i + 1
          if first is None:
            first = i + 1
  total += 10 * first + last

print(total)
