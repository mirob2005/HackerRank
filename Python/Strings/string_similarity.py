# Z Algorithm
# Followed demo from:
# http://www.utdallas.edu/~besp/demo/John2010/z-algorithm.htm
# to implement

if __name__ == '__main__':
    N = int(input())
    
    for line in range(N):
        string = input()
        
        length = len(string)
        total = length

        z = [0]
        l = 0
        r = 0

        for k in range(1,length):
            if k > r:
                match=0
                index = k
                while index < length:
                    if string[index] == string[match]:
                        match +=1
                        index +=1
                    else:
                        break
                z.append(match)
                if match > 0:
                    total+=match
                    l = k
                    r = index-1
            else:
                if z[k-l] < (r-k)+1:
                    z.append(z[k-l])
                    total+=z[k-l]
                else:
                    match = r-k
                    index = r
                    while index < length:
                        if string[index] == string[match]:
                            match +=1
                            index +=1
                        else:
                            break
                    z.append(match)
                    total+=match
                    l = k
                    r = index-1
        print(total)