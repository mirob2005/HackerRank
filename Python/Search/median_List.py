n = int(input().strip())

nl = []

for op in range(n):
    operation = input().split(' ')
    if operation[0] == 'a':
        nl.append(int(operation[1]))
    else:
        if int(operation[1]) in nl:
            nl.remove(int(operation[1]))
        else:
            print('Wrong!')
            continue
    
    length = len(nl)
    if length == 0:
        print('Wrong!')
    else:
        nl.sort()

        if length%2 ==1:
            index = length//2
            median = nl[index]
        else:
            index1 = length//2 -1
            index2 = length//2
            median = (nl[index1]+nl[index2])/2
        if int(median) == median:
            print(int(median))
        else:
            print(median)