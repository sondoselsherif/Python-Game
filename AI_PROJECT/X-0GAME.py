#dictionary
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
#mfunction to print board for each row
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('_____')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('_____')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")
#calling function
printBoard(board)

#function to check is the space is free to detect that the player can play in this position or not
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False
#لو في أي مساحات فاضية يبقى لسه ممكن نلعب, لو مافيش سبقى تعادل
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

#check diagonals, rows and columns to detect if they are the same or not
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

#function to insert letter (X||O)
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Computer wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        #recursion
        insertLetter(letter, position)
        return
#X is Max
#O is min
player = 'O'
computer = 'X'







def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return


def compMove():
    bestScore = -800
    bestMove = 0
    #To make computer the firsr player

    for key in board.keys():
        if (board[key] == ' '):
            board[key] = computer
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(computer, bestMove)
    return

#isMaximizing=> is a bolean value
def minimax(board, depth, isMaximizing):
    #terminate status
    if (checkWhichMarkWon(computer)):
        return 100
    elif (checkWhichMarkWon(player)):
        return -100
    elif (checkDraw()):
        return 0
#This is computer bot
    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = computer
                # Maximizing moment
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
 ##This is enemy bot
#we take the high score becuase we need the minimum score
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                # Miniimizing moment
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore




#print("Computer goes first! Good luck.")
#print("Positions are as follow:")
#print("1, 2, 3 ")
#print("4, 5, 6 ")
#print("7, 8, 9 ")
#print("\n")



global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()
