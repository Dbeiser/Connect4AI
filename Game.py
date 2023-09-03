
letters = ["A", "B", "C", "D", "E", "F", "G"]

board = [["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""]]
rows = 6
columns = 7

def printboard():
    print("\n      A    B    C    D    E    F    G ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(columns):
            if (board[x][y] == "🔵"):
                print("", board[x][y], end=" |")
            elif (board[x][y] == "🔴"):
                print("", board[x][y], end=" |")
            else:
                print(" ", board[x][y], end="  |")

    print("\n   +----+----+----+----+----+----+----+")


printboard()