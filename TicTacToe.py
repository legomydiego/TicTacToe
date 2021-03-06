test_board = ['#','X','O','X','O','X','O','X','O','X']
board = ['#','','','','','','','','','']

def print_board():
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

def run_game():
    game_on = True
    print('Welcome to TicTacToe')
    while(game_on):
        print_board()
        print('Player One, what is your move?')
        move1 = int(input('Please select a cell to play'))
        check_played(move1,'one')
        if check_winner()==False:
            break
        print_board()
        print('Player Two, what is your move?')
        move2 = int(input('Please select a cell to play'))
        check_played(move2,'two')
        game_on = check_winner()

def check_winner():
    #check for winner by row
    for row in range(1,10,3):
        if board[row]==board[row+1] and board[row]==board[row+2] and board[row]!='':
            if board[row]=='X':
                print('Player one wins')
            elif board[row]=='O':
                print('Player two wins')
            return False
    #check for winner by column
    for column in range(1,4):
        if board[column]==board[column+3] and board[column]==board[column+6] and board[column]!='':
            if board[column]=='X':
                print('Player one wins')
            elif board[column]=='O':
                print('Player two wins')
            return False
    #check diagonal winner
    if board[1]==board[5] and board[1]==board[9] and board[1]!='':
        if board[1]=='X':
                print('Player one wins')
        elif board[1]=='O':
                print('Player two wins')
        return False
    if board[3]==board[5] and board[3]==board[7] and board[3]!='':
        if board[3]=='X':
                print('Player one wins')
        elif board[3]=='O':
                print('Player two wins')
        return False
    return True

def check_played(move,player):
    while board[move]!='':
        move = int(input('Cell has been used, please enter a different one'))
        
    if player=='one':
        board[move]='X'
    elif player=='two':
        board[move]='O'

run_game()