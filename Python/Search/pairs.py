NK = input()

N = int(NK.partition(' ')[0])
K = int(NK.partition(' ')[2])

numbers = [int(x) for x in input().strip().split(' ')]

numbers.sort()

count = 0

for index, num in enumerate(numbers):
    while index < N and num + K > numbers[index]:
        index += 1
    if index == N:
        continue
    elif num + K == numbers[index]:
        count += 1
        
print(count)