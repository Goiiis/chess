class Chess:
    def __init__(self):
        self.__current = None
        self.__old = []
        self.__turn = 0

    def createBoard(self):
        self.__current = [
        ["R","H","B","K","Q","B","H","R"],
        ["P","P","P","P","P","P","P","P"],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        ["p","p","p","p","p","p","p","p"],
        ["r","h","b","k","q","b","h","r"]
        ]
        self.__old = [[
        ["R","H","B","K","Q","B","H","R"],
        ["P","P","P","P","P","P","P","P"],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        ["p","p","p","p","p","p","p","p"],
        ["r","h","b","k","q","b","h","r"]
        ]]
    def boardPrint(self):
        for i in range(8):
            print(" ".join([str(x) for x in self.__current[i]]))

    def pop(self):
        self.__current = self.__old[-1]
        self.__old.pop(-1)
        self.boardPrint()

    def Pawn(self):
        pawn_moves = []
        if not self.__turn % 2:
            for row in range(8):
                for square in range(8):
                    if self.__current[row][square] == "p": # checking for pawns
                        if self.__current[row - 1][square] == " " and row - 1 >= 0: # checking if space in front is clear
                            pawn_moves.append((row - 1, square))

                            if self.__current[row - 2][square] == " " and row - 2 >= 0: # checking 2 squares ahead
                                if row == 6: # checking if pawn in correct square to move two
                                    pawn_moves.append((row - 2, square))

                        if self.__current[row - 1][square - 1].upper() == self.__current[row - 1][square - 1] and self.__current[row - 1][square - 1] != " " and square - 1 >= 0: # checking for captures to the left
                            pawn_moves.append((row - 1, square - 1))

                        try:
                            if self.__current[row - 1][square + 1].upper() == self.__current[row - 1][square + 1] and self.__current[row - 1][square + 1] != " " and square + 1 <= 7: # checking for captures to the right
                                pawn_moves.append((row - 1, square + 1))

                        except IndexError:
                            pass #out of bounds
                        # en passant to left. check if pawn next to pawn was there before new move. also checks pawn moved 2 squares
                        try:
                            if self.__current[row][square - 1] == "P"  and self.__old[-1][row][square - 1] == " " and square - 1 >= 0 and self.__old[-1][row - 2][square - 1] == "P":
                                pawn_moves.append((row - 1, square - 1))

                        except IndexError:
                            pass #out of bounds
                        # en passant to right. check pawn next to it if it didnt exist before. also check pawn moved two squares
                        try:
                            if self.__current[row][square + 1] == "P"  and self.__old[-1][row][square + 1] == " " and square + 1 <= 7 and self.__old[-1][row - 2][square + 1] == "P":
                                pawn_moves.append((row - 1, square + 1))

                        except IndexError:
                            pass #out of bounds
        else:
            for row in range(8):
                for square in range(8):
                    if self.__current[row][square] == "P": # checking for pawns
                        if self.__current[row + 1][square] == " " and row + 1 <= 7: # checking if space in front is clear
                            pawn_moves.append((row + 1, square))

                            if self.__current[row + 2][square] == " " and row + 2 <= 7: # checking 2 squares ahead
                                if row == 1: # checking if pawn in correct square to move two
                                    pawn_moves.append((row + 2, square))

                        try:
                            if self.__current[row + 1][square - 1].lower() == self.__current[row + 1][square - 1] and self.__current[row + 1][square - 1] != " " and square - 1 >= 0: # checking for captures to the left
                                pawn_moves.append((row + 1, square - 1))

                        except IndexError:
                            pass #out of bounds

                        try:
                            if self.__current[row + 1][square + 1].lower() == self.__current[row + 1][square + 1] and self.__current[row + 1][square + 1] != " " and square + 1 <= 7: # checking for captures to the right
                                pawn_moves.append((row - 1, square + 1))

                        except IndexError:
                            pass #out of bounds
                        # en passant to left. check if pawn next to pawn was there before new move. also checks pawn moved 2 squares
                        try:
                            if self.__current[row][square - 1] == "p"  and self.__old[-1][row][square - 1] == " " and square - 1 >= 0 and self.__old[-1][row + 2][square - 1] == "p":
                                pawn_moves.append((row + 1, square - 1))

                        except IndexError:
                            pass #out of bounds
                        # en passant to right. check pawn next to it if it didnt exist before. also check pawn moved two squares
                        try:
                            if self.__current[row][square + 1] == "p"  and self.__old[-1][row][square + 1] == " " and square + 1 <= 7 and self.__old[-1][row + 2][square + 1] == "p":
                                pawn_moves.append((row + 1, square + 1))

                        except IndexError:
                            pass #out of bounds

        return(pawn_moves)

    def Bishop(self):
        bishop_moves = []
        for row in range(8):
            for square in range(8):
                if self.__current[row][square] == "b" and not self.__turn % 2:
                    # up left
                    for i in range(7):
                        try:
                            if self.__current[row - i][square - i] == " " and row - i >= 0 and square - i >= 0:
                                bishop_moves.append((row - i, square - i))
                                # stops when piece can be captured
                            elif self.__current[row - i][square - i].upper() == self.__current[row - i][square - i] and row - i >= 0 and square - i >= 0:
                                bishop_moves.append((row - i, square - i))
                                break

                            else:
                                break
                        except IndexError:
                            break
                            # out of bounds
                    # up right
                    # do i + 1
                    for i in range(7):
                        try:
                            print(i, self.__current[row][square], row - i >= 0 and square + i <= 7)
                            if self.__current[row - i][square + i] == " " and row - i >= 0 and square + i <= 7:
                                print("hmmm")
                                bishop_moves.append((row - i, square + i))

                            elif self.__current[row - i][square + i].upper() == self.__current[row - i][square + i] and row - i >= 0 and square + i <= 7:
                                bishop_moves.append((row - i, square + i))
                                break

                            else:
                                break

                        except IndexError:
                            break
                            # out of bounds
                    # down left
                    for i in range(7):
                        try:
                            if self.__current[row + i][square - i] == " " and row + i <= 7 and square - i >= 0:
                                bishop_moves.append((row + i, square - i))

                            elif self.__current[row + i][square - i].upper() == self.__current[row + i][square - i] and row + i <= 7 and square - i >= 0:
                                bishop_moves.append((row + i, square - i))
                                break

                            else:
                                break
                        except IndexError:
                            break
                            # out of bounds
                    # down right
                    for i in range(7):
                        try:
                            if self.__current[row + i][square + i] == " " and row + i <= 7 and square + i >= 0:
                                bishop_moves.append((row + i, square + i))

                            elif self.__current[row + i][square + i].upper() == self.__current[row + i][square + i] and row + i <= 7 and square + i <= 7:
                                bishop_moves.append((row + i, square + i))
                                break

                            else:
                                break

                        except IndexError:
                            break

                elif self.__current[row][square] == "B" and self.__turn % 2:
                    # up left
                    for i in range(7):
                        try:
                            if self.__current[row - i][square - i] == " " and row - i >= 0 and square - i >= 0:
                                bishop_moves.append((row - i, square - i))

                            elif self.__current[row - i][square - i].lower() == self.__current[row - i][square - i] and row - i >= 0 and square - i >= 0:
                                bishop_moves.append((row - i, square - i))
                                break

                            else:
                                break
                        except IndexError:
                            break
                            # out of bounds
                    # up right
                    for i in range(7):
                        try:
                            if self.__current[row - i][square + i] == " " and row - i >= 0 and square + i <= 7:
                                bishop_moves.append((row - i, square + i))

                            elif self.__current[row - i][square + i].lower() == self.__current[row - i][square + i] and row - i >= 0 and square + i <= 7:
                                bishop_moves.append((row - i, square + i))
                                break

                            else:
                                break
                        except IndexError:
                            break
                            # out of bounds
                    # down left
                    for i in range(7):
                        try:
                            if self.__current[row + i][square - i] == " " and row + i <= 7 and square - i >= 0:
                                bishop_moves.append((row + i, square - i))

                            elif self.__current[row + i][square - i].lower() == self.__current[row + i][square - i] and row + i <= 7 and square - i >= 0:
                                bishop_moves.append((row + i, square - i))
                                break

                            else:
                                break
                        except IndexError:
                            break
                            # out of bounds
                    # down right
                    for i in range(7):
                        try:
                            if self.__current[row + i][square + i] == " " and row + i <= 7 and square + i >= 0:
                                bishop_moves.append((row + i, square + i))

                            elif self.__current[row + i][square + i].lower() == self.__current[row + i][square + i] and row + i <= 7 and square + i <= 7:
                                bishop_moves.append((row + i, square + i))
                                break

                            else:
                                break
                        except IndexError:
                            break
        return(bishop_moves)


    def make_move(self, x1, y1, x2, y2):
        # x is row y is column
        piece = self.__current[x1][y1]
        print("current piece is {}".format(piece))
        if not self.__turn % 2: #white goes
            if piece == "p":
                moves = self.Pawn()
                if (x2, y2) in moves:
                    self.__old.append(self.__current)
                    self.__current[x2][y2] = piece
                    self.__current[x1][y1] = " "
                    self.__turn += 1
                else:
                    print('fail')

            if piece == "b":
                moves = self.Bishop()
                print(moves)
                for things in moves:
                    print(moves)

        else:
            if piece == "P":
                moves = self.Pawn()
                if (x2, y2) in moves:
                    self.__old.append(self.__current)
                    self.__current[x2][y2] = piece
                    self.__current[x1][y1] = " "
                    self.__turn += 1
                print('fail')



board = Chess()

def main():
    print("Hello World!")
    board.createBoard()
    print("board created")
    board.make_move(6,3,4,3) #e4
    board.boardPrint()
    board.make_move(1,4,3,4) #e5
    board.boardPrint()
    board.make_move(7,2,3,4)
    board.boardPrint()


if __name__ == "__main__":
    main()
