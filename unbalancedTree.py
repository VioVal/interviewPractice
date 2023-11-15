def makeNode(array, counter):
    counter += 1
    if counter >= len(array): return None
    node = Node(array[counter])
    node.right = makeNode(array, counter)
    return node

def buildTree(array):
    counter = -1
    root = makeNode(array, counter)
    return root

def printTrees(root):
    queue = [root]

    while len(queue) > 0:
        temp = queue[0]
        queue.pop(0)
        print(temp.data)
        if temp.left != None: queue.append(temp.left)
        if temp.right != None: queue.append(temp.right)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class UnbalancedTree:
    def __init__(self, array):
        self.root = buildTree(array)

    def printTrees(self):
        printTrees(self.root)