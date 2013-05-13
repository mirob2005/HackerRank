import time
import math

if __name__ == '__main__':
    
    s = time.clock()
    
    #Store computed factorials to avoid recalculating
    fact = {}

    
    N = int(input())
    
    AP = []
    
    for ap in range(N):
        AP.append([int(x) for x in input().split(' ')])
    
    
    Q = int(input())
    
    for op in range(Q):
        operation = [int(x) for x in input().split(' ')]
        
        if operation[0] == 0:
            #Query
            index = operation[1] - 1
            K=0
            V=1
            while index < operation[2]:
                K+=AP[index][2]
                V*=pow(AP[index][1],AP[index][2])
                index += 1
            if K in fact:
                V*=fact[K]
            else:
                F = math.factorial(K)
                fact[K] = F
                V*=F
            print('%s %s'%(K,V%1000003))
        else:
            #Update
            index = operation[1] - 1
            while index < operation[2]:
                AP[index][2] += operation[3]
                index += 1
    f = time.clock()
    total = f-s
    print(total)