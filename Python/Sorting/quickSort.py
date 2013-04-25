def quickSort(ar):
    if len(ar) < 2:
        return(ar)
    else:
        p = ar[0]
        less = []
        more = []
        for item in ar[1:]:
            if item < p:
                less.append(item)
            else:
                more.append(item)
        
        final = less if less else [] + [p] + more if more else []
        
        l = quickSort(less)
        m = quickSort(more)
        subarray = l+ [p] + m
        print(' '.join([str(x) for x in subarray]))
        return l + [p] +m


m = int(input())
ar = [int(i) for i in input().strip().split()]
quickSort(ar)