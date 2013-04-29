from Queue_head import Queue

def findEnd(table):
    for ri,row in enumerate(table):
        for ci,column in enumerate(row):
            if column[0] == '*':
                return (ri,ci)
    return None

def traverseTable(table,startX,startY,K,N,M):
    x,y = startX,startY
    
    queue = Queue()
    followUp = Queue()
    queue.enQueue((x,y))
    first = queue.deQueue()
    while first:
        followUp.enQueue(first)
        x = first[0]
        y = first[1]
        if x - 1 >=0 and table[y][x-1][1] == None:
            #print('x - 1 >=0')
            table[y][x-1][1],table[y][x-1][2] = computeCount(table,x-1,y,K,N,M)
            #if table[y][x-1][1] == float('inf'):
                #print('BAD')
                #Search for better
            #table[y][x-1][1],table[y][x-1][2] = searchNearby(table,x-1,y,table[y][x-1][1],table[y][x-1][2],K,N,M)
            #traverseTable(table,x-1,y,K,N,M)
            queue.enQueue((x-1,y))
            
        if y - 1 >=0 and table[y-1][x][1] == None:
            #print('y - 1 >=0')
            table[y-1][x][1],table[y-1][x][2] = computeCount(table,x,y-1,K,N,M)
            #if table[y-1][x][1] == float('inf'):
                #print('BAD')
                #Search for better
            #table[y-1][x][1],table[y-1][x][2] = searchNearby(table,x,y-1,table[y-1][x][1],table[y-1][x][2],K,N,M)
            #traverseTable(table,x,y-1,K,N,M)
            queue.enQueue((x,y-1))
    
        if x + 1 <M and table[y][x+1][1] == None:
            #print('x + 1 <M')
            table[y][x+1][1],table[y][x+1][2] = computeCount(table,x+1,y,K,N,M)
            #if table[y][x+1][1] == float('inf'):
                #print('BAD')
                #Search for better
            #table[y][x+1][1],table[y][x+1][2] = searchNearby(table,x+1,y,table[y][x+1][1],table[y][x+1][2],K,N,M)
            #traverseTable(table,x+1,y,K,N,M)
            queue.enQueue((x+1,y))
    
        if y + 1 <N and table[y+1][x][1] == None:
            #print('y + 1 <N')
            table[y+1][x][1],table[y+1][x][2] = computeCount(table,x,y+1,K,N,M)
            #if table[y+1][x][1] == float('inf'):
                #print('BAD')
                #Search for better
            #table[y+1][x][1],table[y+1][x][2] = searchNearby(table,x,y+1,table[y+1][x][1],table[y+1][x][2],K,N,M)
            #traverseTable(table,x,y+1,K,N,M)
            queue.enQueue((x,y+1))
            
        first = queue.deQueue()
        
    print('##################')
    for row in table:
        print(row)
    print('##################')

    second = followUp.deQueue()
    while second:
        x = second[0]
        y = second[1]
        table[y][x][1],table[y][x][2] = searchNearby(table,x,y,table[y][x][1],table[y][x][2],K,N,M)
        second = followUp.deQueue()
    #    
    #for ri,row in enumerate(table):
    #    for si,square in enumerate(row):
    #        square[1],square[2] = searchNearby(table,si,ri,square[1],square[2],K,N,M)
    
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
        count = table[y][x][2]
        if dist > K:
            #print('sx %s sy %s'%(startX, startY))
            #print('x %s y %s'%(x, y))
            dist,count = searchNearby(table,startX,startY,dist,count,K,N,M)
        return (dist,count)

def searchNearby(table,x,y,dist,count,K,N,M):
    ptr = table[y][x]
    best = count
    #print('--------------------------')
    #print('x: %s y: %s'%(x,y))
    #print('best: %s' %best)
    #print('dist: %s' %dist)

    
    if y + 1 <N:
        #print('y + 1 <N')
        #if table[y+1][x][1] == None:
            #table[y+1][x][1],table[y+1][x][2] = computeCount(table,x,y+1,K,N,M)
        if table[y+1][x][1] != None and table[y+1][x][1]+1 <= K and (table[y+1][x][2] < best or dist == float('inf')):
            dist = table[y+1][x][1]+1
            #print(table[y][x][0])
            if table[y][x][3] == 'D':
                best = table[y+1][x][2]
            else:
                best = table[y+1][x][2]+1
            if table[y][x][0] != 'D':
                table[y][x][0] = 'D'
        #    print('best: %s' %best)
        #    print('dist: %s' %dist)
        #else:
        #    print('NODICE:')
        #    print('Not None?: %s'%str(table[y+1][x][1]))
        #    #print('<K: %s'%str(table[y+1][x][1]+1))
        #    print('%d < %d OR'%(table[y+1][x][2],best))
        #    print('%f == inf'%dist)
        
    if x + 1 <M:
        #print('x + 1 <M')
        #if table[y][x+1][1] == None:
            #table[y][x+1][1],table[y][x+1][2] = computeCount(table,x+1,y,K,N,M)
        if table[y][x+1][1] != None and table[y][x+1][1]+1 <= K and (table[y][x+1][2] < best or dist == float('inf')):
            dist = table[y][x+1][1]+1
            if table[y][x][3] == 'R':
                best = table[y][x+1][2]
            else:
                best = table[y][x+1][2]+1
            if table[y][x][0] != 'R':
                table[y][x][0] = 'R'
                #print('best: %s' %best)
                #print('dist: %s' %dist)
        #else:
        #    print('NODICE:')
        #    print('Not None?: %s'%str(table[y][x+1][1]))
        #    #print('<K: %s'%str(table[y][x+1][1]+1))
        #    print('%d < %d OR'%(table[y][x+1][2],best))
        #    print('%f == inf'%dist)
        
    if y - 1 >=0:
        #print('y - 1 >=0')
        #if table[y-1][x][1] == None:
            #table[y-1][x][1],table[y-1][x][2] = computeCount(table,x,y-1,K,N,M)
        if table[y-1][x][1] != None and table[y-1][x][1]+1 <= K and (table[y-1][x][2] < best or dist == float('inf')):
            dist = table[y-1][x][1]+1
            if table[y][x][3] == 'U':
                best = table[y-1][x][2]
            else:
                best = table[y-1][x][2]+1
            if table[y][x][0] != 'U':
                table[y][x][0] = 'U'

    if x - 1 >=0:
        #print('x - 1 >=0')
        #if table[y][x-1][1] == None:
            #table[y][x-1][1],table[y][x-1][2] = computeCount(table,x-1,y,K,N,M)
        if table[y][x-1][1] != None and table[y][x-1][1]+1 <= K and (table[y][x-1][2] < best or dist == float('inf')):
            dist = table[y][x-1][1]+1
            if table[y][x][3] == 'L':
                best = table[y][x-1][2]
            else:
                best = table[y][x-1][2]+1
            if table[y][x][0] != 'L':
                table[y][x][0] = 'L'


    #print('After:')
    #print('best: %s' %best)
    #print('dist: %s' %dist)


    #print(best)
    if dist > K:
        return float('inf'),0
    else:
        return dist,best
    
    

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