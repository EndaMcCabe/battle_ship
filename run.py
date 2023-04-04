# from random import randint
class Board:
    """
    This class will hold all the attributes of the board for the user and the computer
    """

    def __init__(self, size, num, name, user):
        self.size = size
        self.num = num
        self.ships = []
        self.name = name
        self.guesses = []
        self.user = user
        self.board = [['.' for x in range(size)] for y in range(size)]

    def showBoard(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = 'X'

        if (x, y) in self.ships:
            self.board[x][y] = 'x'
            return 'Hit'
        else:
            return "Miss"
    
    def add_ship(self, x, y, user):
        if len(self.ships) >= self.ships:
            pass
        else:
            self.ships.append((x, y))
            if self.user == 'User':
                self.board[x][y] = "O"


def play_game():
    size = 5
    num = 3
    user_board = Board(size, num, 'User', "user")
    print(user_board.board)

play_game()