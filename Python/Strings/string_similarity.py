def prefix(string,substring):
    total = 0
    for char1,char2 in zip(string,substring):
        if char1 == char2:
            total+=1
        else:
            return total
    return total

if __name__ == '__main__':
    N = int(input())
    
    for test in range(N):
        string = input()
        
        total = 0
        
        start = 0
        while start < len(string):
            total += prefix(string,string[start:])
            start+=1

        print(total)