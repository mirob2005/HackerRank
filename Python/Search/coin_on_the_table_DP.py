class Element:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class Queue:
    def __init__(self):
        self.head = None        
        
    def __str__(self):
        ptr = self.head
        if(self.head==None):
            string = "Front < > Back"
        else:
            string = "Front < "
            while ptr:
                string += ("%s "%str(ptr.data))
                ptr = ptr.next
            string += "> Back"
        return string
        
    def enQueue(self,data):
        #Append the most recent node to the end
        ptr = self.head
        if(ptr == None):
            self.head = Element(data,self.head)
        else:
            while ptr.next:
                ptr=ptr.next
            ptr.next = Element(data, None)
        
    def deQueue(self):
        #move head ptr and return previous head
        if(self.head == None):
            return None
        ptr = self.head
        self.head = self.head.next
        ptr.next = None
        return ptr.data

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
            table[y][x-1][1],table[y][x-1][2] = computeCount(table,x-1,y,K,N,M)
            queue.enQueue((x-1,y))
            
        if y - 1 >=0 and table[y-1][x][1] == None:
            table[y-1][x][1],table[y-1][x][2] = computeCount(table,x,y-1,K,N,M)
            queue.enQueue((x,y-1))
    
        if x + 1 <M and table[y][x+1][1] == None:
            table[y][x+1][1],table[y][x+1][2] = computeCount(table,x+1,y,K,N,M)
            queue.enQueue((x+1,y))
    
        if y + 1 <N and table[y+1][x][1] == None:
            table[y+1][x][1],table[y+1][x][2] = computeCount(table,x,y+1,K,N,M)
            queue.enQueue((x,y+1))
            
        first = queue.deQueue()

    second = followUp.deQueue()
    while second:
        x = second[0]
        y = second[1]
        table[y][x][1],table[y][x][2],changed = searchNearby(table,x,y,table[y][x][1],table[y][x][2],K,N,M,followUp)
        if changed:
            if x - 1 >=0:
                if checkNearby(table,x,y,x-1,y,K):
                    followUp.enQueue((x-1,y))
            if y - 1 >=0:
                if checkNearby(table,x,y,x,y-1,K):
                    followUp.enQueue((x,y-1))
            if x + 1 <M:
                if checkNearby(table,x,y,x+1,y,K):
                    followUp.enQueue((x+1,y))
            if y + 1 <N:
                if checkNearby(table,x,y,x,y+1,K):
                    followUp.enQueue((x,y+1))
        second = followUp.deQueue()
        
    if table[0][0][1] == float('inf'):
        return -1
    else:
        return table[0][0][2]

def computeCount(table,startX,startY,K,N,M):
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
            dist,count,changed = searchNearby(table,startX,startY,dist,count,K,N,M)
        return (dist,count)

def searchNearby(table,x,y,dist,count,K,N,M,queue=None):
    ptr = table[y][x]
    best = count
    prevCount = count
    prevDist = dist
    prevDir = table[y][x][0]
    
    if y + 1 <N:
        if table[y+1][x][1] != None and table[y+1][x][1]+1 <= K and (table[y+1][x][2] < best or dist == float('inf')):
            dist = table[y+1][x][1]+1
            if table[y][x][3] == 'D':
                best = table[y+1][x][2]
            else:
                best = table[y+1][x][2]+1
            if table[y][x][0] != 'D':
                table[y][x][0] = 'D'

    if x + 1 <M:
        if table[y][x+1][1] != None and table[y][x+1][1]+1 <= K and (table[y][x+1][2] < best or dist == float('inf')):
            dist = table[y][x+1][1]+1
            if table[y][x][3] == 'R':
                best = table[y][x+1][2]
            else:
                best = table[y][x+1][2]+1
            if table[y][x][0] != 'R':
                table[y][x][0] = 'R'

    if y - 1 >=0:
        if table[y-1][x][1] != None and table[y-1][x][1]+1 <= K and (table[y-1][x][2] < best or dist == float('inf')):
            dist = table[y-1][x][1]+1
            if table[y][x][3] == 'U':
                best = table[y-1][x][2]
            else:
                best = table[y-1][x][2]+1
            if table[y][x][0] != 'U':
                table[y][x][0] = 'U'

    if x - 1 >=0:
        if table[y][x-1][1] != None and table[y][x-1][1]+1 <= K and (table[y][x-1][2] < best or dist == float('inf')):
            dist = table[y][x-1][1]+1
            if table[y][x][3] == 'L':
                best = table[y][x-1][2]
            else:
                best = table[y][x-1][2]+1
            if table[y][x][0] != 'L':
                table[y][x][0] = 'L'

    if prevCount == best and prevDist == dist and prevDir == table[y][x][0]:
        changed = False
    else:
        changed = True
    
    if dist > K:
        return float('inf'),0,changed
    else:
        return dist,best,changed
    
def checkNearby(table,x1,y1,x2,y2,K):
    if table[y1][x1][1] == K:
        return False
    if table[y1][x1][2] < table[y2][x2][2] or table[y2][x2][1] == float('inf'):
        return True
    else:
        return False
    

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
    
    print(traverseTable(table,endpt[1],endpt[0],K,N,M))
    