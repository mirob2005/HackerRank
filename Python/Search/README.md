# Algorithms:

## Search:
https://www.hackerrank.com/categories/algorithms/search

### Coin on the Table:
https://www.hackerrank.com/challenges/coin-on-the-table

- 9/9 Correct
- Done using Dynamic Programming.
- All of the squares are stored in a table. Each sqaure has 4 items stored: current direction, current distance to goal, current number of changes required to reach goal, original direction.
- The table is filled out initially by starting at the goal and going outward in a BFS-type way using a queue.
- The table is recalculated in a similar fashion and each time a square gets updated, the surrounding sqaures get checked and updated if necessary.
- These rechecks are necessary to ensure an update gets propagated throughout all of the squares.
- This algorithm answers the least number of changes for a valid path for all squares not just the start point and does so in a time-efficient way.
- Test checks up to a 50 by 50 table with paths up to 1000 squares long.

### Flowers:
https://www.hackerrank.com/challenges/flowers

- 9/9 Correct
- Prices are sorted in order of lowest to highest.
- Then the highest priced item is removed and given to the next available 'friend'.
- Repeating as necessary so that the person with the most flowers has at most one more than the friend with the least.

### Pairs:
https://www.hackerrank.com/challenges/pairs

- 14/14 Correct
- The numbers are sorted from lowest to highest.
- The algorithm starts with a number xi and iterates though all of the following numbers until one is found to be equal to xi + K or greater than xi + K.
- If it's equal, we incremement our count and move on to the next number.
- Else we just move on to the next number.
