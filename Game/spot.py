"""
spot class
"""

class Spot:

    def __init__(self, x, y):
        
        self.tttboard = [[0] * 3 for _ in range(3)]  # mini tic tac toe board

    def draw_board(self):
        
        for i in range(3):
            print self.tttboard[i] 
        
    def make_move(self, x, y, piece):
        
        if self.is_move_valid(x, y):
            
            self.tttboard[x][y] = piece

    def is_move_valid(self, x, y):
        
        if self.tttboard[x][y] == 0:
            
            return True

        return False

    def get_ttt_state(self):
        
        if self.check_columns() or self.check_diagonals() or self.check_rows():
            
            return 1

        else:

            for i in range(3):
                for j in range(3):
                    
                    if self.tttboard[i][j] == 0:
                        
                        return 0

        return -1
            

    def check_rows(self):

        for i in range(3):
            
            piece = self.tttboard[i][0]
            if piece == self.tttboard[i][1] and piece == self.tttboard[i][2] and piece != 0:

                return True

        return False

    def check_columns(self):
    
        for i in range(3):
            
            piece = self.tttboard[0][i]
            if piece == self.tttboard[1][i] and piece == self.tttboard[2][i] and piece != 0:

                return True

        return False


    def check_diagonals(self):

        center = self.tttboard[1][1]

        if center == self.tttboard[0][0] and center == self.tttboard[2][2] and center != 0:

            return True

        elif center == self.tttboard[0][2] and center == self.tttboard[2][0] and center != 0:

            return True

        return False