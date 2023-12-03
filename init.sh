cp -r template $1
curl --cookie $2 https://adventofcode.com/2023/day/$1/input > $1/input.txt
