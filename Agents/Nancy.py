import numpy as np
import random
class Nancy:

    def __init__(self):

        self.learning_rate = 1e-4
        self.reward_discount = 0.99
        self.rewards = [] # rewards
        self.inputs = [] # inputs that Nancy uses to predict moves
        self.hidden_states = [] # hidden layer values
        self.actions = [] # predictions made by Nancy
        self.weights = [0] * 2
        self.weights[0] = np.random.randn(729, 81) / np.sqrt(81)
        self.weights[1] = np.random.randn(81, 729) / np.sqrt(729)
        self.biases = [np.random.randn(729, 1), np.random.randn(81, 1)]

    def make_local_move(self, board):
        gx, gy = board.gx, board.gy
        spot = board.board[gx][gy]
        if isinstance(spot, str):
            return self.make_global_move(board)

        board_vec = self.flatten(board.board)
        predicted_moves = self.predict_move(board_vec, gx, gy)
        # print(predicted_moves)
        pos = predicted_moves[0][1] % 9
        y = pos % 3
        x = pos // 3
        i = 1
        while not spot.is_move_valid(x, y):
            i += 1
            print(i)
            pos = predicted_moves[i][1] % 9
            y = pos % 3
            x = pos // 3
        return x, y
    
    def forward_pass(self, board_vec):

        hidden = np.dot(self.weights[0], board_vec.T) + self.biases[0]
        hidden_transform = self.sigmoid(hidden)
        self.hidden_states.append(hidden_transform)
        log_probs = np.dot(self.weights[1], hidden_transform) + self.biases[1]
        prediction = self.sigmoid(log_probs.T)
        self.actions.append(prediction)
        return prediction

    def backprop(self, pred, labels):
        
        prediction_grad = np.dot(grad, pred - grad)
        
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

    def sigmoid_grad(self, x):
        sig = self.sigmoid(x)
        return sig * (1.0 - sig)

    def flatten(self, board):
        
        board_vec = np.zeros((3, 3, 3, 3))
        for i in range(3):
            for j in range(3):
                spot = board[i][j]
                if not isinstance(spot, str):
                    for k in range(3):
                        for l in range(3):
                            if board[i][j].tttboard[k][l] == 'X':
                                board_vec[i][j][k][l] = 1.0
                            elif board[i][j].tttboard[k][l] == 'O':
                                board_vec[i][j][k][l] = -1.0
        board_vec = np.reshape(board_vec, (1, 81))
        return board_vec

    def make_global_move(self, board):
        # random for now till i figure something out
        rand_int = random.randint(0, 8)
        gy = rand_int % 3
        gx = rand_int // 3
        while not board.is_global_coord_valid(gx, gy):
            rand_int = random.randint(0, 8)
            gy = rand_int % 3
            gx = rand_int // 3
        
        return gx, gy