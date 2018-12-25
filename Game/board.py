"""
board class for uttt
"""
from .spot import Spot

class Board:

    def __init__(self):

        self.board = [[Spot() for _ in range(3)] for _ in range(3)]
        self.player = True  # True for X, False for O
        self.gx = -1
        self.gy = -1

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                ttt = self.board[i][j]
                if isinstance(ttt, Spot):
                    print(ttt.tttboard, end='')
                    # for index, item in enumerate(ttt.tttboard):
                    #     print(item, end='')
                    #     if not index % 3:
                    #         print()
                else:
                    print(ttt)
            print("\n\n")

    def change_player(self):

        self.player = not self.player

    def is_global_coord_valid(self, gx, gy):
        
        if isinstance(self.board[gx][gy], Spot):
            
            return True

        return False

    def set_global_coord(self, gx, gy):
    
        if self.is_global_coord_valid(gx, gy):
            
            self.gx = gx
            self.gy = gy

        else:
            
            self.gx = -1
            self.gy = -1

    def resolve_ttt_boards(self):
        
        for i in range(3):
            for j in range(3):
                
                ttt_board = self.board[i][j]

                if isinstance(ttt_board, Spot):
                    
                    state = ttt_board.get_ttt_state()

                    if state == 1:
                        
                        self.board[i][j] = 'X' if self.player else 'O'

                    elif state == -1:
                        
                        self.board[i][j] = 'D'

    def get_board_state(self):
        
        if self.check_diagonals() or self.check_columns() or self.check_rows():
            
            return 1

        for i in range(3):
            for j in range(3):
                
                if isinstance(self.board[i][j], Spot):

                    return 0 

        return -1

    def check_rows(self):

        for i in range(3):
            
            piece = self.board[i][0]

            if piece == self.board[i][1] and piece == self.board[i][2] and piece != 'D':
                
                return True

        return False

    def check_columns(self):
        
        for i in range(3):
            
            piece = self.board[0][i]

            if piece == self.board[1][i] and piece == self.board[2][i] and piece != 'D':
                
                return True

        return False


    def check_diagonals(self):

        center = self.board[1][1]

        if center == self.board[0][0] and center == self.board[2][2] and center != 'D':

            return True

        elif center == self.board[2][0] and center == self.board[0][2] and center != 'D':

            return True

        return False