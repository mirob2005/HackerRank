
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
        self.last = 0
        # True = Even, False = Odd
        self.parity = True

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
        
        self.computeMedian()

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
                    ptr.deleteNode()
                elif ptr.right == None:
                    ptr.left.parent = ptr.parent
                    if ptr == self.root:
                        self.root = ptr.left
                    elif ptr.isLeftChild():
                        ptr.parent.left = ptr.left
                    else:
                        ptr.parent.right = ptr.left
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

        self.computeMedian()
        
    
    def computeMedian(self):
        self.traverseTree(self.root)

    def traverseTree(self,root,count=1):
        if root.left:
            count = self.traverseTree(root.left,count)
        for i in range(root.count):
            if count == (self.count//2 + 1):
                if self.parity:
                    median = (self.last + root.number)/2
                    if median == int(median):
                        print(int(median))
                        #return None,None
                    else:
                        print(median)
                        #return None,None
                else:
                    print(root.number)
                    #return None,None
            count += 1
            self.last = root.number
        if root.right:
            count= self.traverseTree(root.right,count)
        return count


if __name__ == '__main__':
    n = int(input().strip())
    
    tree = BST()
    
    for op in range(n):
        operation = input().split(' ')
        if operation[0] == 'a':
            tree.addNode(int(operation[1]))
        else:
            tree.removeNode(int(operation[1]))
    