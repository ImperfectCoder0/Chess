

X = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Y = ['1', '2', '3', '4', '5', '6', '7', '8']
WHITE_PIECES = ['wp', 'wn', 'wb', 'wr', 'wq', 'wk']
BLACK_PIECES = ['bp', 'bn', 'bb', 'br', 'bq', 'bk']


class Board:
    positions = {'a1': 'wr', 'a2': 'wp', 'a3': None, 'a4': None, 'a5': None, 'a6': None, 'a7': 'bp', 'a8': 'br',
                 'b1': 'wn', 'b2': 'wp', 'b3': None, 'b4': None, 'b5': None, 'b6': None, 'b7': 'bp', 'b8': 'bn',
                 'c1': 'wb', 'c2': 'wp', 'c3': None, 'c4': None, 'c5': None, 'c6': None, 'c7': 'bp', 'c8': 'bb',
                 'd1': 'wq', 'd2': 'wp', 'd3': None, 'd4': None, 'd5': None, 'd6': None, 'd7': 'bp', 'd8': 'bq',
                 'e1': 'wk', 'e2': 'wp', 'e3': None, 'e4': None, 'e5': None, 'e6': None, 'e7': 'bp', 'e8': 'bk',
                 'f1': 'wb', 'f2': 'wp', 'f3': None, 'f4': None, 'f5': None, 'f6': None, 'f7': 'bp', 'f8': 'bb',
                 'g1': 'wn', 'g2': 'wp', 'g3': None, 'g4': None, 'g5': None, 'g6': None, 'g7': 'bp', 'g8': 'bn',
                 'h1': 'wr', 'h2': 'wp', 'h3': None, 'h4': None, 'h5': None, 'h6': None, 'h7': 'bp', 'h8': 'br'}
    white_legal_moves = {}
    black_legal_moves = {}

    def __init__(self):
        self.squares = 64

    def check_for_pieces(self, new, color: str):
        color = color[0].lower()
        if Board.positions[new] != None:
            if Board.positions[new][0] == color:
                return -1
            elif Board.positions[new][0] != color:
                return 0
        return 1

    def update(self, old, new, piece, color):
        Board.positions[old] = None
        Board.positions[new] = piece + color

    def Legal_Moves(self, *args, **kwargs):
        raise NotImplementedError('Move is not implemented in class')

    def in_check(self, color, pos):
        if color == 'w':
            opposite = Board.black_legal_moves
        elif color == 'b':
            opposite = Board.white_legal_moves
        for piece in opposite.keys():
            if opposite[piece] is None:
                continue
            if piece.__class__ == Pawn:
                if not piece.capturable:
                    continue

                try:
                    if opposite[piece][-2] == pos:
                        return 1
                except IndexError:
                    try:
                        if opposite[piece][-1] == pos:
                            return 1
                    except IndexError:
                        pass
            else:
                for move in opposite[piece]:
                    if move == pos:
                        return 1


