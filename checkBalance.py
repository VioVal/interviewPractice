from binarySearchTree import Tree
from unbalancedTree import UnbalancedTree

def recursiveChecker(node, depth, array):
    if node == None:
        array.append(depth)
        return

    depth += 1
    recursiveChecker(node.left, depth, array)
    recursiveChecker(node.right, depth, array)

def checkBalance(tree):
    node = tree.root

    depth = 0
    array = []

    recursiveChecker(node, depth, array)

    if max(array) - min(array) > 1:
        print("Unbalanced")
    else:
        print("Balanced")

tree = Tree([2, 5, 6, 8, 9])
checkBalance(tree)

unbalancedTree = UnbalancedTree([2, 5, 6, 8, 9])
checkBalance(unbalancedTree)