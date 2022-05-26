#THIS IS GOING TO BE IT!

def print_board(board):
    print(board[1]," | " , board[2], " | " , board[3])
    print(board[4] , " | " , board[5] , " | " , board[6])
    print(board[7] , " | " , board[8] , " | " , board[9])

def enter_pos(board, playerpos, seeifplayer):
    if seeifplayer == 1:
        for i in board:
            if i == int(playerpos):
                board[i] = 'X'
                break
        else:
            print("this is already taken,chose another location.")

    else:
        for i in board:
            if i == int(playerpos):
                board[i] = 'O'
                break
        else:
            print("this is already taken,chose another location.")

def check_if_win(board):
    if board[1] == board[4] and board[1] == board[7]:
        return True
    if board[2] == board[5] and board[2] == board[8]:
        return True
    if board[3] == board[6] and board[3] == board[9]:
        return True
    if board[1] == board[5] and board[1] == board[9]:
        return True
    if board[3] == board[5] and board[3] == board[7]:
        return True
    if board[1] == board[2] and board[1] == board[3]:
        return True
    if board[4] == board[5] and board[4] == board[6]:
        return True
    if board[7] == board[8] and board[7] == board[9]:
        return True
    return False

print("Welcome to Tic Tac Toe Game!!")
print("Are you ready to play? enter YES or NO")
ready = input()
while ready.lower() == 'yes':
    #Chosing what player 1 will be - X or O
    print("Player 1 - What would you like to be X or O?")
    player1 = input().upper()
    while player1.lower() != 'x' and player1.lower() != 'o':
        player1 = input("Player 1 - Please try again entring X or O").upper()
    if player1.lower() == 'x':
        player2 = 'O'
    else:
        player2 = 'X'
        player1 = 'O'
    print("Player 1 is: " + player1 + " and Player 2 is: " + player2)
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    gamecount = 0
    seeifplayer = 1

    while gamecount < 10:
        print("This is the postions of the game:")
        print_board(board)
        if seeifplayer == 1:
            print("Player 1 your turn:")
        else:
            print("Player 2 your turn:")
        print("Enter the postion you want")
        playerpos = input()
        #checking to see if the input is correct
        while playerpos.isdigit() == False:
            print("Please re-enter the postion you want")
            playerpos = input()

        # Entering the postion on the board
        enter_pos(board, playerpos, seeifplayer)
        if check_if_win(board) == True:
            if seeifplayer == 1:
                print("Player 1 WINS!")
                break
            else:
                print("Player 2 WINS!")
                break
        # Who turn is it?
        if seeifplayer == 1:
            seeifplayer = 2
        else:
            seeifplayer = 1

        #Check to see if its a tie
        gamecount = gamecount + 1
        if gamecount == 9:
            print("Its a TIE!")
            break

    print("Are you ready to play again? enter YES or NO")
    ready = input()


print("Thank you!")
