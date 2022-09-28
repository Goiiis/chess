# chess with an engine
# by me

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
                        try:
                            if self.__current[row - 1][square - 1].upper() == self.__current[row - 1][square - 1] and self.__current[row - 1][square - 1] != " " and square - 1 >= 0: # checking for captures to the left
                                pawn_moves.append((row - 1, square - 1))

                        except IndexError as e:
                            print("pawn error is {}".format(e))

                        try:
                            if square + 1 <= 7:
                                if self.__current[row - 1][square + 1].upper() == self.__current[row - 1][square + 1] and self.__current[row - 1][square + 1] != " ": # checking for captures to the right
                                    pawn_moves.append((row - 1, square + 1))

                        except IndexError as e:
                            print("pawn error is {}".format(e))
                             #out of bounds
                        # en passant to left. check if pawn next to pawn was there before new move. also checks pawn moved 2 squares
                        try:
                            if self.__current[row][square - 1] == "P"  and self.__old[-1][row][square - 1] == " " and square - 1 >= 0 and self.__old[-1][row - 2][square - 1] == "P":
                                pawn_moves.append((row - 1, square - 1))

                        except IndexError as e:
                            print("pawn error is {}".format(e)) #out of bounds
                        # en passant to right. check pawn next to it if it didnt exist before. also check pawn moved two squares
                        try:
                            if self.__current[row][square + 1] == "P"  and self.__old[-1][row][square + 1] == " " and square + 1 <= 7 and self.__old[-1][row - 2][square + 1] == "P":
                                pawn_moves.append((row - 1, square + 1))

                        except IndexError as e:
                            print("pawn error is {}".format(e))
                             #out of bounds
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
                            if square - 1 >= 0:
                                if self.__current[row + 1][square - 1].lower() == self.__current[row + 1][square - 1] and self.__current[row + 1][square - 1] != " ": # checking for captures to the left
                                    pawn_moves.append((row + 1, square - 1))

                        except IndexError as e:
                            print("pawn error is {}".format(e)) #out of bounds

                        try:
                            if self.__current[row + 1][square + 1].lower() == self.__current[row + 1][square + 1] and self.__current[row + 1][square + 1] != " " and square + 1 <= 7: # checking for captures to the right
                                pawn_moves.append((row - 1, square + 1))

                        except IndexError as e:
                            print("pawn error is {}".format(e)) #out of bounds
                        # en passant to left. check if pawn next to pawn was there before new move. also checks pawn moved 2 squares
                        try:
                            if square - 1 >= 0:
                                if self.__current[row][square - 1] == "p"  and self.__old[-1][row][square - 1] == " " and self.__old[-1][row + 2][square - 1] == "p":
                                    pawn_moves.append((row + 1, square - 1))

                        except IndexError as e:
                            print("pawn error is {}".format(e)) #out of bounds
                        # en passant to right. check pawn next to it if it didnt exist before. also check pawn moved two squares
                        try:
                            if self.__current[row][square + 1] == "p"  and self.__old[-1][row][square + 1] == " " and square + 1 <= 7 and self.__old[-1][row + 2][square + 1] == "p":
                                pawn_moves.append((row + 1, square + 1))

                        except IndexError as e:
                            print("pawn error is {}".format(e)) #out of bounds

        return(pawn_moves)

    def Bishop(self):
        bishop_moves = []
        for row in range(8):
            for square in range(8):
                if self.__current[row][square] == "b" and not self.__turn % 2:
                    # up left
                    for i in range(1,8):
                        try:
                            if row - i >= 0 and square - i >= 0:
                                if self.__current[row - i][square - i] == " ":
                                    bishop_moves.append((row - i, square - i))
                                    # stops when piece can be captured
                                elif self.__current[row - i][square - i].upper() == self.__current[row - i][square - i]:
                                    bishop_moves.append((row - i, square - i))
                                    break

                                else:
                                    break

                            else:
                                break

                        except IndexError as e:
                            print("bishop error is {}".format(e))
                            # out of bounds
                    # up right
                    for i in range(1,8):
                        try:
                            if row - i >= 0 and square + i <= 7:
                                if self.__current[row - i][square + i] == " ":
                                    bishop_moves.append((row - i, square + i))
                                    # stops when piece is captured
                                elif self.__current[row - i][square + i].upper() == self.__current[row - i][square + i]:
                                    bishop_moves.append((row - i, square + i))
                                    break

                                else:
                                    break

                            else:
                                break

                        except IndexError as e:
                            print("bishop error is {}".format(e))
                            # out of bounds
                    # down left
                    for i in range(1,8):
                        try:
                            if row + i <= 7 and square - i >= 0:
                                if self.__current[row + i][square - i] == " ":
                                    bishop_moves.append((row + i, square - i))

                                elif self.__current[row + i][square - i].upper() == self.__current[row + i][square - i]:
                                    bishop_moves.append((row + i, square - i))
                                    break

                                else:
                                    break

                            else:
                                break
                        except IndexError as e:
                            print("bishop error is {}".format(e))
                            # out of bounds
                    # down right
                    for i in range(1,8):
                        try:
                            if row + i <= 7 and square + i <= 7:
                                if self.__current[row + i][square + i] == " ":
                                    bishop_moves.append((row + i, square + i))

                                elif self.__current[row + i][square + i].upper() == self.__current[row + i][square + i]:
                                    bishop_moves.append((row + i, square + i))
                                    break

                                else:
                                    break

                            else:
                                break

                        except IndexError as e:
                            print("bishop error is {}".format(e))

                elif self.__current[row][square] == "B" and self.__turn % 2:
                    # up left
                    for i in range(1,8):
                        try:
                            if row - i >= 0 and square - i >= 0:
                                if self.__current[row - i][square - i] == " ":
                                    bishop_moves.append((row - i, square - i))

                                elif self.__current[row - i][square - i].lower() == self.__current[row - i][square - i]:
                                    bishop_moves.append((row - i, square - i))
                                    break

                                else:
                                    break

                            else:
                                break
                        except IndexError as e:
                            print("bishop error is {}".format(e))
                            # out of bounds
                    # up right
                    for i in range(1,8):
                        try:
                            if row - i >= 0 and square + i <= 7:
                                if self.__current[row - i][square + i] == " ":
                                    bishop_moves.append((row - i, square + i))

                                elif self.__current[row - i][square + i].lower() == self.__current[row - i][square + i]:
                                    bishop_moves.append((row - i, square + i))
                                    break

                                else:
                                    break

                            else:
                                break
                        except IndexError as e:
                            print("bishop error is {}".format(e))
                            # out of bounds
                    # down left
                    for i in range(1,8):
                        try:
                            if row + i <= 7 and square - i >= 0:
                                if self.__current[row + i][square - i] == " ":
                                    bishop_moves.append((row + i, square - i))

                                elif self.__current[row + i][square - i].lower() == self.__current[row + i][square - i]:
                                    bishop_moves.append((row + i, square - i))
                                    break

                                else:
                                    break

                            else:
                                break

                        except IndexError as e:
                            print("bishop error is {}".format(e))
                            # out of bounds
                    # down right
                    for i in range(1,8):
                        try:
                            if row + i <= 7 and square + i <= 7:
                                if self.__current[row + i][square + i] == " ":
                                    bishop_moves.append((row + i, square + i))

                                elif self.__current[row + i][square + i].lower() == self.__current[row + i][square + i]:
                                    bishop_moves.append((row + i, square + i))
                                    break

                                else:
                                    break

                            else:
                                break

                        except IndexError as e:
                            print("bishop error is {}".format(e))

        return(bishop_moves)

    def Knight(self):
        knight_moves = []
        if self.__turn % 2 == 0:
            for row in range(8):
                for square in range(8):
                    if self.__current[row][square] == "h":
                    # up up left
                        try:
                            if row - 2 >= 0 and square - 1 >= 0:
                                if self.__current[row - 2][square - 1] != self.__current[row - 2][square - 1].lower() or self.__current[row - 2][square - 1] == " ":
                                    knight_moves.append((row - 2, square - 1))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # down down left
                        try:
                            if row + 2 <= 7 and square - 1 >= 0:
                                if self.__current[row + 2][square - 1] != self.__current[row + 2][square - 1].lower() or self.__current[row + 2][square - 1] == " ":
                                    knight_moves.append((row + 2, square - 1))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # up up right
                        try:
                            if row - 2 >= 0 and square + 1 >= 0:
                                if self.__current[row - 2][square + 1] != self.__current[row - 2][square + 1].lower() or self.__current[row - 2][square + 1] == " ":
                                    knight_moves.append((row - 2, square + 1))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # down down right
                        try:
                            if row + 2 <= 7 and square + 1 <= 7:
                                if self.__current[row + 2][square + 1] != self.__current[row + 2][square + 1].lower() or self.__current[row + 2][square + 1] == " ":
                                    knight_moves.append((row + 2, square + 1))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # left left down
                        try:
                            if square - 2 >= 0 and row + 1 <= 7:
                                if self.__current[row + 1][square - 2] != self.__current[row + 1][square - 2].lower() or self.__current[row + 1][square - 2] == " ":
                                    knight_moves.append((row + 1, square - 2))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # left left up
                        try:
                            if square - 2 >= 0 and row - 1 >= 0:
                                if self.__current[row - 1][square - 2] != self.__current[row - 1][square - 2].lower() or self.__current[row - 1][square - 2] == " ":
                                    knight_moves.append((row - 1, square - 2))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # right right down
                        try:
                            if square + 2 <= 7 and row + 1 <= 7:
                                if self.__current[row + 1][square + 2] != self.__current[row + 1][square + 2].lower() or self.__current[row + 1][square + 2] == " ":
                                    knight_moves.append((row + 1, square + 2))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # right right up
                        try:
                            if square + 2 <= 7 and row - 1 >= 0:
                                if self.__current[row - 1][square + 2] != self.__current[row - 1][square + 2].lower() or self.__current[row - 1][square + 2] == " ":
                                    knight_moves.append((row - 1, square + 2))

                        except IndexError as e:
                            print("knight error is {}".format(e))
        else:
            for row in range(8):
                for square in range(8):
                    if self.__current[row][square] == "H":
                # up up left
                        try:
                            if row - 2 >= 0 and square - 1 >= 0:
                                if self.__current[row - 2][square - 1] != self.__current[row - 2][square - 1].upper() or self.__current[row - 2][square - 1] == " ":
                                    knight_moves.append((row - 2, square - 1))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # down down left
                        try:
                            if row + 2 <= 7 and square - 1 >= 0:
                                if self.__current[row + 2][square - 1] != self.__current[row + 2][square - 1].upper() or self.__current[row + 2][square - 1] == " ":
                                    knight_moves.append((row + 2, square - 1))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # up up right
                        try:
                            if row - 2 >= 0 and square + 1 >= 0:
                                if self.__current[row - 2][square + 1] != self.__current[row - 2][square + 1].upper() or self.__current[row - 2][square + 1] == " ":
                                    knight_moves.append((row - 2, square + 1))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # down down right
                        try:
                            if row + 2 <= 7 and square + 1 <= 7:
                                if self.__current[row + 2][square + 1] != self.__current[row + 2][square + 1].upper() or self.__current[row + 2][square + 1] == " ":
                                    knight_moves.append((row + 2, square + 1))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # left left down
                        try:
                            if square - 2 >= 0 and row + 1 <= 7:
                                if self.__current[row + 1][square - 2] != self.__current[row + 1][square - 2].upper() or self.__current[row + 1][square - 2] == " ":
                                    knight_moves.append((row + 1, square - 2))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # left left up
                        try:
                            if square - 2 >= 0 and row - 1 >= 0:
                                if self.__current[row - 1][square - 2] != self.__current[row - 1][square - 2].upper() or self.__current[row - 1][square - 2] == " ":
                                    knight_moves.append((row - 1, square - 2))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # right right down
                        try:
                            if square + 2 <= 7 and row + 1 <= 7:
                                if self.__current[row + 1][square + 2] != self.__current[row + 1][square + 2].upper() or self.__current[row + 1][square + 2] == " ":
                                    knight_moves.append((row + 1, square + 2))

                        except IndexError as e:
                            print("knight error is {}".format(e))

                        # right right up
                        try:
                            if square + 2 <= 7 and row - 1 >= 0:
                                if self.__current[row - 1][square + 2] != self.__current[row - 1][square + 2].upper() or self.__current[row - 1][square + 2] == " ":
                                    knight_moves.append((row - 1, square + 2))

                        except IndexError as e:
                            print("knight error is {}".format(e))

        return(knight_moves)

    def Rook(self):
        rook_moves = []
        for row in range(8):
            for square in range(8):
                if self.__turn % 2 == 0 and self.__current[row][square] == 'r':
                     # checks right
                    for i in range(1,8):
                        try:
                            if square + i <= 7:
                                if self.__current[row][square + i] == ' ':
                                    rook_moves.append((row, square + i))

                                elif self.__current[row][square + i].upper() == self.__current[row][square + i]:
                                    rook_moves.append((row, square + i))
                                    break

                                else:
                                    break
                            else:
                                break

                        except IndexError as e:
                            prinet("rook error is {}".format(e))
                            break
                    # check left
                    for i in range(1,8):
                        try:
                            if square - i >= 0:
                                if self.__current[row][square - i] == ' ':
                                    rook_moves.append((row, square - i))

                                elif self.__current[row][square - i].upper() == self.__current[row][square - i]:
                                    rook_moves.append((row, square - i))
                                    break

                                else:
                                    break
                            else:
                                break

                        except IndexError as e:
                            print("rook error is {}".format(e))
                            break
                    # check up
                    for i in range(1,8):
                        try:
                            if row - i >= 0:
                                if self.__current[row - i][square] == ' ':
                                    rook_moves.append((row - i, square))

                                elif self.__current[row - i][square].upper() == self.__current[row - i][square]:
                                    rook_moves.append((row - i, square))
                                    break

                                else:
                                    break
                            else:
                                break

                        except IndexError as e:
                            print("rook error is {}".format(e))
                            break
                    # check down
                    for i in range(1,8):
                        try:
                            if row + i <= 7:
                                if self.__current[row + i][square] == ' ':
                                    rook_moves.append((row + i, square))

                                elif self.__current[row + i][square].upper() == self.__current[row + i][square]:
                                    rook_moves.append((row + i, square))
                                    break

                                else:
                                    break
                            else:
                                break

                        except IndexError as e:
                            print("rook error is {}".format(e))
                            break

                elif self.__turn % 2 == 1 and self.__current[row][square] == 'R':
                    # checks right
                    for i in range(1,8):
                        try:
                            if square + i <= 7:
                                if self.__current[row][square + i] == ' ':
                                    rook_moves.append((row, square + i))

                                elif self.__current[row][square + i].lower() == self.__current[row][square + i]:
                                    rook_moves.append((row, square + i))
                                    break

                                else:
                                    break
                            else:
                                break

                        except IndexError as e:
                           print("rook error is {}".format(e))
                           break

                   # check left
                    for i in range(1,8):
                        try:
                            if square - i >= 0:
                                if self.__current[row][square - i] == ' ':
                                    rook_moves.append((row, square - i))

                                elif self.__current[row][square - i].lower() == self.__current[row][square - i]:
                                    rook_moves.append((row, square - i))
                                    break

                                else:
                                    break
                            else:
                                break

                        except IndexError:
                            break
                   # check up
                    for i in range(1,8):
                        try:
                            if row - i >= 0:
                                if self.__current[row - i][square] == ' ' and row - i >= 0:
                                    rook_moves.append((row - i, square))

                                elif self.__current[row - i][square].lower() == self.__current[row - i][square] and row - i >= 0:
                                    rook_moves.append((row - i, square))
                                    break

                                else:
                                    break
                            else:
                                break

                        except IndexError as e:
                            print("rook error is {}".format(e))
                            break
                   # check down
                    for i in range(1,8):
                        try:
                            if row + i <= 7:
                                if self.__current[row + i][square] == ' ':
                                    rook_moves.append((row + i, square))

                                elif self.__current[row + i][square].lower() == self.__current[row + i][square]:
                                    rook_moves.append((row + i, square))
                                    break

                                else:
                                    break
                            else:
                                break

                        except IndexError as e:
                            print("rook error is {}".format(e))
                            break
        return rook_moves


    def make_move(self, x1, y1, x2, y2):
        # x is row y is column
        piece = self.__current[x1][y1]
        print("current piece is {}".format(piece))
        moves = []
        if not self.__turn % 2: #white goes
            if piece == "p":
                moves = self.Pawn()

            if piece == "b":
                moves = self.Bishop()

            if piece == "r":
                moves = self.Rook()

            if piece == "h":
                moves = self.Knight()

            if (x2, y2) in moves:
                self.__old.append(self.__current)
                self.__current[x2][y2] = piece
                self.__current[x1][y1] = " "
                self.__turn += 1
            else:
                print("fail white")
                print("moves are {}".format(moves))



        else:
            if piece == "P":
                moves = self.Pawn()

            if piece == "B":
                moves = self.Bishop()

            if piece == "R":
                moves = self.Rook()

            if piece == "H":
                moves = self.Knight()

            if (x2, y2) in moves:
                self.__old.append(self.__current)
                self.__current[x2][y2] = piece
                self.__current[x1][y1] = " "
                self.__turn += 1
            else:
                print("fail black")
                print("moves are {}".format(moves))




board = Chess()

def main():
    print("Hello World!")
    board.createBoard()
    print("board created")
    board.make_move(6,0,4,0) #a4
    board.make_move(1,0,3,0) #a5
    board.make_move(7, 1, 5, 2)

    board.boardPrint()


if __name__ == "__main__":
    main()
