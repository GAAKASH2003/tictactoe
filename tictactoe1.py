import random
def display(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])
    
def playerin():
    marker=" "
    while not (marker=='X' or marker=='O'):
        marker=input("enter X or O:").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def place(board,mark,plac):
    board[plac]=mark
    
def iswin(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark)) 
def choosefir():
    if(random.randint(0,1)==0):
        return 'Player 1'    
    else:
        return 'Player 2'
    
def space_check(board,pos):
    if(board[pos]==' '):
        return True
    else:
        return False
    
def fullb(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
        
def readin(board):
    pos=0
    while pos not in range(1,10) or not  space_check(board,pos):
        pos=int(input("enter the numbers in the range 1 to 10:"))
    return pos 
def replay():
    return input("do you want to replay say yes or no?")[0]=='y'

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = playerin()
    turn = choosefir()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display(theBoard)
            position = readin(theBoard)
            place(theBoard, player1_marker, position)

            if iswin(theBoard, player1_marker):
                display(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if fullb(theBoard):
                    display(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display(theBoard)
            position = readin(theBoard)
            place(theBoard, player2_marker, position)

            if iswin(theBoard, player2_marker):
                display(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if fullb(theBoard):
                    display(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
       
        
        
        