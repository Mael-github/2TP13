class Node:
    def __init__(self,val,left,right):
        self.__val = val
        self.__right = right
        self.__left = left

    def getVal(self):
        return self.__val

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def setRight(self,node):
        self.__right = node

    def setLeft(self,node):
        self.__left = node


node1 = Node(2,None,None)
node2 = Node(8,None,None)
node3 = Node(5,node1,node2)
print(node3.getLeft().getVal())
