import time

if __name__ == '__main__':
    s = time.clock()
    N = int(input())
    
    numbers = input().split(' ')
    numbers = [int(x) for x in numbers]

    visited = {}
    tuples = set()
    
    for index,number in enumerate(numbers):
        if number in visited:
            visited[number].append(index)
            visited[number].append([])
        else:
            visited[number] = [index,[]]
        for row in range(number):
            if row in visited.keys():
                length = len(visited[row])
                for i in range(0,length,2):
                    if index > visited[row][i]:
                        visited[row][i+1].append(number)

    for first,second in visited.items():
        #print('%s => %s'%(first,second))
        ptr = 0
        while ptr < len(second):
            index = second[ptr]
            secondItem = second[ptr+1]
            for item in secondItem:
                if item in visited:
                    third = visited[item]
                    tptr = 0
                    while tptr < len(third):
                        secondIndex = third[tptr]
                        if secondIndex > index:
                            for thirdItem in third[tptr+1]:
                                tuples.add((first,item,thirdItem))
                            #print('%s => %s => %s'%(first,item,third[tptr+1]))
                            #count += 1
                        tptr +=2
            ptr +=2
                
        #        print('%s => %s => %s'%(first,item,visited[item]))
        #        count += len(visited[item])

    #print(tuples)
    print(len(tuples))
    f = time.clock()
    total = f-s
    print(total)
    #for key,value in visited.items():
        #print('%s => %s'%(key,value))