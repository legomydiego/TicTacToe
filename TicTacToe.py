test_board = ['#','X','O','X','O','X','O','X','O','X']
board = ['#','','','','','','','','','']
game_on = True
def print_board():
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

def run_game():
    print('Welcome to TicTacToe')
    print_board()
    while(game_on):
        print('Player One, what is your move?')
        move1 = input('Please select a cell to play')
        check_played(move1,one)
        print('Player Two, what is your move?')
        move2 = input('Please select a cell to play')
        check_played(move2,two)
        game_on=False

def check_winner():
    for row in range(1,10,3):
        if board[row]==board[row+1] and board[row]==board[row+2]:
            if board[row]='X':
                print('Player one wins')
            elif boad[row]='O':
                print('Player two wins')
    for column in range(1,4):
        if board[column]==board[column+3] and board[column]==board[column+6]:
            if board[column]='X':
                print('Player one wins')
            elif boad[column]='O':
                print('Player two wins')

def check_played(move,player):
    if board[move]!='':
        input('Cell has been used, please enter a different one')
    else:
        if player=='one':
            board[move]='X'
        elif player=='two':
            board[move]='O'