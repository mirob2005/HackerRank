class NumberList:
    def __init__(self):
        self.numbers = []
        self.count = 0
    def addNumber(self,number):
        if not self.numbers:
            self.numbers.append(number)
        else:
            index = self.count//2
            compare = self.numbers[index]
            if number > compare:
                while index < self.count-1 and number > compare:
                    index +=1
                    compare = self.numbers[index]
                else:
                    self.numbers.insert(index,number)
            elif number < compare:
                while index >= 0 and number < compare:
                    index -=1
                    compare = self.numbers[index]
                else:
                    self.numbers.insert(index+1,number)
            else:
                self.numbers.insert(index,number)
        self.count += 1
        self.printMedian()
    
    def removeNumber(self,number):
        if not self.numbers:
            print('Wrong!')
            return
        else:
            index = self.count//2
            compare = self.numbers[index]
            if number > compare:
                while index < self.count-1 and number > compare:
                    index +=1
                    compare = self.numbers[index]
                else:
                    if number == compare:
                        self.numbers.pop(index)
                    else:
                        print('Wrong!')
                        return
            elif number < compare:
                while index >= 0 and number < compare:
                    index -=1
                    compare = self.numbers[index]
                else:
                    if number == compare:
                        self.numbers.pop(index)
                    else:
                        print('Wrong!')
                        return
            else:
                self.numbers.pop(index)
        self.count -= 1
        self.printMedian()

    def printMedian(self):
        if not self.numbers:
            print('Wrong!')
            return
        if self.count % 2 == 1:
            print(self.numbers[self.count//2])
        else:
            median = (self.numbers[self.count//2] + self.numbers[(self.count//2)-1])/2
            if int(median) == median:
                print(int(median))
            else:
                print(median)

if __name__ == '__main__':
    n = int(input().strip())
    
    nl = NumberList()
    
    for op in range(n):
        operation = input().split(' ')
        if operation[0] == 'a':
            nl.addNumber(int(operation[1]))
        else:
            nl.removeNumber(int(operation[1]))