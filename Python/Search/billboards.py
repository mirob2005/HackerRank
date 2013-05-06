import time

if __name__ == '__main__':
    s= time.clock()
    
    NK = input().split(' ')
    N = int(NK[0])
    K = int(NK[1])

    profits = []

    for billboard in range(N):
        profits.append(int(input()))

    table = []

    for row in range(2):
        table.append([0 for x in range(K+1)])

    index = True
    for bb in profits:
        table[not index][0] = max(table[index])
        table[not index][1:] = [x+bb for x in table[index][:-1]]
        index = not index

    print(max(table[index]))
    
    f = time.clock()
    total = f-s
    print('Time: %s'%total)