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

sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tree = Tree(sortedArray)
tree.printTrees()
print("\n\n")
tree.inOrderPrint()
print("\n\n")



class LinkedListHeader:
    def __init__(self):
        self.head = None
        self.tail = None

class Link:
    def __init__(self, data):
        self.data = data
        self.next = None

def addLink(node, array, depth):
    link = Link(node.data)

    if array[depth].tail == None:
        array[depth].head = link
        array[depth].tail = link
    else:
        array[depth].tail.next = link
        array[depth].tail = link

def createLists(node, array, depth):
    if node == None: return None
    depth += 1
    createLists(node.left, array, depth)
    addLink(node, array, depth)
    createLists(node.right, array, depth)

def createLinkedListForEachDepth(root, depthOfTrees):
    array = []
    for i in range(0, depthOfTrees):
        array.append(LinkedListHeader())

    createLists(root, array, -1)

    return array

class ArrayOfLinkedLists:
    def __init__(self, tree, depth):
        self.array = createLinkedListForEachDepth(tree.root, depth)

    def printLinkedLists(self):
        for i in self.array:
            node = i.head
            while node!= None:
                print(node.data)
                node = node.next
            print("\n")

depth = math.log(len(sortedArray), 2) + 1

arrayOfLinkedLists = ArrayOfLinkedLists(tree, int(depth))
arrayOfLinkedLists.printLinkedLists()