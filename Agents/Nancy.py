import numpy as np

class Nancy:

    def __init__(self):

        self.weights = [0] * 2
        self.weights[0] = np.random.randn(729, 81) / np.sqrt(81)
        self.weights[1] = np.random.randn(81, 729) / np.sqrt(729)
        self.biases = [np.random.randn(729, 1), np.random.randn(81, 1)]
        self.actions = []

    def make_local_move(self, board):
        board_vec = self.flatten(board.board)
        gx, gy = board.gx, board.gy
        spot = board.board[gx][gy]
        predicted_moves = self.predict_move(board_vec, gx, gy)
        # print(predicted_moves)
        pos = predicted_moves[0][1] % 9
        y = pos % 3
        x = pos // 3
        i = 1
        while not spot.is_move_valid(x, y):
            i += 1
            pos = predicted_moves[i][1] % 9
            y = pos % 3
            x = pos // 3
        return x, y
    
    def forward_pass(self, board_vec):

        hidden = np.dot(self.weights[0], board_vec.T) + self.biases[0]
        hidden_transform = self.sigmoid(hidden)
        log_probs = np.dot(self.weights[1], hidden_transform) + self.biases[1]
        prediction = self.sigmoid(log_probs.T)
        return prediction

    def backprop(self, grad):
        
        pass
        
    def predict_move(self, board_vec, gx, gy):
        predict = self.forward_pass(board_vec)
        x_start = 27 * gx
        y_start = 9 * gy
        tttboard_range = [x_start + y_start + i for i in range(9)]
        # print(tttboard_range)
        ttt_sample = predict[0][tttboard_range[0] : tttboard_range[-1] + 1]
        # print(ttt_sample)
        pairs = [(ttt_sample[i], tttboard_range[i]) for i in range(9)]
        pairs.sort(key=lambda x : x[0])
        return pairs
        
    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))
    def flatten(self, board):
        
        board_vec = np.zeros((3, 3, 3, 3))
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if board[i][j].tttboard[k][l] == 'X':
                            board_vec[i][j][k][l] = 1.0
                        elif board[i][j].tttboard[k][l] == 'O':
                            board_vec[i][j][k][l] = -1.0
        board_vec = np.reshape(board_vec, (1, 81))
        return board_vec

    def make_global_move(self, board):

        pass