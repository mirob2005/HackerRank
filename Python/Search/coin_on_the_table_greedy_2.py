class coord:
    def __init__(self,y,x):
        self.x = x
        self.y = y
    def __add__(self,other):
        return coord(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return coord(self.x-other.x,self.y-other.y)
    def __str__(self):
        return 'X: %s, Y: %s'%(self.x,self.y)
    def distance(self,startX,startY):
        return (self.x - startX) + (self.y - startY)

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



NMK = input().strip()

N = int(NMK.split(' ')[0])
M = int(NMK.split(' ')[1])
K = int(NMK.split(' ')[2])

table = []

for row in range(N):
    table.append([])
    for char in input().strip():
        table[row].append(char)


if computeCount(table,K,N,M) <= K:
    print(0)
else:
    for ri,row in enumerate(table):
        for ci,column in enumerate(row):
            if column == '*':
                goal = coord(ri,ci)
                print(goal)
                break
    if goal.distance(0,0) > K:
        print(-1)
    else:
        changes = 0
        x = 0
        y = 0
        ptr = table[y][x]
        while ptr != '*':
            if ptr == 'L' or ptr == 'U':
                if goal.x > x and goal.y > y:
                    table[y][x] = 'R'
                    xCount = computeCount(table,K,N,M)
                    table[y][x] = 'D'
                    yCount = computeCount(table,K,N,M)
                    if xCount < yCount:
                        print('Changing1 (%s,%s) from %s to %s'%(x,y,ptr,'R'))
                        table[y][x] = 'R'
                    else:
                        print('Changing2 (%s,%s) from %s to %s'%(x,y,ptr,'D'))
                elif goal.x >x:
                    print('Changing1 (%s,%s) from %s to %s'%(x,y,ptr,'R'))
                    table[y][x] = 'R'
                else:
                    print('Changing2 (%s,%s) from %s to %s'%(x,y,ptr,'D'))
                    table[y][x] = 'D'
                changes += 1
            elif ptr == 'R' and goal.x <= x:
                print('Changing3 (%s,%s) from %s to %s'%(x,y,ptr,'D'))
                table[y][x] = 'D'
                changes += 1
            elif ptr == 'D' and goal.y <= y:
                print('Changing4 (%s,%s) from %s to %s'%(x,y,ptr,'R'))
                table[y][x] = 'R'
                changes += 1
            else:
                if ptr == 'D':
                    y +=1
                else:
                    x +=1
            if computeCount(table,K,N,M) <= K:
                print(changes)
                break
            ptr = table[y][x]