import time

if __name__ == '__main__':
    s = time.clock()
    N = int(input())
    
    numbers = input().split(' ')
    numbers = [int(x) for x in numbers]
    
    visited = [False for x in range(100001)]
    
    tuples = set()
    
    for index, number in enumerate(numbers):
        if not visited[number]:
            first = number
            while index < N-1:
                index += 1
                if number < numbers[index]:
                    second = numbers[index]
                    thirdIndex = index
                    while thirdIndex < N-1:
                        thirdIndex += 1
                        if second < numbers[thirdIndex]:
                            tuples.add((first,second,numbers[thirdIndex]))
                else:
                    continue

    print(len(tuples))
    #print(tuples)
    f = time.clock()
    total = (f-s)
    print(total)