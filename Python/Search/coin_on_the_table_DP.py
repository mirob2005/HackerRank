#def computeCount(table,startX,startY,K,N,M):
#    count = 0
#    x,y = startX,startY
#    ptr = table[y][x]
#    while ptr[0] != '*':
#        if count > K:
#            return float('inf')
#        if ptr[0] == 'U':
#            y -= 1
#        elif ptr[0] == 'D':
#            y += 1
#        elif ptr[0] == 'L':
#            x -= 1
#        elif ptr[0] == 'R':
#            x += 1
#        count += 1
#        if x < 0 or x >= M or y < 0 or y >= N:
#            return float('inf')
#        ptr = table[y][x]
#    return count
#
#def traverseTable(table,K,N,M):
#    if computeCount(table,K,N,M) <= K:
#        print(0)
#    else:
#        for ri,row in enumerate(table):
#            for ci,column in enumerate(row):
#                if column == '*':
#                    goal = (ri,ci)
#                    break
#        if goal[0] + goal[1] > K:
#            print(-1)
#        else:
#            changes = 0
#            x = 0
#            y = 0
#            ptr = table[y][x]
#            while ptr != '*':
#                table[y][x] = 'R'
#                RCount = computeCount(table,K,N,M)
#                table[y][x] = 'D'
#                DCount = computeCount(table,K,N,M)
#                table[y][x] = 'U'
#                UCount = computeCount(table,K,N,M)
#                table[y][x] = 'L'
#                LCount = computeCount(table,K,N,M)
#                best = min(RCount,DCount,UCount,LCount)
#                newX = x
#                newY = y
#                if best == float('inf'):
#                    print('inf')
#                    if goal[0] > y:
#                        table[y][x] = 'D'
#                        print('Changing01 (%s,%s) from %s to %s'%(x,y,ptr,'D'))
#                        newY +=1
#                    else:
#                        table[y][x] = 'R'
#                        print('Changing02 (%s,%s) from %s to %s'%(x,y,ptr,'R'))
#                        newX +=1
#    
#                else:
#                    if RCount == best:
#                        table[y][x] = 'R'
#                        print('Changing1 (%s,%s) from %s to %s'%(x,y,ptr,'R'))
#                        newX += 1
#                    elif DCount == best:
#                        table[y][x] = 'D'
#                        print('Changing2 (%s,%s) from %s to %s'%(x,y,ptr,'D'))
#                        newY += 1
#                    elif UCount == best:
#                        table[y][x] = 'U'
#                        print('Changing3 (%s,%s) from %s to %s'%(x,y,ptr,'U'))
#                        newY -=1
#                    else:
#                        table[y][x] = 'L'
#                        print('Changing4 (%s,%s) from %s to %s'%(x,y,ptr,'L'))
#                        newX -=1
#                if ptr != table[y][x]:
#                    changes +=1
#                x = newX
#                y = newY
#                if best <= K:
#                    print(changes)
#                    break
#                ptr = table[y][x]

def findEnd(table):
    for ri,row in enumerate(table):
        for ci,column in enumerate(row):
            if column[0] == '*':
                return (ri,ci)
    return None

def traverseTable(table,startX,startY,K,N,M):
    x,y = startX,startY
    #print('x: %s y: %s'%(x,y))
    
    if x + 1 <M and table[y][x+1][1] == None:
        #print('x + 1 <M')
        table[y][x+1][1],table[y][x+1][2] = computeCount(table,x+1,y,K,N,M)
        if table[y][x+1][1] == float('inf'):
            #print('BAD')
            #Search for better
            table[y][x+1][1],table[y][x+1][2] = searchNearby(table,x+1,y,table[y][x+1][1],K,N,M)
        traverseTable(table,x+1,y,K,N,M)
    if x - 1 >=0 and table[y][x-1][1] == None:
        #print('x - 1 >=0')
        table[y][x-1][1],table[y][x-1][2] = computeCount(table,x-1,y,K,N,M)
        if table[y][x-1][1] == float('inf'):
            #print('BAD')
            #Search for better
            table[y][x-1][1],table[y][x-1][2] = searchNearby(table,x-1,y,table[y][x-1][1],K,N,M)
        traverseTable(table,x-1,y,K,N,M)
    if y + 1 <N and table[y+1][x][1] == None:
        #print('y + 1 <N')
        table[y+1][x][1],table[y+1][x][2] = computeCount(table,x,y+1,K,N,M)
        if table[y+1][x][1] == float('inf'):
            #print('BAD')
            #Search for better
            table[y+1][x][1],table[y+1][x][2] = searchNearby(table,x,y+1,table[y+1][x][1],K,N,M)
        traverseTable(table,x,y+1,K,N,M)
    if y - 1 >=0 and table[y-1][x][1] == None:
        #print('y - 1 >=0')
        table[y-1][x][1],table[y-1][x][2] = computeCount(table,x,y-1,K,N,M)
        if table[y-1][x][1] == float('inf'):
            #print('BAD')
            #Search for better
            table[y-1][x][1],table[y-1][x][2] = searchNearby(table,x,y-1,table[y-1][x][1],K,N,M)
        traverseTable(table,x,y-1,K,N,M)
    
    if table[0][0][1] == float('inf'):
        return -1
    else:
        return table[0][0][2]

