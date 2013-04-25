#!/bin/python

# Head ends here
def insertionSort(m,ar):
    if m < 2:
        print(' '.join([str(x) for x in ar]))
    for index in range(1,m):
        while ar[index] < ar[index-1]:
            ar[index], ar[index-1] = ar[index-1],ar[index]
            if index > 1:
                index -= 1
        print(' '.join([str(x) for x in ar]))


# Tail starts here

m = int(input())
ar = [int(i) for i in input().strip().split()]
insertionSort(m, ar)