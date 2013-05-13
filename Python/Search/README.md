# Algorithms:

## Search:
https://www.hackerrank.com/categories/algorithms/search

- 6/8 Completed Successfully

### Arithmetic Progressions:
https://www.hackerrank.com/challenges/arithmetic-progressions

- 3/9 Correct (6 Time Limit)
- Submission: https://www.hackerrank.com/submissions/code/637454

- NOT DONE

### Billboards
https://www.hackerrank.com/challenges/billboards

- 10/10 Correct
- Submission: https://www.hackerrank.com/submissions/code/641716
- Longest Time: 0.78 seconds where N = 98789 and K = 21012

- Done using Dynamic Programming
- Originally, I was filling out a KN table to record all possibilities and thus achieving O(KN) complexity.
- This took ~60 seconds for a less complex test case (N = 40000, K = 6000), and eventually down to ~35 seconds by skipping rows in the table and by using a 2 by K table.
- Now, the algorithm starts by taking in the first K+1 elements.
- Then we keep a N element array for our DP table and an array to keep a queue of skippable indices.
- The DP table will begin by recording the first K+1 elements, but then start recording the sum of the skippable billboards.
- By the end, the first index in our queue will correspond to the index in our DP table which will be the sum of the billboards we will skip.
- This way, our time complexity is O(N) and our space complexity is also O(N).
- Constraints on the problem were: 0<K<=N<=100,000

### Coin on the Table:
https://www.hackerrank.com/challenges/coin-on-the-table

- 10/10 Correct
- Submission: https://www.hackerrank.com/submissions/code/633605
- Longest Time: 7.05 seconds where N,M < 51 and K < 1001 (table of 2500 squares)

- Done using Dynamic Programming.
- All of the squares are stored in a table. Each sqaure has 4 items stored: current direction, current distance to goal, current number of changes required to reach goal, original direction.
- The table is filled out initially by starting at the goal and going outward in a BFS-type way using a queue.
- The table is recalculated in a similar fashion and each time a square gets updated, the surrounding squares get checked and updated if necessary.
- These rechecks are necessary to ensure an update gets propagated throughout all of the squares.
- This algorithm answers the least number of changes for a valid path for all squares not just the start point and does so in a time-efficient way.
- Test checks up to a 50 by 50 table with paths up to 1000 squares long.

### Flowers:
https://www.hackerrank.com/challenges/flowers

- 10/10 Correct
- Submission: https://www.hackerrank.com/submissions/code/626703
- Longest Test: 0.12 seconds

- Prices are sorted in order of lowest to highest.
- Then the highest priced item is removed and given to the next available 'friend'.
- Repeating as necessary so that the person with the most flowers has at most one more than the friend with the least.

### Median
https://www.hackerrank.com/challenges/median

- 10/10 Correct
- Submission: https://www.hackerrank.com/submissions/code/635851
- Longest Test: 4.6 seconds where 0<n<=100,000

- Each additional number added to the list is inserted using binary search to find the correct index.
- Each number removed is also found (or not found) using binary search to find the index to remove.
- This way the list is sorted as the numbers are inputted and the list never has to be explicitly sorted.
- The median is found by seeing if the list has an even number or odd number of elements.
- If even, the median is the average of the 2 middle elements found using: 'index1 = length//2 -1' and 'index2 = length//2'.
- If odd, the median is the middle element found using: index = length//2

### Pairs:
https://www.hackerrank.com/challenges/pairs

- 15/15 Correct
- Submission: https://www.hackerrank.com/submissions/code/626684
- Longest Test: 0.3 seconds where N<=10^5

- The numbers are sorted from lowest to highest.
- The algorithm starts with a number xi and iterates though all of the following numbers until one is found to be equal to xi + K or greater than xi + K.
- If it's equal, we incremement our count and move on to the next number.
- Else we just move on to the next number.

### Task Scheduling:
https://www.hackerrank.com/challenges/task-scheduling

- 10/10 Correct
- Submission: https://www.hackerrank.com/submissions/code/636683
- Longest Test: <3 seconds (100,000 tasks)

- Done with dynamic programming in mind. (Stores data to avoid recalculation for each added task)
- The program keeps track of the latest deadline and keeps a list of usuable time slots.
- Whenever a time slot is used, it is popped from the list.
- The greatest time slot prior to the deadline time is used first.
- In order to find this greatest available time slot before the deadline, a binary search of the list is conducted and returns the index.
- This index and subsequent lower indices are popped from the list until there are no more time slots or until all minutes are used up.
- If we run out of time slots, the remaining minutes are added to the lateness of the deadlines.

### Triplets:
https://www.hackerrank.com/challenges/triplets

- 6/15 Correct (9 Time Limit)
- Current Approach time complexity: O(n^3). Solution requires O(nlogn) to make time limit.
- Submission: https://www.hackerrank.com/submissions/code/637455

- NOT DONE