class King(Board):
    def __init__(self, pos, color: str):
        super(King, self).__init__()
        self.legal_moves = []
        self.color = color[0].lower()
        self.pos = pos
        self.has_moved = False
        super().positions[pos] = color + 'k'

    def Legal_Moves(self, rook):
        Maximum = 1

        for XPos in range(1, Maximum + 1):
            for YPos in range(1, Maximum + 1):

                xPos2 = X.index(self.pos[0])
                yPos2 = Y.index(self.pos[1])
                Right_Moves = [(xPos2 + XPos, yPos2), (xPos2 + XPos, yPos2 + YPos), (xPos2 + XPos, yPos2 - YPos)]
                Left_Moves = [(xPos2 - XPos, yPos2), (xPos2 - XPos, yPos2 + YPos), (xPos2 - XPos, yPos2 - YPos)]
                Up_Moves = [(xPos2, yPos2 + YPos), (xPos2 + XPos, yPos2 + YPos), (xPos2 - XPos, yPos2 + YPos)]
                Down_Moves = [(xPos2, yPos2 - YPos), (xPos2 + XPos, yPos2 - YPos), (xPos2 - XPos, yPos2 - YPos)]
                Right = Left = Up = Down = True
                if xPos2 + XPos >= 8:
                    Right = False
                    del Up_Moves[1]
                    del Down_Moves[1]
                elif xPos2 - XPos <= -1:
                    Left = False
                    del Up_Moves[2]
                    del Down_Moves[2]
                if yPos2 + YPos >= 8:
                    Up = False
                    del Right_Moves[1]
                    del Left_Moves[1]
                elif yPos2 - YPos <= -1:
                    Down = False
                    del Right_Moves[2]
                    del Left_Moves[2]

                if Right:
                    for Seperate_Right_Moves in Right_Moves:
                        SeperatedX = X[Seperate_Right_Moves[0]]
                        SeperatedY = Y[Seperate_Right_Moves[1]]
                        if super(King, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                            self.legal_moves.extend([(SeperatedX + SeperatedY)])
                if Left:
                    for Seperate_Left_Moves in Left_Moves:
                        SeperatedX = X[Seperate_Left_Moves[0]]
                        SeperatedY = Y[Seperate_Left_Moves[1]]
                        if super(King, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                            self.legal_moves.extend([(SeperatedX + SeperatedY)])
                if Up:
                    for Seperate_Up_Moves in Up_Moves:
                        SeperatedX = X[Seperate_Up_Moves[0]]
                        SeperatedY = Y[Seperate_Up_Moves[1]]
                        if super(King, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                            self.legal_moves.extend([(SeperatedX + SeperatedY)])
                if Down:
                    for Seperate_Down_Moves in Down_Moves:
                        SeperatedX = X[Seperate_Down_Moves[0]]
                        SeperatedY = Y[Seperate_Down_Moves[1]]
                        if super(King, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                            self.legal_moves.extend([(SeperatedX + SeperatedY)])

        def is_castling(self: King, rook: Rook):
            white_q_castling = ['d1', 'c1', 'e1']
            white_k_castling = ['e1', 'f1', 'g1']
            black_q_castling = ['d8', 'c8', 'e8']
            black_k_castling = ['e8', 'f8', 'g8']
            if not self.has_moved and not rook.has_moved:
                if rook.pos == 'a1' and self.color == 'w':
                    for moves in white_q_castling:
                        if super(King, self).in_check(self.color, moves) is not None: break
                        else:
                            if super(King, self).check_for_pieces(moves, self.color) == 1:
                                self.legal_moves.append('QC')
                if rook.pos == 'a8' and self.color == 'b':
                    for moves in black_q_castling:
                        if super(King, self).in_check(self.color, moves) is not None: break
                        else:
                            if super(King, self).check_for_pieces(moves, self.color) == 1:
                                self.legal_moves.append('QC')
                if rook.pos == 'h1' and self.color == 'w':
                    for moves in white_k_castling:
                        if super(King, self).in_check(self.color, moves) is not None: break
                        else:
                            if super(King, self).check_for_pieces(moves, self.color) == 1:
                                self.legal_moves.append('KC')
                if rook.pos == 'h8' and self.color == 'b':
                    for moves in black_k_castling:
                        if super(King, self).in_check(self.color, moves) is not None: break
                        else:
                            if super(King, self).check_for_pieces(moves, self.color) == 1:
                                self.legal_moves.append('KC')
        is_castling(self, rook)
        for var in self.legal_moves:
            if super(King, self).in_check(self.color, var) == 1:
                self.legal_moves.remove(var)
        return self.legal_moves


class Queen(Board):
    def __init__(self, pos, color: str):
        super(Queen, self).__init__()
        self.legal_moves = []
        self.color = color[0].lower()
        self.pos = pos
        super().positions[pos] = color + 'q'

    def Legal_Moves(self, king):
        Maximum = 8
        constant_up = []
        constant_down = []
        constant_left = []
        constant_right = []
        for XPos in range(1, Maximum + 1):
            for YPos in range(1, Maximum + 1):
                if XPos != YPos:
                    continue
                xPos2 = X.index(self.pos[0])
                yPos2 = Y.index(self.pos[1])
                Right_Moves = [(xPos2 + XPos, yPos2), (xPos2 + XPos, yPos2 + YPos), (xPos2 + XPos, yPos2 - YPos)]
                Left_Moves = [(xPos2 - XPos, yPos2), (xPos2 - XPos, yPos2 + YPos), (xPos2 - XPos, yPos2 - YPos)]
                Up_Moves = [(xPos2, yPos2 + YPos), (xPos2 + XPos, yPos2 + YPos), (xPos2 - XPos, yPos2 + YPos)]
                Down_Moves = [(xPos2, yPos2 - YPos), (xPos2 + XPos, yPos2 - YPos), (xPos2 - XPos, yPos2 - YPos)]
                for up in constant_up:
                    Up_Moves[up] = None
                for right in constant_right:
                    Right_Moves[right] = None
                    print(constant_right)
                for down in constant_down:
                    Down_Moves[down] = None
                for left in constant_left:
                    Left_Moves[left] = None
                Right = Left = Up = Down = True
                if xPos2 + XPos >= 8:
                    Right = False
                    del Up_Moves[1]
                    del Down_Moves[1]
                if xPos2 - XPos <= -1:
                    Left = False
                    del Up_Moves[-1]
                    del Down_Moves[-1]
                if yPos2 + YPos >= 8:
                    Up = False
                    del Right_Moves[1]
                    del Left_Moves[1]
                if yPos2 - YPos <= -1:
                    Down = False
                    del Right_Moves[-1]
                    del Left_Moves[-1]

                if Right:
                    for Seperate_Right_Moves in Right_Moves:
                        if Seperate_Right_Moves is not None:
                            SeperatedX = X[Seperate_Right_Moves[0]]
                            SeperatedY = Y[Seperate_Right_Moves[1]]
                            if super(Queen, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Queen, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_right.append(Right_Moves.index(Seperate_Right_Moves))
                                print(Seperate_Right_Moves)
                if Left:
                    for Seperate_Left_Moves in Left_Moves:
                        if Seperate_Left_Moves is not None:
                            SeperatedX = X[Seperate_Left_Moves[0]]
                            SeperatedY = Y[Seperate_Left_Moves[1]]
                            if super(Queen, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Queen, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_left.append(Left_Moves.index(Seperate_Left_Moves))
                if Up:
                    for Seperate_Up_Moves in Up_Moves:
                        if Seperate_Up_Moves is not None:
                            SeperatedX = X[Seperate_Up_Moves[0]]
                            SeperatedY = Y[Seperate_Up_Moves[1]]
                            if super(Queen, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Queen, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_up.append(Up_Moves.index(Seperate_Up_Moves))
                if Down:
                    for Seperate_Down_Moves in Down_Moves:
                        if Seperate_Down_Moves is not None:
                            SeperatedX = X[Seperate_Down_Moves[0]]
                            SeperatedY = Y[Seperate_Down_Moves[1]]
                            if super(Queen, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Queen, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_down.append(Down_Moves.index(Seperate_Down_Moves))
                for var in self.legal_moves:
                    if super(Queen, self).in_check(self.color, king.pos) == 1:
                        self.legal_moves.remove(var)
                if XPos == Maximum and YPos == Maximum:
                    return self.legal_moves



class Rook(Board):
    def __init__(self, pos, color: str, side):
        super(Rook, self).__init__()
        self.legal_moves = []
        self.color = color[0].lower()
        self.pos = pos
        self.side = side
        self.has_moved = False
        super().positions[pos] = color + 'r'

    def Legal_Moves(self, king):
        constant_up = []
        constant_down = []
        constant_left = []
        constant_right = []
        for XPos in range(1, 9):
            for YPos in range(1, 9):
                if XPos != YPos:
                    continue
                xPos2 = X.index(self.pos[0])
                yPos2 = Y.index(self.pos[1])
                Right_Moves = [(xPos2 + XPos, yPos2)]
                Left_Moves = [(xPos2 - XPos, yPos2)]
                Up_Moves = [(xPos2, yPos2 + YPos)]
                Down_Moves = [(xPos2, yPos2 - YPos)]
                for up in constant_up:
                    Up_Moves[up] = None
                for right in constant_right:
                    Right_Moves[right] = None
                for down in constant_down:
                    Down_Moves[down] = None
                for left in constant_left:
                    Left_Moves[left] = None
                Right = Left = Up = Down = True
                if xPos2 + XPos >= 8:
                    Right = False
                    del Right_Moves[-1]
                if xPos2 - XPos <= -1:
                    Left = False
                    del Left_Moves[-1]
                if yPos2 + YPos >= 8:
                    Up = False
                    del Up_Moves[-1]
                if yPos2 - YPos <= -1:
                    Down = False
                    del Down_Moves[-1]

                if Right:
                    for Seperate_Right_Moves in Right_Moves:
                        if Seperate_Right_Moves is not None:
                            SeperatedX = X[Seperate_Right_Moves[0]]
                            SeperatedY = Y[Seperate_Right_Moves[1]]
                            if super(Rook, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Rook, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_right.append(Right_Moves.index(Seperate_Right_Moves))
                if Left:
                    for Seperate_Left_Moves in Left_Moves:
                        if Seperate_Left_Moves is not None:
                            SeperatedX = X[Seperate_Left_Moves[0]]
                            SeperatedY = Y[Seperate_Left_Moves[1]]
                            if super(Rook, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Rook, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_left.append(Left_Moves.index(Seperate_Left_Moves))
                if Up:
                    for Seperate_Up_Moves in Up_Moves:
                        if Seperate_Up_Moves is not None:
                            SeperatedX = X[Seperate_Up_Moves[0]]
                            SeperatedY = Y[Seperate_Up_Moves[1]]
                            if super(Rook, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Rook, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_up.append(Up_Moves.index(Seperate_Up_Moves))
                if Down:
                    for Seperate_Down_Moves in Down_Moves:
                        if Seperate_Down_Moves is not None:
                            SeperatedX = X[Seperate_Down_Moves[0]]
                            SeperatedY = Y[Seperate_Down_Moves[1]]
                            if super(Rook, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Rook, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_down.append(Down_Moves.index(Seperate_Down_Moves))
                for var in self.legal_moves:
                    if super(Rook, self).in_check(self.color, king.pos) == 1:
                        self.legal_moves.remove(var)
                if XPos == 8 and YPos == 8:
                    return self.legal_moves


class Bishop(Board):
    def __init__(self, pos, color: str):
        super(Bishop, self).__init__()
        self.legal_moves = []
        self.color = color[0].lower()
        self.pos = pos
        super().positions[pos] = color + 'b'

    def Legal_Moves(self, king):
        constant_up = []
        constant_down = []
        constant_left = []
        constant_right = []
        for XPos in range(1, 9):
            for YPos in range(1, 9):
                if XPos != YPos:
                    continue
                xPos2 = X.index(self.pos[0])
                yPos2 = Y.index(self.pos[1])
                Right_Down_Moves = [(xPos2 + XPos, yPos2 - YPos)]
                Left_Up_Moves = [(xPos2 - XPos, yPos2 + YPos)]
                Right_Up_Moves = [(xPos2 + XPos, yPos2 + YPos)]
                Left_Down_Moves = [(xPos2 - YPos, yPos2 - YPos)]
                for up in constant_up:
                    Right_Up_Moves[up] = None
                for right in constant_right:
                    Right_Down_Moves[right] = None
                for down in constant_down:
                    Left_Down_Moves[down] = None
                for left in constant_left:
                    Left_Up_Moves[left] = None
                Right = Left = Up = Down = True
                if xPos2 + XPos >= 8:
                    Right = False
                    del Right_Down_Moves[-1]
                if xPos2 - XPos <= -1:
                    Left = False
                    del Left_Up_Moves[-1]
                if yPos2 + YPos >= 8:
                    Up = False
                    del Right_Up_Moves[-1]
                if yPos2 - YPos <= -1:
                    Down = False
                    del Left_Down_Moves[-1]

                if Right:
                    for Seperate_Right_Moves in Right_Down_Moves:
                        if Seperate_Right_Moves is not None:
                            SeperatedX = X[Seperate_Right_Moves[0]]
                            SeperatedY = Y[Seperate_Right_Moves[1]]
                            if super(Bishop, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Bishop, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_right.append(Right_Down_Moves.index(Seperate_Right_Moves))
                if Left:
                    for Seperate_Left_Moves in Left_Up_Moves:
                        if Seperate_Left_Moves is not None:
                            SeperatedX = X[Seperate_Left_Moves[0]]
                            SeperatedY = Y[Seperate_Left_Moves[1]]
                            if super(Bishop, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Bishop, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_left.append(Left_Up_Moves.index(Seperate_Left_Moves))
                if Up:
                    for Seperate_Up_Moves in Right_Up_Moves:
                        if Seperate_Up_Moves is not None:
                            SeperatedX = X[Seperate_Up_Moves[0]]
                            SeperatedY = Y[Seperate_Up_Moves[1]]
                            if super(Bishop, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Bishop, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_up.append(Right_Up_Moves.index(Seperate_Up_Moves))
                if Down:
                    for Seperate_Down_Moves in Left_Down_Moves:
                        if Seperate_Down_Moves is not None:
                            SeperatedX = X[Seperate_Down_Moves[0]]
                            SeperatedY = Y[Seperate_Down_Moves[1]]
                            if super(Bishop, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                                self.legal_moves.extend([(SeperatedX + SeperatedY)])
                            if super(Bishop, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != 1:
                                constant_down.append(Left_Down_Moves.index(Seperate_Down_Moves))
                for var in self.legal_moves:
                    if super(Bishop, self).in_check(self.color, king.pos) == 1:
                        self.legal_moves.remove(var)
                if XPos == 8 and YPos == 8:
                    return self.legal_moves


class Knight(Board):
    def __init__(self, pos, color: str):
        super(Knight, self).__init__()
        self.legal_moves = []
        self.color = color[0].lower()
        self.pos = pos
        super().positions[pos] = color + 'n'

    def Legal_Moves(self, king):
        xPos2 = X.index(self.pos[0])
        yPos2 = Y.index(self.pos[1])
        Right_Moves = [(xPos2 + 2, yPos2 - 1), (xPos2 + 2, yPos2 + 1)]
        Left_Moves = [(xPos2 - 2, yPos2 + 1), (xPos2 - 2, yPos2 - 1)]
        Up_Moves = [(xPos2 + 1, yPos2 + 2), (xPos2 - 1, yPos2 + 2)]
        Down_Moves = [(xPos2 - 1, yPos2 - 2), (xPos2 + 1, yPos2 - 2)]
        Right = Left = Up = Down = True
        if xPos2 + 2 >= 8:
            Right = False
            Right_Moves.clear()
            if xPos2 + 1 >= 8 and Up_Moves and Down_Moves:
                del Up_Moves[0]
                del Down_Moves[1]
        if xPos2 - 2 <= -1:
            Left = False
            Left_Moves.clear()
            if xPos2 - 1 <= -1 and Up_Moves and Down_Moves:
                del Up_Moves[1]
                del Down_Moves[0]
        if yPos2 + 2 >= 8:
            Up = False
            Up_Moves.clear()
            if yPos2 + 1 >= 8 and Left_Moves and Right_Moves:
                del Right_Moves[1]
                del Left_Moves[0]
        if yPos2 - 2 <= -1:
            Down = False
            Down_Moves.clear()
            if yPos2 - 1 <= -1 and Left_Moves and Right_Moves:
                del Right_Moves[0]
                del Left_Moves[1]

        if Right:
            for Seperate_Right_Moves in Right_Moves:
                SeperatedX = X[Seperate_Right_Moves[0]]
                SeperatedY = Y[Seperate_Right_Moves[1]]
                if super(Knight, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                    self.legal_moves.extend([(SeperatedX + SeperatedY)])
        if Left:
            for Seperate_Left_Moves in Left_Moves:
                SeperatedX = X[Seperate_Left_Moves[0]]
                SeperatedY = Y[Seperate_Left_Moves[1]]
                if super(Knight, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                    self.legal_moves.extend([(SeperatedX + SeperatedY)])
        if Up:
            for Seperate_Up_Moves in Up_Moves:
                SeperatedX = X[Seperate_Up_Moves[0]]
                SeperatedY = Y[Seperate_Up_Moves[1]]
                if super(Knight, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                    self.legal_moves.extend([(SeperatedX + SeperatedY)])
        if Down:
            for Seperate_Down_Moves in Down_Moves:
                SeperatedX = X[Seperate_Down_Moves[0]]
                SeperatedY = Y[Seperate_Down_Moves[1]]
                if super(Knight, self).check_for_pieces((SeperatedX + SeperatedY), self.color) != -1 and (SeperatedX + SeperatedY) not in self.legal_moves:
                    self.legal_moves.extend([(SeperatedX + SeperatedY)])
        for var in self.legal_moves:
            if super(Knight, self).in_check(self.color, king.pos) == 1:
                self.legal_moves.remove(var)
        return self.legal_moves


class Pawn(Board):
    def __init__(self, pos, color: str):
        super(Pawn, self).__init__()
        self.legal_moves = []
        self.color = color[0].lower()
        self.pos = pos
        self.captureable = False
        super().positions[pos] = color + 'p'

    def Legal_Moves(self, king):
        xPos2 = X.index(self.pos[0])
        yPos2 = Y.index(self.pos[1])
        Capture_Moves = {'w': ((xPos2 + 1, yPos2 + 1), (xPos2 - 1, yPos2 + 1)), 'b': ((xPos2 + 1, yPos2 - 1), (xPos2 - 1, yPos2 - 1))}
        Start_Moves = {'w': (xPos2, yPos2 + 2), 'b': (xPos2, yPos2 - 2)}
        Moves = {'w': (xPos2, yPos2 + 1), 'b': (xPos2, yPos2 - 1)}
        if 8 > Moves[self.color][1] > -1 and super(Pawn, self).check_for_pieces((X[Moves[self.color][0]] + Y[Moves[self.color][1]]), self.color) == 1:
            self.legal_moves.append((X[Moves[self.color][0]] + Y[Moves[self.color][1]]))
            conditional = True
        else:
            conditional = False
        if self.pos[1] == '2' and self.color == 'w' and conditional:
            self.legal_moves.append((X[Start_Moves[self.color][0]] + Y[Start_Moves[self.color][1]]))
        if self.pos[1] == '7' and self.color == 'b' and conditional:
            self.legal_moves.append((X[Start_Moves[self.color][0]] + Y[Start_Moves[self.color][1]]))

        for moves in Capture_Moves[self.color]:
            if 8 > moves[0] > -1 or 8 > moves[1] > -1:
                if super(Pawn, self).check_for_pieces((X[moves[0]-1] + Y[moves[1]-1]), self.color) == 0:
                    self.legal_moves.append((X[moves[0]-1] + Y[moves[1]-1]))
                    self.captureable = True




        for var in self.legal_moves:
            if super(Pawn, self).in_check(self.color, king.pos) == 1:
                self.legal_moves.remove(var)
        return self.legal_moves

    def promote(self):
        if self.color == 'w' and self.pos[1] == '8':
            ans = input('Which piece do you want to promote to?')
            legal = ('q', 'n', 'b', 'r')
            while ans[0].lower() not in legal:
                ans = input('Which piece do you want to promote to?')
            Board.positions[self.pos] = self.color + ans
            if ans == 'q':
                self.__class__ = Queen




av = Board()
a = King('e7', 'white')
d = Queen('e8', 'white')
d.Legal_Moves(a)
Board.black_legal_moves[d] = d.legal_moves
print(d.__class__)
print(d.pos)
print(d)
d.Legal_Moves(a)
print(d.legal_moves)

