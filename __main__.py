# chess with an engine
# by me

class Chess:
    def __init__(self):
        self.__current = None
        self.__old = []
        self.__turn = 0
        self.__white_l = True
        self.__white_r = True
        self.__black_l = True
        self.__black_r = True

    def createBoard(self):
        self.__current = [[
        ["R","H","B","Q","K","B","H","R"],
        ["P","P","P","P","P","P","P","P"],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        ["p","p","p","p","p","p","p","p"],
        ["r","h","b","q","k","b","h","r"]
        ], {"white_left": True, "white_right": True, "black_left": True, "black_right,": True}]
        self.__old = [[
        [
        ["R","H","B","K","Q","B","H","R"],
        ["P","P","P","P","P","P","P","P"],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        ["p","p","p","p","p","p","p","p"],
        ["r","h","b","q","k","b","h","r"]],
        {"white_left": True, "white_right": True, "black_left": True, "black_right,": True}]]
    def boardPrint(self):
        for i in range(8):
            print(" ".join([str(x) for x in self.__current[0][i]]))

        print(self.__old)

    def pop(self):
        self.__current = self.__old[-1]
        self.__old.pop(-1)
        self.boardPrint()

    def Pawn(self, row, square):
        pawn_moves = []
        if self.__turn % 2 == 0:
            if self.__current[0][row - 1][square] == " " and row - 1 >= 0: # checking if space in front is clear
                pawn_moves.append((row - 1, square))

                if self.__current[0][row - 2][square] == " " and row - 2 >= 0: # checking 2 squares ahead
                    if row == 6: # checking if pawn in correct square to move two
                        pawn_moves.append((row - 2, square))
            try:
                if self.__current[0][row - 1][square - 1].upper() == self.__current[0][row - 1][square - 1] and self.__current[0][row - 1][square - 1] != " " and square - 1 >= 0: # checking for captures to the left
                    pawn_moves.append((row - 1, square - 1))

            except IndexError as e:
                print("pawn error is {}".format(e))

            try:
                if square + 1 <= 7:
                    if self.__current[0][row - 1][square + 1].upper() == self.__current[0][row - 1][square + 1] and self.__current[0][row - 1][square + 1] != " ": # checking for captures to the right
                        pawn_moves.append((row - 1, square + 1))

            except IndexError as e:
                print("pawn error is {}".format(e))
                 #out of bounds
            # en passant to left. check if pawn next to pawn was there before new move. also checks pawn moved 2 squares
            try:
                if self.__current[0][row][square - 1] == "P"  and self.__old[-1][row][square - 1] == " " and square - 1 >= 0 and self.__old[-1][row - 2][square - 1] == "P":
                    pawn_moves.append((row - 1, square - 1))

            except IndexError as e:
                print("pawn error is {}".format(e)) #out of bounds
            # en passant to right. check pawn next to it if it didnt exist before. also check pawn moved two squares
            try:
                if self.__current[0][row][square + 1] == "P"  and self.__old[-1][row][square + 1] == " " and square + 1 <= 7 and self.__old[-1][row - 2][square + 1] == "P":
                    pawn_moves.append((row - 1, square + 1))

            except IndexError as e:
                print("pawn error is {}".format(e))
                 #out of bounds
        elif self.__turn % 2 == 1:
            if self.__current[0][row + 1][square] == " " and row + 1 <= 7: # checking if space in front is clear
                pawn_moves.append((row + 1, square))

                if self.__current[0][row + 2][square] == " " and row + 2 <= 7: # checking 2 squares ahead
                    if row == 1: # checking if pawn in correct square to move two
                        pawn_moves.append((row + 2, square))

            try:
                if square - 1 >= 0:
                    if self.__current[0][row + 1][square - 1].lower() == self.__current[0][row + 1][square - 1] and self.__current[0][row + 1][square - 1] != " ": # checking for captures to the left
                        pawn_moves.append((row + 1, square - 1))

            except IndexError as e:
                print("pawn error is {}".format(e)) #out of bounds

            try:
                if self.__current[0][row + 1][square + 1].lower() == self.__current[0][row + 1][square + 1] and self.__current[0][row + 1][square + 1] != " " and square + 1 <= 7: # checking for captures to the right
                    pawn_moves.append((row - 1, square + 1))

            except IndexError as e:
                print("pawn error is {}".format(e)) #out of bounds
            # en passant to left. check if pawn next to pawn was there before new move. also checks pawn moved 2 squares
            try:
                if square - 1 >= 0:
                    if self.__current[0][row][square - 1] == "p"  and self.__old[-1][row][square - 1] == " " and self.__old[-1][row + 2][square - 1] == "p":
                        pawn_moves.append((row + 1, square - 1))

            except IndexError as e:
                print("pawn error is {}".format(e)) #out of bounds
            # en passant to right. check pawn next to it if it didnt exist before. also check pawn moved two squares
            try:
                if self.__current[0][row][square + 1] == "p"  and self.__old[-1][row][square + 1] == " " and square + 1 <= 7 and self.__old[-1][row + 2][square + 1] == "p":
                    pawn_moves.append((row + 1, square + 1))

            except IndexError as e:
                print("pawn error is {}".format(e)) #out of bounds

        else:
            print("something went wrong")

        return(pawn_moves)

    def Bishop(self, row, square):
        bishop_moves = []
        if self.__turn % 2 == 0:
            # up left
            for i in range(1,8):
                try:
                    if row - i >= 0 and square - i >= 0:
                        if self.__current[0][row - i][square - i] == " ":
                            bishop_moves.append((row - i, square - i))
                            # stops when piece can be captured
                        elif self.__current[0][row - i][square - i].upper() == self.__current[0][row - i][square - i]:
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
                        if self.__current[0][row - i][square + i] == " ":
                            bishop_moves.append((row - i, square + i))
                            # stops when piece is captured
                        elif self.__current[0][row - i][square + i].upper() == self.__current[0][row - i][square + i]:
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
                        if self.__current[0][row + i][square - i] == " ":
                            bishop_moves.append((row + i, square - i))

                        elif self.__current[0][row + i][square - i].upper() == self.__current[0][row + i][square - i]:
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
                        if self.__current[0][row + i][square + i] == " ":
                            bishop_moves.append((row + i, square + i))

                        elif self.__current[0][row + i][square + i].upper() == self.__current[0][row + i][square + i]:
                            bishop_moves.append((row + i, square + i))
                            break

                        else:
                            break

                    else:
                        break

                except IndexError as e:
                    print("bishop error is {}".format(e))

        elif self.__turn % 2 == 1:
                    # up left
                    for i in range(1,8):
                        try:
                            if row - i >= 0 and square - i >= 0:
                                if self.__current[0][row - i][square - i] == " ":
                                    bishop_moves.append((row - i, square - i))

                                elif self.__current[0][row - i][square - i].lower() == self.__current[0][row - i][square - i]:
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
                                if self.__current[0][row - i][square + i] == " ":
                                    bishop_moves.append((row - i, square + i))

                                elif self.__current[0][row - i][square + i].lower() == self.__current[0][row - i][square + i]:
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
                                if self.__current[0][row + i][square - i] == " ":
                                    bishop_moves.append((row + i, square - i))

                                elif self.__current[0][row + i][square - i].lower() == self.__current[0][row + i][square - i]:
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
                                if self.__current[0][row + i][square + i] == " ":
                                    bishop_moves.append((row + i, square + i))

                                elif self.__current[0][row + i][square + i].lower() == self.__current[0][row + i][square + i]:
                                    bishop_moves.append((row + i, square + i))
                                    break

                                else:
                                    break

                            else:
                                break

                        except IndexError as e:
                            print("bishop error is {}".format(e))

        else:
            print("something went wrong")

        return(bishop_moves)

    def Knight(self, row, square):
        knight_moves = []
        if self.__turn % 2 == 0:
        # up up left
            try:
                if row - 2 >= 0 and square - 1 >= 0:
                    if self.__current[0][row - 2][square - 1] != self.__current[0][row - 2][square - 1].lower() or self.__current[0][row - 2][square - 1] == " ":
                        knight_moves.append((row - 2, square - 1))

            except IndexError as e:
                print("knight error is {}".format(e))

            # down down left
            try:
                if row + 2 <= 7 and square - 1 >= 0:
                    if self.__current[0][row + 2][square - 1] != self.__current[0][row + 2][square - 1].lower() or self.__current[0][row + 2][square - 1] == " ":
                        knight_moves.append((row + 2, square - 1))

            except IndexError as e:
                print("knight error is {}".format(e))

            # up up right
            try:
                if row - 2 >= 0 and square + 1 >= 0:
                    if self.__current[0][row - 2][square + 1] != self.__current[0][row - 2][square + 1].lower() or self.__current[0][row - 2][square + 1] == " ":
                        knight_moves.append((row - 2, square + 1))

            except IndexError as e:
                print("knight error is {}".format(e))

            # down down right
            try:
                if row + 2 <= 7 and square + 1 <= 7:
                    if self.__current[0][row + 2][square + 1] != self.__current[0][row + 2][square + 1].lower() or self.__current[0][row + 2][square + 1] == " ":
                        knight_moves.append((row + 2, square + 1))

            except IndexError as e:
                print("knight error is {}".format(e))

            # left left down
            try:
                if square - 2 >= 0 and row + 1 <= 7:
                    if self.__current[0][row + 1][square - 2] != self.__current[0][row + 1][square - 2].lower() or self.__current[0][row + 1][square - 2] == " ":
                        knight_moves.append((row + 1, square - 2))

            except IndexError as e:
                print("knight error is {}".format(e))

            # left left up
            try:
                if square - 2 >= 0 and row - 1 >= 0:
                    if self.__current[0][row - 1][square - 2] != self.__current[0][row - 1][square - 2].lower() or self.__current[0][row - 1][square - 2] == " ":
                        knight_moves.append((row - 1, square - 2))

            except IndexError as e:
                print("knight error is {}".format(e))

            # right right down
            try:
                if square + 2 <= 7 and row + 1 <= 7:
                    if self.__current[0][row + 1][square + 2] != self.__current[0][row + 1][square + 2].lower() or self.__current[0][row + 1][square + 2] == " ":
                        knight_moves.append((row + 1, square + 2))

            except IndexError as e:
                print("knight error is {}".format(e))

            # right right up
            try:
                if square + 2 <= 7 and row - 1 >= 0:
                    if self.__current[0][row - 1][square + 2] != self.__current[0][row - 1][square + 2].lower() or self.__current[0][row - 1][square + 2] == " ":
                        knight_moves.append((row - 1, square + 2))

            except IndexError as e:
                print("knight error is {}".format(e))
        elif turn % 2 == 1:
                # up up left
            try:
                if row - 2 >= 0 and square - 1 >= 0:
                    if self.__current[0][row - 2][square - 1] != self.__current[0][row - 2][square - 1].upper() or self.__current[0][row - 2][square - 1] == " ":
                        knight_moves.append((row - 2, square - 1))

            except IndexError as e:
                print("knight error is {}".format(e))

            # down down left
            try:
                if row + 2 <= 7 and square - 1 >= 0:
                    if self.__current[0][row + 2][square - 1] != self.__current[0][row + 2][square - 1].upper() or self.__current[0][row + 2][square - 1] == " ":
                        knight_moves.append((row + 2, square - 1))

            except IndexError as e:
                print("knight error is {}".format(e))

            # up up right
            try:
                if row - 2 >= 0 and square + 1 >= 0:
                    if self.__current[0][row - 2][square + 1] != self.__current[0][row - 2][square + 1].upper() or self.__current[0][row - 2][square + 1] == " ":
                        knight_moves.append((row - 2, square + 1))

            except IndexError as e:
                print("knight error is {}".format(e))

            # down down right
            try:
                if row + 2 <= 7 and square + 1 <= 7:
                    if self.__current[0][row + 2][square + 1] != self.__current[0][row + 2][square + 1].upper() or self.__current[0][row + 2][square + 1] == " ":
                        knight_moves.append((row + 2, square + 1))

            except IndexError as e:
                print("knight error is {}".format(e))

            # left left down
            try:
                if square - 2 >= 0 and row + 1 <= 7:
                    if self.__current[0][row + 1][square - 2] != self.__current[0][row + 1][square - 2].upper() or self.__current[0][row + 1][square - 2] == " ":
                        knight_moves.append((row + 1, square - 2))

            except IndexError as e:
                print("knight error is {}".format(e))

            # left left up
            try:
                if square - 2 >= 0 and row - 1 >= 0:
                    if self.__current[0][row - 1][square - 2] != self.__current[0][row - 1][square - 2].upper() or self.__current[0][row - 1][square - 2] == " ":
                        knight_moves.append((row - 1, square - 2))

            except IndexError as e:
                print("knight error is {}".format(e))

            # right right down
            try:
                if square + 2 <= 7 and row + 1 <= 7:
                    if self.__current[0][row + 1][square + 2] != self.__current[0][row + 1][square + 2].upper() or self.__current[0][row + 1][square + 2] == " ":
                        knight_moves.append((row + 1, square + 2))

            except IndexError as e:
                print("knight error is {}".format(e))

            # right right up
            try:
                if square + 2 <= 7 and row - 1 >= 0:
                    if self.__current[0][row - 1][square + 2] != self.__current[0][row - 1][square + 2].upper() or self.__current[0][row - 1][square + 2] == " ":
                        knight_moves.append((row - 1, square + 2))

            except IndexError as e:
                print("knight error is {}".format(e))

        else:
            print("something went wrong")

        return(knight_moves)

    def Rook(self, row, square):
        rook_moves = []
        if self.__turn % 2 == 0:
             # checks right
            for i in range(1,8):
                try:
                    if square + i <= 7:
                        if self.__current[0][row][square + i] == ' ':
                            rook_moves.append((row, square + i))

                        elif self.__current[0][row][square + i].upper() == self.__current[0][row][square + i]:
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
                        if self.__current[0][row][square - i] == ' ':
                            rook_moves.append((row, square - i))

                        elif self.__current[0][row][square - i].upper() == self.__current[0][row][square - i]:
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
                        if self.__current[0][row - i][square] == ' ':
                            rook_moves.append((row - i, square))

                        elif self.__current[0][row - i][square].upper() == self.__current[0][row - i][square]:
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
                        if self.__current[0][row + i][square] == ' ':
                            rook_moves.append((row + i, square))

                        elif self.__current[0][row + i][square].upper() == self.__current[0][row + i][square]:
                            rook_moves.append((row + i, square))
                            break

                        else:
                            break
                    else:
                        break

                except IndexError as e:
                    print("rook error is {}".format(e))
                    break

        elif self.__turn % 2 == 1 and self.__current[0][row][square] == 'R':
            # checks right
            for i in range(1,8):
                try:
                    if square + i <= 7:
                        if self.__current[0][row][square + i] == ' ':
                            rook_moves.append((row, square + i))

                        elif self.__current[0][row][square + i].lower() == self.__current[0][row][square + i]:
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
                        if self.__current[0][row][square - i] == ' ':
                            rook_moves.append((row, square - i))

                        elif self.__current[0][row][square - i].lower() == self.__current[0][row][square - i]:
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
                        if self.__current[0][row - i][square] == ' ' and row - i >= 0:
                            rook_moves.append((row - i, square))

                        elif self.__current[0][row - i][square].lower() == self.__current[0][row - i][square] and row - i >= 0:
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
                        if self.__current[0][row + i][square] == ' ':
                            rook_moves.append((row + i, square))

                        elif self.__current[0][row + i][square].lower() == self.__current[0][row + i][square]:
                            rook_moves.append((row + i, square))
                            break

                        else:
                            break
                    else:
                        break

                except IndexError as e:
                    print("rook error is {}".format(e))
                    break
        else:
            print("something went wrong")

        return rook_moves

    def Queen(self, row, square):
        move_rook = self.Rook(row, square)
        move_bishop = self.Bishop(row, square)
        return move_rook + move_bishop

    def make_move(self, x1, y1, x2, y2):
        # x is row y is column
        piece = self.__current[0][x1][y1]
        print("current piece is {}".format(piece))
        moves = []
        piece = piece.lower()
        if piece == "p":
            moves = self.Pawn(x1, y1)

        if piece == "b":
            moves = self.Bishop(x1, y1)

        if piece == "r":
            moves = self.Rook(x1, y1)

        if piece == "h":
            moves = self.Knight(x1, y1)

        if piece == "q":
            moves = self.Queen(x1, y1)

        if (x2, y2) in moves:
            if x1 == 7 and y1 == 0: # if left rook moves
                self.__white_l = False # left rook now has no castle
                self.__current[1]["white_left"] = False

            self.__old.append(self.__current)
            self.__current[0][x2][y2] = piece
            self.__current[0][x1][y1] = " "
            self.__turn += 1
        else:
            print("fail turn {}".format(self.__turn))
            print("moves are {}".format(moves))





board = Chess()

def main():
    print("Hello World!")
    board.createBoard()
    print("board created")
    board.make_move(6,4,4,4) #a4
    board.make_move(1,4,3,4) #a5
    board.make_move(7, 1, 5, 2)

    board.boardPrint()

    print

if __name__ == "__main__":
    main()
