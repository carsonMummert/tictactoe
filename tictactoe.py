import time

# 0 1 2
# 3 4 5
# 6 7 8

# a1 a2 b2 a3 b3 b1 c1 c3 c2

board = [" "," "," "," "," "," "," "," "," "]
sets =  [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
indexValues = [3, 2, 3, 2, 4, 2, 3, 2, 3]

def printBoard():
    cols = "  1   2   3 "
    row1 = "A " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2])
    row2 = "B " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5])
    row3 = "C " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8])
    filler = "  ---------"
    print(cols + "\n" + row1 + "\n" + filler + "\n" + row2 + "\n" + filler + "\n" + row3)

def clearBoard():
    for space in board:
        space = " "

def turn(piece):
    print("Select next piece pos.\n(Ex: 'A1', 'c2', etc.):")
    next_pos = input()
    valid = False
    while not valid:
        if len(next_pos) == 2:
            row = ord(str.lower(next_pos[0]))
            col = int(next_pos[1]) - 1
            if row >= 97 and row <= 99:
                if col >= 0 and col <= 2:
                    switcher = {
                        97: (col),
                        98: (col + 3),
                        99: (col + 6)
                    }
                    if board[switcher.get(row)] == ' ':
                        board[switcher.get(row)] = piece
                        valid = True
                    else:
                        print("Invalid, space is already occupied")
                else:
                    print("Invalid column value.")
            else:
                print("Invalid row value.")
        else:
            print("Invalid string length.")
            print("Input must be formatted as follows: \nEx: 'A1', 'c2', etc.")
            next_pos = input()

def aiTurn(piece):
    minimaxScore = [0,0,0,0,0,0,0,0];
    for i in range(8):
        for j in range(3):
            index = sets[i][j]
            if board[index] == 'X':
                minimaxScore[i] -= 1
            elif board[index] == "O":
                minimaxScore[i] += 1
    bestScore = 0
    bestSets = []
    for i in range(8):
        if abs(minimaxScore[i]) > abs(bestScore):
            bestSets = []
            bestSets.append(i)
            bestScore = minimaxScore[i]
        elif abs(minimaxScore[i]) == abs(bestScore):
            bestSets.append(i)
    playedYet = False
    bestScores = [2,-2,1,-1,0]
    for score in bestScores:
        for best in bestSets:
            if minimaxScore[best] == score:
                for spot in sets[best]:
                    if board[spot] == " " and playedYet == False:
                        board[spot] = piece
                        playedYet = True
                        break
                        
def checkWin():
    for set in sets:
        if board[set[0]] != " ":
            if board[set[0]] == board[set[1]] and board[set[1]] == board[set[2]]:
                print("Winner: " + board[set[0]])
                return True
    return False

def checkDraw():
    free = 0
    for space in board:
        if space != "X" and space != "O":
            free += 1
    if free == 0:
        print("Draw!")
        return True
    return False

def pvpGame():
    piece = "X"
    print("Begin game!!")
    printBoard()
    while not checkWin() and not checkDraw():
        print("Player " + piece + " turn:")
        turn(piece)
        printBoard()
        if piece == "X":
            piece = "O"
        else:
            piece = "X"
    clearBoard()

def pveGame():
    piece = "X"
    print("Begin game!! Good luck, weary traveler. The bot will consume all.")
    printBoard()
    while not checkWin() and not checkDraw():
        if piece == "X":
            turn(piece)
        else:
            time.sleep(1)
            aiTurn(piece)
        printBoard()
        if piece == "X":
            piece = "O"
        else:
            piece = "X"
    return False

def main():
    print("PvE (y) or PvP (n)?")
    mode = input()
    if str.lower(mode) == 'y':
        pveGame()
    else:
        pvpGame()

# board2 = ["X", "O", "O", "O", "X", "X", "X", "X", "O"]
# print(checkDraw(board2))
# print()
main()
