import torch as t
from .errors import *

SYMBOLS = {'black': 1, 'white': 2}
FORWARD = {'black': 1, 'white': -1}


class Piece:
    def __init__(self, loc: list, color: str):
        self.loc = loc
        self.color = color
        self.is_king = False
        self.id = id(self)

    def move(self, new_loc):
        self.loc = new_loc


class Board(object):
    """
    Checkers Board with states.
    """

    def __init__(self):
        # init board tensor with zeros for empty space
        self.curr = t.zeros(8, 8, dtype=t.int)
        self.piecies = []
        self.focused_piece = None

    def movePiece(self, color: str, start_loc: list, end_loc: list) -> None:
        # Check locations for errors.
        if not 0 <= (start_loc[0] | start_loc[1] | end_loc[0] | end_loc[1]) <= 7:
            raise LocationRangeError()

        # Find piece on board
        piece_found = False

        for i in range(len(self.piecies)):
            if (self.piecies[i].loc == start_loc) and (self.piecies[i].color == color):
                piece_found = True
                break

        if not piece_found:
            raise PieceNotFound()
        else:
            self.focused_piece = self.piecies[i]
        # Check valid move
        # ...
        try:
            valid_mv = self.checkValidMove(end_loc)
            if not valid_mv:
                raise InvalidMove(add_info="Moving in this manner is illegal.")

        except InvalidMove as err:
            # Deal with invalid input
            print(err.message) ## TEMP
            # Game.print(err.message)
            return

        # Move piece
        self.piecies[i].move(end_loc)
        self.curr[start_loc[0], start_loc[1]] = 0
        self.curr[end_loc[0], end_loc[1]] = SYMBOLS[color]

        # Check for eliminated piecies and remove them.
        # ...
        return

    def generateBoard(self):
        # Setup black piecies
        for i in range(0, 3):

            if i % 2 != 0:
                start = 0
            else:
                start = 1

            for j in range(start, 8, 2):
                self.curr[i, j] = 1
                self.piecies.append(Piece([i, j], "black"))

        # Setup white piecies
        for i in range(5, 8):

            if i % 2 != 0:
                start = 0
            else:
                start = 1

            for j in range(start, 8, 2):
                self.curr[i, j] = 2
                self.piecies.append(Piece([i, j], "white"))

    def update(self):
        pass

    def checkValidMove(self, end_loc: list) -> bool:
        # Check if space is occupied
        for piece in self.piecies:
            if piece.loc == end_loc:
                raise SpaceOccupied()

        # Check if end location is in valid paths
        valid_paths = []

        # Forward + abs::right and forward + abs::left
        if 0 <= self.focused_piece.loc[0]+FORWARD[self.focused_piece.color] <= 7:
            if 0 <= self.focused_piece.loc[1]+1 <= 7:
                valid_paths.append([self.focused_piece.loc[0]+FORWARD[self.focused_piece.color], self.focused_piece.loc[1]+1])
            
            if 0 <= self.focused_piece.loc[1]-1 <= 7:
                valid_paths.append([self.focused_piece.loc[0]+FORWARD[self.focused_piece.color], self.focused_piece.loc[1]-1])

        
        if self.focused_piece.is_king:
            if 0 <= self.focused_piece.loc[1]+1 <= 7:
                valid_paths.append([self.focused_piece.loc[0]-FORWARD[self.focused_piece.color], self.focused_piece.loc[1]+1])
            
            if 0 <= self.focused_piece.loc[1]-1 <= 7:
                valid_paths.append([self.focused_piece.loc[0]-FORWARD[self.focused_piece.color], self.focused_piece.loc[1]-1])

        if end_loc in valid_paths:
            return True
        else:
            return False
