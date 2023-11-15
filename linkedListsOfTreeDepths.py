import math
from binarySearchTree import Tree

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

sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tree = Tree(sortedArray)

depth = math.log(len(sortedArray), 2) + 1

arrayOfLinkedLists = ArrayOfLinkedLists(tree, int(depth))
arrayOfLinkedLists.printLinkedLists()