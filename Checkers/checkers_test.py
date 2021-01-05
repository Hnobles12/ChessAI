import checkers as c

board = c.Board()
board.generateBoard()

print(board.curr)


# for piece in board.piecies:
#     print(piece.__dict__)

board.movePiece('black',[2,1],[3,1])
print(board.curr)

# from checkers.errors import *

# try:
#     raise SpaceOccupied()
# except InvalidMove as err:
#     print(err.message)