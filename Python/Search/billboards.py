if __name__ == '__main__':
    NK = input().split(' ')
    N = int(NK[0])
    K = int(NK[1])

    profits = []

    for billboard in range(N):
        profits.append(int(input()))
        
    combinations = []
    
    factor = K +1
    
    for x in range(factor):
        combinations.append(0)
    
        for index,bb in enumerate(profits):
            if (index + 1)%factor != x:
                combinations[x]+= bb

    print(max(combinations))