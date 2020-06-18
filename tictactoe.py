def tictactoe():
    board=[[0,0,0],[0,0,0],[0,0,0]]
    def printBoard(b):
        for i in b:
            print(i)

    def takeAndCheckInput(current):
        place=list(map(lambda a:int(a),input().split()))
        if len(place)!=2 :
            print("Only to nubers between 1 and 3 are required.", len(place),"we given.")
            return 0
        if board[place[1]-1][place[0]-1]!=0 :
            print("This posotion is already taken.")
            return 0
        else:
             board[place[1]-1][place[0]-1]=current
             return 1;
        return 1;

    def checkIfWin():
        for i in range(3):
            if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0] in ["X","Y"]:
                print("\nPLAYER",board[i][0],"WINS")
                return 1
            if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i] in ["X","Y"]:
                print("player",board[0][i],"wins")
                return 1
            if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0] in ["X","Y"]:
                print("player",board[0][0],"wins")
                return 1
            if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0] in ["X","Y"]:
                print("player",board[0][2],"wins")
                return 1
        return 0
    def checkIfFull():
        for i in board:
            for j in i:
                if j==0:
                    return 0
        return 1
    printBoard(board)
    i=0
    while(True):
        players=["X","Y"]
        nowPlaying=players[i%2]
        print("\nNow",nowPlaying,"is playing")
        if takeAndCheckInput(nowPlaying):
            i=i+1
        if checkIfWin():
            break
        if checkIfFull():
            printBoard(board)
            print("The board is full. There is no winner.")
            break
        printBoard(board)
