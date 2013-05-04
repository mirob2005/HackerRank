if __name__ == '__main__':
    NK = input().split(' ')
    N = int(NK[0])
    K = int(NK[1])

    profits = []

    for billboard in range(N):
        profits.append(int(input()))

    table = []

    for row in range(N+1):
        table.append([])
    table[0] = [0 for x in range(K+1)]

    for index,bb in enumerate(profits):
        for adjacent in range(K+1):
            if adjacent == 0:
                table[index+1].append(max(table[index]))
            else:
                table[index+1].append(table[index][adjacent-1]+bb)

    value = 0
    for row in table:
        high = max(row)
        if high > value:
            value = high

    print(value)