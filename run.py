from random import randint
class Board:
    """
    This class will hold all the attributes of the board for the user and the computer
    """

    def __init__(self, size, ships, name, type):
        self.size = size
        self.ships = []
        self.name = name
        self.guesses = []
        self.type = type
        self.board = [['.' for x in range(5)] for y in range(5)]

    def showBoard(self):
        for row in self.board:
            print(" ".join(row))


test = Board(5, 4, 'User', 7)
test.showBoard()