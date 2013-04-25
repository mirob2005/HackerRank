def quickSort(m, ar):
    if m < 2:
        print(ar[0])
    else:
        p = ar[0]
        less = []
        more = []
        for item in ar[1:]:
            if item < p:
                less.append(item)
            else:
                more.append(item)
        final = less + [p] + more
        print(' '.join([str(x) for x in final]))
    


m = int(input())
ar = [int(i) for i in input().strip().split()]
quickSort(m, ar)