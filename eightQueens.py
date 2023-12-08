class Queens:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def eightQueens():
    queenLocations = set()
    counter = 0
    counter = recursiveQueenPlacer(queenLocations, 0, counter)
    print(counter)

def queenChecker(queen, queenLocations):
    for queens in queenLocations:
        if queen.x == queens.x or abs(queen.x - queens.x) == abs(queen.y - queens.y):
            return False
    return True

def recursiveQueenPlacer(queenLocations, y, counter):
    for i in range(8):
        queen = Queens(i, y)
        if queenChecker(queen, queenLocations) == False:
            continue
        if y == 7:
            counter += 1
            continue
        queenLocations.add(queen)
        counter = recursiveQueenPlacer(queenLocations, y + 1, counter)
        queenLocations.discard(queen)

    return counter

eightQueens()