import random
import re

#Print board function
def printBoard(board):
    for i in range(height):
        for j in range(width):
            print(board[i][j], end = "")
        print()

#Gameplay function
def gameplay(board):
    #Make copy of board, with borders added (+2 to each dimension)
    gridStatus = [[0] * (width + 2) for i in range(height + 2)]
    for i in range(height):
        for j in range(width):
            gridStatus[i + 1][j + 1] = board[i][j]
    #Begin checking rules
    for i in range(height):
        for j in range(width):
            #Count number of surrounding lives
            count = 0
            for k in [i - 1, i, i + 1]:
                for l in [j - 1, j, j + 1]:
                    if gridStatus[k + 1][l + 1] == 1:
                        count += 1
            #Rule 1: Loneliness leads to death (<2 others)
            if count < 3:
                board[i][j] = 0
            #Rule 2: Crowdedness also leads to death (>3 others)
            elif count > 4:
                board[i][j] = 0
            #Rule 3: Surrounding lives can reproduce (Exactly 3 others)
            elif count == 3:
                board[i][j] = 1

#Random spawn function
def randomSpawn(numSpawn):
    for i in range(numSpawn):
        row = random.randint(0, height - 1)
        col = random.randint(0, width - 1)
        #Prevent double spawn
        while gameBoard[row][col] == 1:
            row = random.randint(0, height - 1)
            col = random.randint(0, width - 1)
        gameBoard[row][col] = 1
        print("Life spawned at " + str(row) + "," + str(col))

#Asks user for board dimensions
print("Please enter board height:")
while True:
    try:
        height = int(input())
        break
    except:
        print("Please enter an integer:")
print("Please enter board width:")
while True:
    try:
        width = int(input())
        break
    except:
        print("Please enter an integer:")

#Generate game board
gameBoard = [[0] * width for i in range(height)]

#Asks user for starting scenario
print("Enter coordinates to spawn a life using format: \"x,y\". ", end = "")
print("To spawn randomly, enter \"random\". When done, enter \"done\".")
while True:
    coords = input()
    if coords == "done":
        break
    elif coords == "random":
        print("Please enter number of lives to spawn.")
        userSpawnNum = int(input())
        randomSpawn(userSpawnNum)
        break
    #Check for input validity using regex
    elif re.search("\d+,\d+", coords):
        splitCoords = coords.split(",")
        x, y = splitCoords
        x = int(x)
        y = int(y)
        gameBoard[y - 1][x - 1] = 1
        print("Life spawned at " + coords)
    else:
        print("Enter coordinates to spawn a life using format: \"x,y\". ", end = "")
        print("To spawn randomly, enter \"random\". When done, enter \"done\".")

#Show starting game baord
print("This is your starting board:")
printBoard(gameBoard)

#Gameplay
totalTurns = 0
while True:
    print("Please enter number of turns. To quit, enter \"quit\"")
    turns = ""
    turns = input()
    if turns == "":
        gameplay(gameBoard)
        totalTurns += 1
        print("Board after " + str(totalTurns) + " turns:")
        printBoard(gameBoard)
        continue
    elif turns == "quit":
        break
    turns = int(turns)
    totalTurns += turns
    for i in range(turns):
        gameplay(gameBoard)
    print("Board after " + str(totalTurns) + " turns:")
    printBoard(gameBoard)
