import games as games
import basic as basic
listOfGames={
    "TICTACTOE":games.tictactoe,
    "CONNECT4":games.connect4,
}

basic.printIntro()
game=str(input("Your game is: "))
listOfGames[game.upper()]()
