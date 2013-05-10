if __name__ == '__main__':
    
    NK = input().split(' ')
    N = int(NK[0])
    K = int(NK[1])

    profits = []

    for billboard in range(N):
        profits.append(int(input()))
    
    total = sum(profits)
    
    if K >= N:
        print(total)
    elif K == 0:
        print(0)
    else:
        DPtable = []
        queue = []
    
        for index, profit in enumerate(profits[:K+1]):
            DPtable.append(profit)
            while len(queue) != 0 and profit <= profits[queue[-1]]:
                queue.pop()
            queue.append(index)
        
        for index,profit in enumerate(profits[K+1:]):
            index = index + K + 1
            DPtable.append(DPtable[queue[0]] + profit)
            while len(queue) != 0 and DPtable[index] <= DPtable[queue[-1]]:
                queue.pop()
            while len(queue) != 0 and queue[0] <= index-K-1:
                queue.pop(0)
            queue.append(index)
        
        DPtable.append(DPtable[queue[0]])
        
        print(total-DPtable[-1])