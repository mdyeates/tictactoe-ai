"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

# test_board = [
#     [O, O, EMPTY],
#     [X, X, EMPTY],
#     [X, EMPTY, EMPTY]
# ]

""" 
Visual guide
[(0, 0), (0, 1), (0, 2)] 
[(1, 0), (1, 1), (1, 2)]
[(2, 0), (2, 1), (2, 2)]
"""


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # X gets the first move
    if board == initial_state():
        return X
    
    x_count = 0
    o_count = 0
    
    for row in board:
        for letter in row:
            if letter == X:
                x_count += 1
            if letter == O:
                o_count += 1

    if x_count == o_count:
        return X
    
    if x_count > o_count:
        return O

# next_player = player(test_board)
# print(f"Next player: {next_player}")
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))
                
    return possible_actions

# possible_actions = actions(test_board)
# print(f"Possible actions: {possible_actions}")


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)

    if action not in actions(board):
        print("Invalid action:", action)
        print("Current board state:", board)
        raise Exception("Not a valid action")

    current_player = player(board)
    row, letter = action

    board_copy[row][letter] = current_player

    return board_copy

# action = (0, 2)
# result(test_board, action)

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not None:
        return board[2][0]
    
    return None

""" 
Visual guide
[(0, 0), (0, 1), (0, 2)] 
[(1, 0), (1, 1), (1, 2)]
[(2, 0), (2, 1), (2, 2)]
"""



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_game_over = winner(board)

    if is_game_over is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True

# terminal(test_board)
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    is_winner = winner(board)

    if X == is_winner:
        return 1
    elif O == is_winner:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board using alpha-beta pruning.
    """
    if terminal(board):
        return None

    current_player = player(board)
    alpha = -math.inf 
    beta = math.inf  

    best_value = -math.inf if current_player == X else math.inf
    best_action = None

    for action in actions(board):
        if current_player == X:
            value = min_value(result(board, action), alpha, beta)
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(alpha, value)
        else:
            value = max_value(result(board, action), alpha, beta)
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(beta, value)

        if alpha >= beta:
            break 

    return best_action

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action), alpha, beta))
        if value <= alpha:
            return value
        beta = min(beta, value)

    return value

def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action), alpha, beta))
        if value >= beta:
            return value
        alpha = max(alpha, value)

    return value
