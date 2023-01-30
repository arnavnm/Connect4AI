#
# 
#
# AI Player for use in Connect Four   
#

import random  
from Connect4Base import *

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        """  constructs a new AIPlayer object
    """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        return 
    
        
    def __repr__(self) :
        
        """returns a string representing an AIPlayer object"""
        
        return 'Player ' + self.checker + ' ' + '(' + self.tiebreak + ',' + ' ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        
        """takes a list scores containing a score for each 
        column of the board, and that returns the index of the column with the maximum score"""
        
        a = max(scores)
        
        b =[]
        
        for i in range(len(scores)):
            
            if scores[i] == a :
                b += [i]
        
        
        if self.tiebreak == 'LEFT' :
            return b[0] 
        if self.tiebreak == 'RIGHT':
            return b[len(b)-1]
        else:
            return random.choice(b)
        
    def scores_for(self, b):
        
        """takes a Board object b and determines the called AIPlayer‘s scores for the columns in b."""
        
        scores = [50] * b.width
        
        for i in range(b.width):
            
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker) == True:
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[i] = 0    
            elif self.lookahead == 0 :
                scores[i] = 50
                
            else :
                b.add_checker(self.checker, i)
                
                opponent = AIPlayer( self.opponent_checker(), self.tiebreak ,   (self.lookahead -1) )
                
                opponent_score = opponent.scores_for(b)
                
                a = max(opponent_score)
                
                scores[i] = 100 - a
                        
                b.remove_checker(i)    
               
                
        return scores     
    
    
    def next_move(self, b):
        
        
        """return the called AIPlayer‘s judgment of its best possible move."""
        
        
        choice = self.max_score_column(self.scores_for(b))
        
        self.num_moves += 1
        return choice
                    
connect_four(AIPlayer('X', 'LEFT', 5), AIPlayer('O', 'LEFT', 1))