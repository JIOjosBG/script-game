from random import randint,seed
seed(randint(0,10))
def connect4():
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

    printBoard()
