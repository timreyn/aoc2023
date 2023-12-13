import requests
import sys
from bs4 import BeautifulSoup

day = int(sys.argv[1])
cookies = {'session': sys.argv[2].replace('session=', '')}
leaderboard_id = int(sys.argv[3])

homepage = BeautifulSoup(requests.get('https://www.adventofcode.com', cookies=cookies).text, features="lxml")
user = homepage.body.find('div', attrs={'class': 'user'}).text.split(' ')[0]
leaderboard = requests.get('https://www.adventofcode.com/2023/leaderboard/private/view/%d.json' % leaderboard_id, cookies=cookies).json()
for line in open('%d/times.txt' % day):
  start = int(line.strip().split(' ')[1])
  break

def w(f, heading, idx, day):
  t = day[str(idx)]['get_star_ts']
  d = t - start
  print(d)
  formatted = ':%02d' % (d % 60)
  d = d // 60
  while d > 0:
    if d > 60:
      formatted = (':%02d' % (d % 60)) + formatted
    else:
      formatted = ('%d' % d) + formatted
    d = d // 60
  if len(formatted) == 3:
    formatted = '0' + formatted
  f.write('%s: %s\n' % (heading, formatted))

with open('%d/times.txt' % day, 'a') as f:
  for m in leaderboard['members'].values():
    if m['name'] != user:
      continue
    this_day = m['completion_day_level'][str(day)]

    w(f, 'Part 1', '1', this_day)
    w(f, 'Both parts', '2', this_day)
