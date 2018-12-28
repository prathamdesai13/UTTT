from Game.board import Board
from Game.spot import Spot
from Agents.Randy import Randy
from Agents.Nancy import Nancy

class UltimateTicTacToe:

    def __init__(self):

        self.Board = Board()
        self.game_state = True

    def reset_board(self):
        self.Board = Board()
        self.game_state = True

    def global_input(self):
        
        print("Player {} please enter global coordinates: ".format(1 if self.Board.player else 2))
        gx = int(input())
        gy = int(input())

        return gx, gy

    def pvp(self):
        # assuming every move made is legal (really this is just meant for the ai)
        gx, gy = self.global_input()

        self.Board.set_global_coord(gx, gy)

        while self.game_state:
            
            self.Board.draw_board()
            while (self.Board.gx == -1 and self.Board.gy == -1):
                
                # ask to enter global coords again and check if they are valid
                gx, gy = self.global_input()

                self.Board.set_global_coord(gx, gy)

            print("Player {}, enter local coordinates for global spot {}, {}".format(1 if self.Board.player else 0,  self.Board.gx, self.Board.gy))

            spot = self.Board.board[self.Board.gx][self.Board.gy]

            x = int(input())
            y = int(input())

            spot.make_move(x, y, 'X' if self.Board.player else 'O')
            
            self.Board.resolve_ttt_boards()
            self.Board.set_global_coord(x, y)

            state = self.Board.get_board_state()

            if state == 1 or state == -1:
                
                self.game_state = False

                print("Game is over!")

                if state == 1:
                    print("Player {} wins!".format(1 if self.Board.player else 2))

                else:
                    print("Draw!")
                    
            self.Board.change_player()   

        self.Board.draw_board()

    def pvc(self, agent):

        gx, gy = self.global_input()
        self.Board.set_global_coord(gx, gy)

        while self.game_state:

            self.Board.draw_board()
            while(self.Board.gx == -1 and self.Board.gy == -1):
                if self.Board.player: # human player
                    gx, gy = self.global_input()
                else: # not human player
                    gx, gy = agent.make_global_move(self.Board)

                self.Board.set_global_coord(gx, gy)
                print("Global Move perfomed by Player {} is : {}, {}".format(1 if self.Board.player else 0, self.Board.gx, self.Board.gy))
            print("Player {}, enter local coordinates for global spot {}, {}".format(1 if self.Board.player else 0,  self.Board.gx, self.Board.gy))
            spot = self.Board.board[self.Board.gx][self.Board.gy]

            if self.Board.player: # if human player
                x = int(input())
                y = int(input())

            else:
                x, y = agent.make_local_move(self.Board)
            
            spot.make_move(x, y, 'X' if self.Board.player else 'O')
            print()
            print("Local Move perfomed by Player {} is : {}, {}".format(1 if self.Board.player else 0, x, y))
            self.Board.resolve_ttt_boards()
            self.Board.set_global_coord(x, y)

            state = self.Board.get_board_state()

            if state == 1 or state == -1:
                self.game_state = False
                print("Game is over!")

                if state == 1:
                    print("Player {} wins!".format(1 if self.Board.player else 2))

                else:
                    print("Draw!")
            self.Board.change_player()   

        self.Board.draw_board()
        
    def train(self, agent1, agent2, num_episodes=10):
        episode = 0
        episodes_won = 0
        while episode < num_episodes:
            gx, gy = agent1.make_global_move(self.Board)
            self.Board.set_global_coord(gx, gy)

            while self.game_state:

                self.Board.draw_board()
                while(self.Board.gx == -1 and self.Board.gy == -1):
                    if self.Board.player: # agent 1
                        gx, gy = agent1.make_global_move(self.Board)
                    else: # agent2
                        gx, gy = agent2.make_global_move(self.Board)

                    self.Board.set_global_coord(gx, gy)
                    print("Global Move perfomed by Agent {} is : {}, {}".format(1 if self.Board.player else 2, self.Board.gx, self.Board.gy))
                print("Agent {}, enter local coordinates for global spot {}, {}".format(1 if self.Board.player else 2,  self.Board.gx, self.Board.gy))
                spot = self.Board.board[self.Board.gx][self.Board.gy]

                if self.Board.player: # if human player
                    x, y = agent1.make_local_move(self.Board)
                else:
                    x, y = agent2.make_local_move(self.Board)
            
                spot.make_move(x, y, 'X' if self.Board.player else 'O')
                print()
                print("Local Move perfomed by Agent {} is : {}, {}".format(1 if self.Board.player else 2, x, y))
                self.Board.resolve_ttt_boards()
                self.Board.set_global_coord(x, y)

                state = self.Board.get_board_state()

                if state == 1 or state == -1:
                    self.game_state = False
                    print("Game {} is over!".format(episode))
                    episode += 1
                    if state == 1:
                        print("Agent {} wins!".format(1 if self.Board.player else 2))
                        if not self.Board.player:
                            # add rewards and gradient defs here for nancy
                            episodes_won += 1
                            pass
                        else:
                            #idk
                            pass
                    else:
                        print("Draw!")
                self.Board.change_player()   
            self.reset_board()
        print(episodes_won)
        self.Board.draw_board()

if __name__ == '__main__':

    UTTT = UltimateTicTacToe()
    nancy = Nancy()
    randy = Randy()
    UTTT.train(randy, nancy)