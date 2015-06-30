"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    The function should play a game starting with the given player 
    by making random moves, alternating between players.
    """
    while board.check_win() is None:
        coords = mc_move(board, player, 1) 
        board.move(coords[0], coords[1], player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player): 
    """
    The function should score the completed board and update 
    the scores grid. As the function updates the scores grid directly,
    it does not return anything,
    """
    winner = board.check_win()
    if winner != provided.DRAW:
        if winner == player:
            added_score, substract_score = SCORE_CURRENT, SCORE_OTHER
        else:
            added_score, substract_score = SCORE_OTHER, SCORE_CURRENT
        dim = board.get_dim()
        for col in range(dim):
            for row in range(dim):
                square = board.square(row,col)
                if square != 1:
                    if  square == winner:
                        scores[row][col] += added_score
                    else:
                        scores[row][col] -= substract_score
        print scores

def get_best_move(board, scores):
    """
    The function should find all of the empty squares with the maximum score 
    and randomly return one of them as a (row, column) tuple.
    """
    result = tuple([0, 0],)
    max_scores = -500
    empty_squares = board.get_empty_squares()
    for coords in empty_squares:
        col = coords[1]
        row = coords[0]
        if max_scores < scores[row][col]:
            result = ((row, col),)
            max_scores = scores[row][col]
        elif max_scores == scores[row][col]:
            result += (coords,)
    if len(result)>1:
        return result[random.randrange(len(result))]
    else: 
        return tuple(result[0])
    
def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, 
    and the number of trials to run.
    """
    print 'player %d' % player
    result = board.get_empty_squares()
    if len(result)>1:
        # Check own win
        for coords in result:
            duplicate = board.clone()
            print '----'
            print duplicate
            duplicate.move(coords[0], coords[1], player)
            print duplicate
            if (duplicate.check_win()) == player:
                print 'find!'
                return coords

        # Check other win
        for coords in result:
            another = provided.switch_player(player) 
            duplicate = board.clone()
            print '----'
            print duplicate
            duplicate.move(coords[0], coords[1], another)
            print duplicate
            if (duplicate.check_win()) == another:
                print 'find other!'
                return coords

            
        print 'random'    
        return result[random.randrange(len(result))]
    else: 
        return tuple(result[0])
    
      
print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX, NTRIALS)
#print mc_move(main_board, provided.PLAYERX, NTRIALS)