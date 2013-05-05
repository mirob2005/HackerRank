if __name__ == '__main__':
    N = int(input())
    
    AP = []
    
    for ap in range(N):
        AP.append([int(x) for x in input().split(' ')])
    
    
    Q = int(input())
    
    for op in range(Q):
        operation = [int(x) for x in input().split(' ')]
        
        if operation[0] == 0:
            #Query
            seqs = []
            index = operation[1] - 1
            while index < operation[2]:
                seqs.append([pow((AP[index][0]+x*AP[index][1]),AP[index][2]) for x in range(5)])
                index += 1

            product = [1,1,1,1,1]
            for seq in seqs:
                for index,element in enumerate(seq):
                    product[index] *= element
            
            k = 0
            difference = product[:]
            while len(set(difference)) != 1:
                for index,element in enumerate(difference[1:]):
                    difference[index] = element - difference[index]
                difference.pop()
                k += 1
            print('%s %s'%(k,difference[0]%1000003))
        else:
            #Update
            index = operation[1] - 1
            while index < operation[2]:
                AP[index][2] += operation[3]
                index += 1