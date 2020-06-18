from random import randint,seed
seed(randint(0,10))
def connect4():
    print("To get the full experience use terminal")
    board=[]
    for i in range(6):
        board.append([0,0,0,0,0,0])
        print(board[i])
    print("You will be playing with the computer")
    def printBoard():
        class bcolors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
        for i in board:
            for j in i:
                if j =="X":
                    print(bcolors.OKBLUE,end="")
                if j =="Y":
                    print(bcolors.OKGREEN,end="")
                print(j , " ",end="")
                print(bcolors.ENDC,end="")
            print("\n",end="")
    def checkIfFree(a):
        if(board[0][a]==0):
            return 1
        print("This position is not free. Your oponent's turn beacause you gave invalid position")
        return 0
    def askForMove():
        play=int(input("select your next move (1-6):"))-1
        while play>5 or play<0:
            play=int(input("select your next move (1-6):"))-1
        return play
    printBoard()
    def checkIfBoardIsFull():
        for i in range(6):
            if board[0][i]==0:
                return 0
        return 1
    def checkIfWin():
        for i in range(6):
            for k in range(3):
                if board[i][0+k]!=0 and board[i][0+k]==board[i][1+k] and board[i][1+k]==board[i][2+k] and board[i][2+k]==board[i][3+k]:
                    return 1
                if board[0+k][i]!=0 and board[0+k][i]==board[1+k][i] and board[1+k][i]==board[2+k][i] and board[2+k][i]==board[3+k][i]:
                    return 1


    while True:
        play=askForMove()
        if checkIfFree(play):
            check=-1
            while board[check][play]!=0:
                check=check-1
            board[check][play]="X"
        while True:
            enemyTurn=randint(0,5)
            if board[0][enemyTurn]==0:
                check=-1
                while board[check][enemyTurn]!=0:
                    check=check-1
                board[check][enemyTurn]="Y"
                break
        if checkIfWin():
            print('\033[93m',"There is a winner",'\033[0m')
        if checkIfBoardIsFull():
            print('\033[93m',"The board is full",'\033[0m')
            printBoard()
            break

        printBoard()
