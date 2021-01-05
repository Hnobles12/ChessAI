## Game and Board errors

class LocationRangeError(Exception):
    def  __init__(self, message="Location outside of game board."):
        self.message = message
        super().__init__(self.message)
        
class PieceNotFound(Exception):
    def  __init__(self, message="No piece with specified color found at specified location."):
        self.message = message
        super().__init__(self.message)

class InvalidMove(Exception):
    def  __init__(self, message="Invalid Move: ", add_info=""):
        self.message = message+add_info
        super().__init__(self.message)



class SpaceOccupied(InvalidMove):
    def  __init__(self, message="Ending location is occupied by another piece"):
        self.message = message
        super().__init__(add_info=self.message)