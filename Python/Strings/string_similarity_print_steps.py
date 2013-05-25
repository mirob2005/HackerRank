# Z Algorithm
# Followed demo from:
# http://www.utdallas.edu/~besp/demo/John2010/z-algorithm.htm
# to implement

import time

if __name__ == '__main__':
    N = int(input())
    s = time.clock()
    
    for line in range(N):
        string = input()
        
        length = len(string)
        total = length

        compare = 0
        z = [0]
        l = 0
        r = 0

        for k in range(1,length):
            print('\nEvaluating %s'%k)
            if k > r:
                print('Compute Explicitly')
                match=0
                index = k
                while index < length:
                    print('Comparing %s and %s'%(string[index],string[match]))
                    if string[index] == string[match]:
                        match +=1
                        index +=1
                        compare+=1
                    else:
                        compare+=1
                        break
                z.append(match)
                if match > 0:
                    total+=match
                    l = k
                    r = index-1
            else:
                print('Previously Discovered Substring')
                if z[k-l] < (r-k)+1:
                    print('No Additional comparisons needed')
                    z.append(z[k-l])
                    total+=z[k-l]
                else:
                    print('Extended substring')
                    match = r-k
                    index = r
                    while index < length:
                        print('Comparing %s and %s'%(string[index],string[match]))
                        if string[index] == string[match]:
                            match +=1
                            index +=1
                            compare+=1
                        else:
                            compare+=1
                            break
                    z.append(match)
                    total+=match
                    l = k
                    r = index-1
            print('%s compares so far'%compare)
        
            print('z: %s'%str(z))
            print('l: %s'%l)
            print('r: %s'%r)
        print('----------------')
        print('Total matches %s'%total)
        print('Total comparsions: %s'%(compare))
        print(total)
            
    f = time.clock()
    totalTime = f-s
    print(totalTime)