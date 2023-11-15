import math

def createNodes(array, start, end):
    if end < start: return None

    mid = math.ceil((start + end)/2)
    node = Node(array[mid])
    node.left = createNodes(array, start, mid - 1)
    node.right = createNodes(array, mid + 1, end)
    return node

def createTree(sortedArray):
    if len(sortedArray) == 0: return None
    root = createNodes(sortedArray, 0, len(sortedArray) - 1)
    return root

def printTrees(root):
    queue = [root]

    while len(queue) > 0:
        temp = queue[0]
        queue.pop(0)
        print(temp.data)
        if temp.left != None: queue.append(temp.left)
        if temp.right != None: queue.append(temp.right)

def inOrderPrint(node):
    if node != None:
        inOrderPrint(node.left)
        print(node.data)
        inOrderPrint(node.right)

class Tree:
    def __init__(self, sortedArray):
        self.root = createTree(sortedArray)

    def printTrees(self):
        printTrees(self.root)

    def inOrderPrint(self):
        inOrderPrint(self.root)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data