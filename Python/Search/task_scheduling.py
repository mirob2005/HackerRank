def addJob(array, deadline,minutes,late):
    length = len(array)
    if length < deadline:
        for i in range(deadline-length):
            array.append(-1)
    minLeft = minutes
    for i in range(1,deadline+1):
        if array[deadline-i] >= 0:
            continue
        else:
            array[deadline-i] += 1
            minLeft -=1
            if minLeft ==0:
                break
    late += minLeft
    return late

if __name__ == '__main__':

    n = int(input().strip())
    
    nl = []
    late = 0
    for op in range(n):
        job = input().split(' ')
        late = addJob(nl,int(job[0]),int(job[1]),late)
        print(late)