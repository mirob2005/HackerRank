def addJob(array,job):
    if not array:
        array.append([job[0],[job[1]]])
        return
    if len(array) == 1:
        if job[0] > array[0][0]:
            array.append([job[0],[job[1]]])
        elif job[0] < array[0][0]:
            array.insert(0,[job[0],[job[1]]])
        else:
            array[0][1].append(job[1])
        return
    si = 0
    ei = len(array)-1
    binarySearchInsert(array,job,si,ei)
    
def binarySearchInsert(array,job,si,ei):
    if si==ei:
        if job[0] > array[si][0]:
            array.insert(si+1,[job[0],[job[1]]])
        elif job[0] < array[si][0]:
            array.insert(si,[job[0],[job[1]]])
        else:
            array[si][1].append(job[1])
        return
    else:
        middle = (ei-si)//2 +si
        
        if job[0] > array[middle][0]:
            binarySearchInsert(array,job,middle+1,ei)
        elif job[0] < array[middle][0]:
            binarySearchInsert(array,job,si,middle)
        else:
            array[middle][1].append(job[1])
            return

def computeLateness(jobs):
    maxLate = 0
    time = 0
    for deadline in jobs:
        for job in deadline[1]:
            time += job
            if time > deadline[0]:
                late = (time-deadline[0])
                if late > maxLate:
                    maxLate = late
    print(maxLate)

if __name__ == '__main__':

    n = int(input().strip())
    
    nl = []
    
    for op in range(n):
        job = input().split(' ')
        addJob(nl,[int(x) for x in job])

        computeLateness(nl)