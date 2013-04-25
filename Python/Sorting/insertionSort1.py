#!/bin/python

# Head ends here
def insertionSort(m, ar):
    if m ==1:
        print(ar[0])
    else:
        item = ar[-1]
        index = -2
        while index >= -m and item < ar[index]:
            ar[index+1] = ar[index]
            for element in ar:
                print(element,end = ' ')
            print()
            index -= 1
    
        ar[index+1] = item
        for element in ar:
            print(element,end = ' ')
        print()

# Tail starts here

m = int(input())
ar = [int(i) for i in input().strip().split()]
insertionSort(m, ar)