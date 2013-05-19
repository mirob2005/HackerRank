

if __name__ == '__main__':
    inputs = input()
    N,K = [int(x) for x in inputs.split(' ')]
    
    current = {}
    pegs = {x+1:[] for x in range(K)}
    
    locs = [int(x) for x in input().split(' ')]
    
    disks = []
    
    moves = []
    
    for index,loc in enumerate(locs):
        index = index+1
        current[index] = [loc,None]
        disks.append(index)
        pegs[loc].append(index)
        
    goal = [int(x) for x in input().split(' ')]
    
    for index,loc in enumerate(goal):
        current[index+1][1] = loc
        
    #print(current)
    #print(pegs)
    
    cur = disks.pop()
    while True:
        #If not in goal location
        if current[cur][0] != current[cur][1]:
            #If movable
            if pegs[current[cur][0]][0] == cur:
                #print('Moving %s from %s to %s'%(cur,current[cur][0],current[cur][1]))
                moves.append((current[cur][0],current[cur][1]))
                pegs[current[cur][0]].pop(0)
                pegs[current[cur][1]].insert(0,cur)
                current[cur][0] = current[cur][1]
            else:
                #Move others off
                #print('%s is blocked, Need to move other'%cur)
                while pegs[current[cur][0]][0] != cur:
                    moving = pegs[current[cur][0]].pop(0)
                    #Should check also for move to goal with check that it is valid
                    for peg in pegs.keys():
                        if pegs[peg] == [] and peg != current[cur][1]:
                            #print('Moving %s from %s to %s'%(moving,current[cur][0],peg))
                            pegs[peg].insert(0,moving)
                            moves.append((current[cur][0],peg))
                            current[moving][0] = peg
                            break
                    else:
                        for peg in pegs.keys():
                            if peg != current[cur][1] and peg != current[cur][0]:
                                if pegs[peg] and pegs[peg][0] > moving:
                                    #print('Moving %s from %s to %s'%(moving,current[cur][0],peg))
                                    pegs[peg].insert(0,moving)
                                    moves.append((current[cur][0],peg))
                                    current[moving][0] = peg
                                    break
                        else:
                            pegs[current[cur][0]].insert(0,moving)
                            #disks.insert(-1,cur)
                            #disks.insert(0,moving)
                            #print('Found no place, moving on')
                disks.append(cur)
                        
        else:
            pass
            #print('%s is in correct plave'%cur)
            
        #print(current)
        #print(pegs)
        
        if disks:
            cur = disks.pop()
        else:
            break
        
    #print('Moves: %s'%str(moves))
    #print('Current:')
    #for loc, discs in pegs.items():
        #print('Location %s has: %s'%(loc, str(discs)))

    print(len(moves))
    for start,end in moves:
        print('%s %s'%(start,end))