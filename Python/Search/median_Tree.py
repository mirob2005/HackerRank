
class Node:
    def __init__(self, number):
        self.number = number
        self.count = 1
        self.left = None
        self.right = None
        self.parent = None
    def isRightChild(self):
        if self.parent:
            return self == self.parent.right
        else:
            return False
    def isLeftChild(self):
        if self.parent:
            return self == self.parent.left
        else:
            return False
    def deleteNode(self):
        self.number = None
        self.count = None
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
        self.median = None
        self.oldMedian = None
        # True = Even, False = Odd
        self.parity = True
        self.medianEdge = 0

    def addNode(self,number):
        if self.root == None:
            self.root = Node(number)
        else:
            ptr = self.root
            while ptr:
                if number > ptr.number:
                    if ptr.right == None:
                        ptr.right = Node(number)
                        ptr.right.parent = ptr
                        break
                    else:
                        ptr = ptr.right
                elif number <ptr.number:
                    if ptr.left == None:
                        ptr.left = Node(number)
                        ptr.left.parent = ptr
                        break
                    else:
                        ptr = ptr.left
                else:
                    #Allow for duplicates values
                    ptr.count += 1
                    break
        self.count += 1
        self.parity = not self.parity
        
        self.computeMedian(True,number)

    def removeNode(self,number):
        if self.root == None:
            print('Wrong!')
            return
        ptr = self.root
        while ptr:
            if number > ptr.number:
                ptr = ptr.right
            elif number < ptr.number:
                ptr = ptr.left
            else:
                #Duplicate Values
                if ptr.count > 1:
                    ptr.count -= 1
                    break
                #Leaf Node
                if ptr.left == None and ptr.right == None:
                    if ptr == self.root:
                        self.root = None
                    elif ptr.isLeftChild():
                        ptr.parent.left = None
                    else:
                        ptr.parent.right = None
                    ptr.deleteNode()
                    break
                if ptr.left == None:
                    ptr.right.parent = ptr.parent
                    if ptr == self.root:
                        self.root = ptr.right
                    elif ptr.isLeftChild():
                        ptr.parent.left = ptr.right
                    else:
                        ptr.parent.right = ptr.right
                    if ptr == self.median:
                        self.median = ptr.right
                    ptr.deleteNode()
                elif ptr.right == None:
                    ptr.left.parent = ptr.parent
                    if ptr == self.root:
                        self.root = ptr.left
                    elif ptr.isLeftChild():
                        ptr.parent.left = ptr.left
                    else:
                        ptr.parent.right = ptr.left
                    if ptr == self.median:
                        self.median = ptr.left
                    ptr.deleteNode()
                else:
                    child = ptr.left
                    while child.right:
                        child = child.right
                    ptr.number = child.number
                    ptr.count = child.count
                    if child.isLeftChild():
                        child.parent.left = None
                    else:
                        child.parent.right = None
                    child.deleteNode()
                break
        else:
            print('Wrong!')
            return
        self.count -= 1
        self.parity = not self.parity
        if self.root == None:
            print('Wrong!')
            return

        self.computeMedian(False,number)
    
    def computeMedian(self,added,number):
        if self.count == 1 or self.count == self.root.count:
            self.median = self.root
            self.oldMedian = self.median.number
            print(self.median.number)
        else:
            if self.parity:
                #Even Number of ints
                if ((number > self.oldMedian and added) or
                    (number < self.oldMedian and not added) or
                    (number == self.oldMedian and not added
                     and self.median.number < number)):
                    if self.median.right:
                        secondMedian = self.median.right.number
                    else:
                        secondMedian = self.median.parent.number
                    self.medianEdge = 1
                    median = (self.median.number+secondMedian)/2
                    self.oldMedian = median
                    if median == int(median):
                        print(int(median))
                    else:
                        print(median)
                elif ((number < self.oldMedian and added) or
                    (number > self.oldMedian and not added) or
                    (number == self.oldMedian and not added
                     and self.median.number > number)):
                    if self.median.left:
                        secondMedian = self.median.left.number
                    else:
                        secondMedian = self.median.parent.number
                    self.medianEdge = -1
                    median = (self.median.number+secondMedian)/2
                    self.oldMedian = median
                    if median == int(median):
                        print(int(median))
                    else:
                        print(median)
                else:
                    print(self.median.number)
                    self.oldMedian = self.median.number
            else:
                #Odd number of ints
                if (number > self.oldMedian and added) or (number < self.oldMedian and not added):
                    if self.medianEdge == 1:
                        if self.median.right:
                            self.median = self.median.right
                        else:
                            self.median = self.median.parent
                elif (number < self.oldMedian and added) or (number > self.oldMedian and not added):
                    if self.medianEdge == -1:
                        if self.median.left:
                            self.median = self.median.left
                        else:
                            self.median = self.median.parent
                self.medianEdge = 0
                print(self.median.number)
                self.oldMedian = self.median.number


if __name__ == '__main__':
    n = int(input().strip())
    
    tree = BST()
    
    for op in range(n):
        operation = input().split(' ')
        if operation[0] == 'a':
            tree.addNode(int(operation[1]))
        else:
            tree.removeNode(int(operation[1]))
    