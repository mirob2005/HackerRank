def computeCount(table,K,N,M):
    count = 0
    x,y = 0,0
    ptr = table[y][x]
    while ptr != '*':
        if count > K:
            return float('inf')
        if ptr == 'U':
            y -= 1
        elif ptr == 'D':
            y += 1
        elif ptr == 'L':
            x -= 1
        elif ptr == 'R':
            x += 1
        count += 1
        if x < 0 or x >= M or y < 0 or y >= N:
            return float('inf')
        ptr = table[y][x]
    return count

def traverseTable(table,K,N,M):
    if computeCount(table,K,N,M) <= K:
        print(0)
    else:
        for ri,row in enumerate(table):
            for ci,column in enumerate(row):
                if column == '*':
                    goal = (ri,ci)
                    break
        if goal[0] + goal[1] > K:
            print(-1)
        else:
            changes = 0
            x = 0
            y = 0
            ptr = table[y][x]
            while ptr != '*':
                table[y][x] = 'R'
                RCount = computeCount(table,K,N,M)
                table[y][x] = 'D'
                DCount = computeCount(table,K,N,M)
                table[y][x] = 'U'
                UCount = computeCount(table,K,N,M)
                table[y][x] = 'L'
                LCount = computeCount(table,K,N,M)
                best = min(RCount,DCount,UCount,LCount)
                newX = x
                newY = y
                if best == float('inf'):
                    print('inf')
                    if goal[0] > y:
                        table[y][x] = 'D'
                        print('Changing01 (%s,%s) from %s to %s'%(x,y,ptr,'D'))
                        newY +=1
                    else:
                        table[y][x] = 'R'
                        print('Changing02 (%s,%s) from %s to %s'%(x,y,ptr,'R'))
                        newX +=1
    
                else:
                    if RCount == best:
                        table[y][x] = 'R'
                        print('Changing1 (%s,%s) from %s to %s'%(x,y,ptr,'R'))
                        newX += 1
                    elif DCount == best:
                        table[y][x] = 'D'
                        print('Changing2 (%s,%s) from %s to %s'%(x,y,ptr,'D'))
                        newY += 1
                    elif UCount == best:
                        table[y][x] = 'U'
                        print('Changing3 (%s,%s) from %s to %s'%(x,y,ptr,'U'))
                        newY -=1
                    else:
                        table[y][x] = 'L'
                        print('Changing4 (%s,%s) from %s to %s'%(x,y,ptr,'L'))
                        newX -=1
                if ptr != table[y][x]:
                    changes +=1
                x = newX
                y = newY
                if best <= K:
                    print(changes)
                    break
                ptr = table[y][x]

NMK = input().strip()

N = int(NMK.split(' ')[0])
M = int(NMK.split(' ')[1])
K = int(NMK.split(' ')[2])

table = []

for row in range(N):
    table.append([])
    for char in input().strip():
        table[row].append(char)

traverseTable(table,K,N,M)