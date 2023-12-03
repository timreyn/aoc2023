# Usage: For day 1,
#
# ./init.sh 1 session=$SESSION_COOKIE
#
# where $SESSION_COOKIE is grabbed from Chrome.

cp -r template $1
curl --cookie $2 https://adventofcode.com/2023/day/$1/input > $1/input.txt
