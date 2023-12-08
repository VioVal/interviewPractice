class Queens:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def eightQueens(size):
    queenLocations = set()
    counter = 0
    counter = recursiveQueenPlacer(queenLocations, 0, counter, size)
    print(counter)

def queenChecker(queen, queenLocations):
    for queens in queenLocations:
        if queen.x == queens.x or abs(queen.x - queens.x) == abs(queen.y - queens.y):
            return False
    return True

def recursiveQueenPlacer(queenLocations, y, counter, size):
    for i in range(size):
        queen = Queens(i, y)
        if queenChecker(queen, queenLocations) == False:
            continue
        if y == (size - 1):
            counter += 1
            continue
        queenLocations.add(queen)
        counter = recursiveQueenPlacer(queenLocations, y + 1, counter, size)
        queenLocations.discard(queen)

    return counter

eightQueens(8)