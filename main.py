from Game import Board, Spot

class UltimateTicTacToe:

    def __init__(self):

        self.board = Board()
        self.game_state = True

    def pvp(self):
        
        print("Enter global coordinates")
        gx = input()
        gy = input()

        self.board.set_global_coord(gx, gy)

        while self.game_state:
            
            for i in range(3):
                for j in range(3):
                    if isinstance(self.board.board[i][j], Spot):
                        self.board.board[i][j].draw_board()
                    else:
                        print(self.board.board[i][j])
                print("\n")
            while (self.board.gx == -1 and self.board.gy == -1):
                
                # ask to enter global coords again and check if they are valud
                print("Enter global coordinates")

                gx = input()
                gy = input()
                self.board.set_global_coord(gx, gy)

            print("Enter local coordinates for global spot {}, {}".format(self.board.gx, self.board.gy))

            spot = self.board.board[self.board.gx][self.board.gy]
            x = input()
            y = input()

            spot.make_move(x, y, 'X' if self.board.player else 'O')
            
            self.board.set_global_coord(x, y)
            self.board.resolve_ttt_boards()

            state = self.board.get_board_state()

            if state == 1 or state == -1:
                
                self.game_state = False

                print("Game is over!")
                    
            self.board.change_player()   

            


if __name__ == '__main__':

    UTTT = UltimateTicTacToe()

    UTTT.pvp()