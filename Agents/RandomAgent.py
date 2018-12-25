import random

class Randy:

    def __init__(self):

        pass

    def make_local_move(self, spot):
        # given the spot to be played in, generate random local move to play
        rand_int = random.randint(0, 8)
        y = rand_int % 3
        x = rand_int // 3
        while not spot.is_move_valid(x, y):
            rand_int = random.randint(0, 8)
            y = rand_int % 3
            x = rand_int // 3
        
        return x, y

    def make_global_move(self, board):
        # given the board, generate random global spot to play
        rand_int = random.randint(0, 8)
        gy = rand_int % 3
        gx = rand_int // 3
        while not board.is_global_coord_valid(gx, gy):
            rand_int = random.randint(0, 8)
            gy = rand_int % 3
            gx = rand_int // 3
        
        return gx, gy
    

    