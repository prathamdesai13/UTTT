from Game import Board, Spot

class UltimateTicTacToe:

    def __init__(self):

        self.board = Board()
        self.game_state = True

    def global_input(self):
        
        print("Player {} please enter global coordinates: ".format(1 if self.board.player else 2))
        gx = input()
        gy = input()

        return gx, gy

    def pvp(self):
        # assuming every move made is legal (really this is just meant for the ai)
        gx, gy = self.global_input()

        self.board.set_global_coord(gx, gy)

        while self.game_state:
            
            self.board.draw_board()
            while (self.board.gx == -1 and self.board.gy == -1):
                
                # ask to enter global coords again and check if they are valud
                gx, gy = self.global_input()

                self.board.set_global_coord(gx, gy)

            print("Enter local coordinates for global spot {}, {}".format(self.board.gx, self.board.gy))

            spot = self.board.board[self.board.gx][self.board.gy]
            
            x = input()
            y = input()

            spot.make_move(x, y, 'X' if self.board.player else 'O')
            
            self.board.resolve_ttt_boards()
            self.board.set_global_coord(x, y)

            state = self.board.get_board_state()

            if state == 1 or state == -1:
                
                self.game_state = False

                print("Game is over!")

                if state == 1:
                    print("Player {} wins!".format(1 if self.board.player else 2))

                else:
                    print("Draw!")
                    
            self.board.change_player()   

        self.board.

if __name__ == '__main__':

    UTTT = UltimateTicTacToe()

    UTTT.pvp()