if __name__ == '__main__':
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
        for adjacent in range(1,K+1):
            table[not index][adjacent] = table[index][adjacent-1]+bb
        index = not index

    print(max(table[index]))
