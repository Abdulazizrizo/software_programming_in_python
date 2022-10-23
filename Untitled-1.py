
def getBlankBoard():
    """Create a new, blank TicTacToe"""
    # Map of Position numbers: 1|2|3
    #                       -+-+-
    #                       4|5|6
    #                       -+-+-
    #                       7|8|9
    # Points are 1 to 9, the values you can enter are X, O, or BLANK:
    TicTacBoard = {}
    for Position in All_Positions:
        TicTacBoard[Position] = BLANK  # All spaces start as bl
    return TicTacBoard


def getBoardStr(TicTacBoard):
    """returns a text format of the game"""
    return '''
       {}|{}|{}  1 2 3
       -+-+-
       {}|{}|{}  4 5 6
       -+-+-
       {}|{}|{}  7 8 9'''.format(TicTacBoard['1'], TicTacBoard['2'], TicTacBoard['3'],
                                 TicTacBoard['4'], TicTacBoard['5'], TicTacBoard['6'],
                                 TicTacBoard['7'], TicTacBoard['8'], TicTacBoard['9'])


def isValidSpace(TicTacBoard, Position):
    """True if the Position on the TicTactoeBoard is a valid Position number
    and the Position is blank"""
    return Position in All_Positions and TicTacBoard[Position] == BLANK


def isWinner(TicTacBoard, player):
    """Return True if player is a winner on this TTTBoard"""
    # variable names used here to make it readable:
    b, p = TicTacBoard, player
    # Check for 3 marks 3 rows, 3 columns, and 2 diagon
    return ((b['1'] == b['2'] == b['3'] == p) or  # if crosses the top
            (b['4'] == b['5'] == b['6'] == p) or  # if crosses themiddle
            (b['7'] == b['8'] == b['9'] == p) or  # if crosses thebottom
            (b['1'] == b['4'] == b['7'] == p) or  # Down left
            (b['2'] == b['5'] == b['8'] == p) or  # Down middle
            (b['3'] == b['6'] == b['9'] == p) or  # Down right
            (b['3'] == b['5'] == b['7'] == p) or  # Diagonally
            (b['1'] == b['5'] == b['9'] == p))    # Diagonally


def isBoardFull(TicTacBoard):
    """Return True if every Position on the TicTacBoard has been ta"""
    for Position in All_Positions:
        if TicTacBoard[Position] == BLANK:
            return False
    return True


def updateBoard(TicTacBoard, Position, mark):
    """Define the Position on the TicTacBoard to mark"""
    TicTacBoard[Position] = mark


All_Positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

X, O, BLANK = 'X', 'O', ' '  # Constants for values.


def main():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        # Shows TicTactoeBoard on the Display:
        print(getBoardStr(gameBoard))

        # Keep asking the player they not enter 1 - 9:
        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)

        # Check if the game is ended:
        if isWinner(gameBoard, currentPlayer):  # Check for a win
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):  # Checks for a tie
            print(getBoardStr(gameBoard))
            print('Draw!')
            break
        # Player turns
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')


if __name__ == '__main__':
    main()

    
    https://youtu.be/57f68HeDw24
