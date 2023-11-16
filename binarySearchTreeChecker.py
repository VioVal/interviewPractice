from binarySearchTree import Tree

def checkIfBinarySearchTree(tree):
    lastNode = None
    return recursiveChecker(tree.root, lastNode)

def recursiveChecker(node, lastNode):
    if node == None: return True
    if recursiveChecker(node.left, lastNode) == False: return False
    if lastNode != None:
        if node.data <= lastNode.data: return False
    lastNode = node
    if recursiveChecker(node.right, lastNode) == False: return False
    return True

treeWithRepeats = Tree([2, 4, 7, 8, 9, 9, 10, 12, 15])
binarySearchTree = Tree([2, 4, 7, 8, 9, 10, 12, 15, 16])
allTwos = Tree([2, 2, 2, 2, 2, 2, 2, 2])
binaryTree = Tree([6, 3, 5, 5, 8, 12, 15, 4, 12])
print(checkIfBinarySearchTree(treeWithRepeats))
print(checkIfBinarySearchTree(binarySearchTree))
print(checkIfBinarySearchTree(allTwos))
print(checkIfBinarySearchTree(binaryTree))