def computeCount(table,startX,startY,K,N,M):
    #count = 0
    x,y = startX,startY
    ptr = table[y][x]
    if ptr[0] == 'U':
        y -= 1
    elif ptr[0] == 'D':
        y += 1
    elif ptr[0] == 'L':
        x -= 1
    elif ptr[0] == 'R':
        x += 1
    if x < 0 or x >= M or y < 0 or y >= N:
        return (float('inf'),0)
    else:
        if table[y][x][1] == None:
            dist = float('inf')
        else:
            dist = table[y][x][1] +1
        if dist > K:
            #print('sx %s sy %s'%(startX, startY))
            #print('x %s y %s'%(x, y))
            dist,count = searchNearby(table,startX,startY,dist,K,N,M)
        else:
            count = table[y][x][2]
        return (dist,count)

def searchNearby(table,x,y,dist,K,N,M):
    ptr = table[y][x]
    best = dist
    #print(best)
    count = 0
    if x + 1 <M:
        #if table[y][x+1][1] == None:
            #table[y][x+1][1],table[y][x+1][2] = computeCount(table,x+1,y,K,N,M)
        if table[y][x+1][1] != None and table[y][x+1][1]+1 < best and table[y][x+1][1] != float('inf'):
            best = table[y][x+1][1]+1
            #print('1%s'%best)
            if table[y][x][0] == 'R':
                count = table[y][x+1][2]
            else:
                count = table[y][x+1][2]+1
                table[y][x][0] = 'R'
    if x - 1 >=0:
        #if table[y][x-1][1] == None:
            #table[y][x-1][1],table[y][x-1][2] = computeCount(table,x-1,y,K,N,M)
        if table[y][x-1][1] != None and table[y][x-1][1]+1 < best and table[y][x-1][1] != float('inf'):
            #print('2%s'%best)
            best = table[y][x-1][1]+1
            if table[y][x][0] == 'L':
                count = table[y][x-1][2]
            else:
                count = table[y][x-1][2]+1
                table[y][x][0] = 'L'
    if y + 1 <N:
        #if table[y+1][x][1] == None:
            #table[y+1][x][1],table[y+1][x][2] = computeCount(table,x,y+1,K,N,M)
        if table[y+1][x][1] != None and table[y+1][x][1]+1 < best and table[y+1][x][1] != float('inf'):
            best = table[y+1][x][1]+1
            #print('3%s'%best)
            if table[y][x][0] == 'D':
                count = table[y+1][x][2]
            else:
                count = table[y+1][x][2]+1
                table[y][x][0] = 'D'
    if y - 1 >=0:
        #if table[y-1][x][1] == None:
            #table[y-1][x][1],table[y-1][x][2] = computeCount(table,x,y-1,K,N,M)
        if table[y-1][x][1] != None and table[y-1][x][1]+1 < best and table[y-1][x][1] != float('inf'):
            best = table[y-1][x][1]+1
            #print('4%s'%best)
            if table[y][x][0] == 'U':
                count = table[y-1][x][2]
            else:
                count = table[y-1][x][2]+1
                table[y][x][0] = 'U'
    #print(best)
    if best > K:
        return float('inf'),0
    else:
        return best,count
    
    

if __name__ == '__main__':

    NMK = input().strip()
    
    N = int(NMK.split(' ')[0])
    M = int(NMK.split(' ')[1])
    K = int(NMK.split(' ')[2])
    
    table = []
    
    for row in range(N):
        table.append([])
        for char in input().strip():
            table[row].append([char, None,0,char])

    endpt = findEnd(table)
    table[endpt[0]][endpt[1]][1] = 0
    
    for row in table:
        print(row)
    
    print('ANSWER:%s'%traverseTable(table,endpt[1],endpt[0],K,N,M))
    print('--------------------------------')
    for row in table:
        print(row)