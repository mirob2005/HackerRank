def insertNumber(array,number):
    if not array:
        array.append(number)
        return
    if len(array) == 1:
        if number > array[0]:
            array.append(number)
        else:
            array.insert(0,number)
        return
    si = 0
    ei = len(array)-1
    binarySearchInsert(array,number,si,ei)
    
def binarySearchInsert(array,number,si,ei):
    if si==ei:
        if number > array[si]:
            array.insert(si+1,number)
            return
        else:
            array.insert(si,number)
            return
    else:
        middle = (ei-si)//2 +si
        
        if number > array[middle]:
            binarySearchInsert(array,number,middle+1,ei)
        elif number < array[middle]:
            binarySearchInsert(array,number,si,middle)
        else:
            array.insert(middle,number)
            return
        
def removeNumber(array,number):
    if not array:
        return False
    if len(array) == 1:
        if number == array[0]:
            array.pop()
            return True
        else:
            return False
    si = 0
    ei = len(array)-1
    return binarySearchRemove(array,number,si,ei)

def binarySearchRemove(array,number,si,ei):
    if si==ei:
        if number == array[si]:
            array.pop(si)
            return True
        else:
            return False
    else:
        middle = (ei-si)//2 +si
        
        if number > array[middle]:
            return binarySearchRemove(array,number,middle+1,ei)
        elif number < array[middle]:
            return binarySearchRemove(array,number,si,middle)
        else:
            array.pop(middle)
            return True
    
def printMedian(nl):
    length = len(nl)
    if length == 0:
        print('Wrong!')
    else:
        if length%2 ==1:
            index = length//2
            median = nl[index]
        else:
            index1 = length//2 -1
            index2 = length//2
            median = (nl[index1]+nl[index2])/2
        if int(median) == median:
            print(int(median))
        else:
            print(median)

n = int(input().strip())

nl = []

for op in range(n):
    operation = input().split(' ')
    if operation[0] == 'a':
        insertNumber(nl,int(operation[1]))
    else:
        if not removeNumber(nl,int(operation[1])):
            print('Wrong!')
            continue
    printMedian(nl)
