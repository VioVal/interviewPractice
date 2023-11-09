graph = {
    'a': ['b', 'c'],
    'b': ['c', 'a'],
    'c': ['d', 'e'],
    'd': [],
    'e': ['f'],
    'f': ['g', 'h'],
    'g': ['h'],
    'h': []
    }

def pathFinder(graph, start, end):
    currentNode = start
    stack = [currentNode]
    traversedNodes = set()

    if start == end: return True

    while(len(stack) > 0):
        stack.pop(len(stack)-1)
        traversedNodes.add(currentNode)

        for nodes in graph[currentNode]:
            if nodes not in traversedNodes: stack.insert(0, nodes)

        if len(stack) > 0: currentNode = stack[len(stack)-1]
        if(currentNode == end):
            return True
        
    return False

result = pathFinder(graph, 'c', 'c')
if(result == True): print("success")
else: print("Failure")