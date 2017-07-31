#Tic Tac Toe Skeleton

# FUNCTIONS
def draw_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def winning(board, combinations):
    count = 0
    for a in combinations:
        if board[a[0]] == board[a[1]] == board[a[2]] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True

        if board[a[0]] == board[a[1]] == board[a[2]] == "O":
            print("Player 2 Wins!\n")
            print("Congratulations!\n")
            return True
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            count += 1
        if count == 9:
            print("The game ends in a Tie\n")
            return True

# MAIN PROGRAM
board = ['_'] * 9
playing = True
win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

while playing == True:
    draw_board(board)

    # get player 1 input
    #set the right spot in the board

    # get player 2 input
    # set the right spot in the board

    #check for the end

    # if the end is reached ask people if they want to play again!
    playing = False
