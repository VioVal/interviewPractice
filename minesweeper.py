import random
from enum import Enum

class Tile:
    def __init__(self, position):
        self.mine = False
        self.closeBombsCounter = 0
        self.isClicked = False
        self.position = position

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Difficulty:
    def __init__(self, difficulty):
        self.size = self.selectSize(difficulty)
        self.numberOfMines = self.selectNumberOfMines(difficulty)

    def selectSize(difficulty):
        if difficulty == DifficultyEnum.EASY: return 10
        if difficulty == DifficultyEnum.MEDIUM: return 15
        if difficulty == DifficultyEnum.HARD: return 20

    def selectNumberOfMines(difficulty):
        if difficulty == DifficultyEnum.EASY: return 10
        if difficulty == DifficultyEnum.MEDIUM: return 40
        if difficulty == DifficultyEnum.HARD: return 99

class DifficultyEnum(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Board:
    def __init__(self, difficulty):
        self.difficulty = Difficulty(difficulty)
        self.tiles = self.createEmptyBoard(self)
        self.placeMines(self)
        self.shuffleTiles(self)
        self.initialiseCloseBombCounter(self)

    def createEmptyBoard(self):
        tiles = [[Tile(i, j) for j in range(self.difficulty.size)] for i in range(self.difficulty.size)]
        return tiles
    
    def placeMines(self):
        numberOfMines = self.difficulty.numberOfMines
        for i in range(self.difficulty.size):
            for j in range(self.difficulty.size):
                self.tiles[i][j].mine = True
                numberOfMines -= 1
                if(numberOfMines == 0): return

    def shuffleTiles(self):
        numberOfShuffles = self.difficulty.numberOfMines
        for i in range(self.difficulty.size):
            for j in range(self.difficulty.size):
                x = random.randint(self.difficulty.size)
                y = random.randint(self.difficulty.size)
                if self.tiles[x][y].mine == False:
                    self.tiles[x][y].mine = True
                    self.tiles[i][j].mine = False
                numberOfShuffles -= 1
                if numberOfShuffles == 0: return

    def checkAdjacent(self, tile):
        noOfMines = 0
        noOfMines += self.isBomb(Position(tile.position.x - 1,tile.position.y - 1))
        noOfMines += self.isBomb(Position(tile.position.x, tile.position.y - 1))
        noOfMines += self.isBomb(Position(tile.position.x + 1, tile.position.y - 1))
        noOfMines += self.isBomb(Position(tile.position.x - 1, tile.position.y))
        noOfMines += self.isBomb(Position(tile.position.x + 1, tile.position.y - 1))
        noOfMines += self.isBomb(Position(tile.position.x - 1, tile.position.y + 1))
        noOfMines += self.isBomb(Position(tile.position.x, tile.position.y + 1))
        noOfMines += self.isBomb(Position(tile.position.x + 1, tile.position.y + 1))

    def isBomb(self, position):
        if(position.x >= 0 and position.x < self.difficulty.selectSize and position.y >= 0 and position.y < self.difficulty.selectSize):
            if(self.titles[position.x][position.y].mine == True):
                return 1
        return 0
    
    def initialiseCloseBombCounter(self):
        for i in range(self.difficulty.size):
            for j in range(self.difficulty.size):
                if(self.tiles[i][j].mine == False):
                    self.tiles[i][j].closeBombsCounter = self.checkAdjacent(self, self.tiles[i][j])

    def chooseTile(self, position):
        if(self.tiles[position.x][position.y].isClicked == False):
            if(self.tiles[position.x][position.y].mine == True):
                self.failure()
            self.tiles[position.x][position.y].isClicked == True
            if(self.tiles[position.x][position.y].closeBombsCounter == 0):
                self.flipTiles()

    def flipTiles():
        pass

    def success():
        print("Winner")

    def failure():
        print("BANG")