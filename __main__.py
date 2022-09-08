class Chess:
    def __init__(self):
        self.__current = None
        self.__old = None
        self.__turn = False

    def createBoard(self):
        self.__current = [
        ["R","H","B","K","Q","B","H","R"],
        ["P","P","P","P","P","P","P","P"],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," ","p"," "," "," "," "],
        ["p","p","p"," ","p","p","p","p"],
        ["r","h","b","k","q","b","h","r"]
        ]

    def boardPrint(self):
        for i in range(8):
            print(" ".join([str(x) for x in self.__current[i]]))

    def pop(self):
        self.__current = self.__old[-1]
        self.__old.pop(-1)

    def Pawn(self):
        if not self.__turn:
            for row in range(8):
                for square in range(8):
                    if self.__current[row][square] == "p": # checking for pawns
                        if self.__current[row - 1][square] == " " and row - 1 >= 0: # checking if space in front is clear
                            if self.__current[row - 2][square] == " " and row - 2 >= 0: # checking 2 squares ahead
                                if row == 6: # checking if pawn in correct square to move two
                                    print("move two squares:",(row - 2, square))
                            print("move one square:", (row - 1, square))
                        if self.__current[row - 1][square - 1].upper() == self.__current[row - 1][square - 1] and self.__current[row - 1][square - 1] != " " and square - 1 >= 0: # checking for captures to the left
                            print("capture left:", (row - 1, square - 1))
                        try:
                            if self.__current[row - 1][square + 1].upper() == self.__current[row - 1][square + 1] and self.__current[row - 1][square + 1] != " " and square + 1 <= 7: # checking for captures to the right
                                print("capture right:", (row - 1, square + 1))
                        except IndexError:
                            print("out of bounds")
                        # en passant to left. check if pawn next to pawn was there before new move
                        if self.__current[row][square - 1] == "P"  and self.__old[-1][row][square]


board = Chess()

def main():
    print("Hello World!")
    board.createBoard()
    board.boardPrint()
    board.Pawn()

if __name__ == "__main__":
    main()
