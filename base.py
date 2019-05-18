class Board:
    black = False
    white = True
    def __init__(self):
        self.state = [[Pawn(Board.white) for _ in range(8)]] + \
                     [[None] * 8 for _ in range(6)] + \
                     [[Pawn(Board.black) for _ in range(8)]]

    def get_piece(self, x, y):
        return self.state[y][x]

    def get_all_moves(self, is_white):
        for y, row in enumerate(self.state):
            for x, piece in enumerate(row):
                if piece and piece.is_white == is_white:
                    for move in piece.get_moves(self, x, y):
                        yield move

    def move_piece(self, start, end):
        xi, yi = start
        xf, yf = end
        self.state[yf][xf] = self.state[yi][xi]
        self.state[yi][xi] = None

    def __str__(self):
        rows = ["  abcdefgh"]
        for idx, row in enumerate(self.state):
            row_str = [str(piece) if piece else " " for piece in row]
            rows.append(f"{idx} {''.join(row_str)}")
        return "\n" + "\n".join(rows[::-1])

class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def get_moves(self):
        # returns list of valid board positions
        raise NotImplementedError()

class Pawn(Piece):
    
    def get_moves(self, board, x, y):
        # now this specifies board position
        # TODO Fix range to be within board limits
        if self.is_white and not board.get_piece(x, y + 1):
            return [(x, y + 1)] 
        elif not self.is_white and not board.get_piece(x, y - 1):
            return [(x, y - 1)]
        return []

    def get_attacks(self, board, x, y):
        pass 
    
    def __str__(self):
        return "P"

def main():
    board = Board()
    moves = board.get_all_moves(Board.white)
    print(list(moves))
    print(board)
    board.move_piece((1, 0), (1, 1))
    print(board)


main()



