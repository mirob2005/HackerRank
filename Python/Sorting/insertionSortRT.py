#!/bin/python

# Head ends here
def insertionSort(m,ar):
    shift = 0
    if m < 2:
        print(shift)
    else:
        for index in range(1,m):
            while ar[index] < ar[index-1]:
                ar[index], ar[index-1] = ar[index-1],ar[index]
                shift += 1
                if index > 1:
                    index -= 1
        print(shift)


# Tail starts here

m = int(input())
ar = [int(i) for i in input().strip().split()]
insertionSort(m, ar)