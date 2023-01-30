#
# 
#
# Playing the game 
#   

from Board import Board
from Player import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the Player class or a subclass of Player).
          One player should use 'X' checkers and the other should
          use 'O' checkers.
    """
    
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p, b):
    
    """takes two parameters: a Player object p for the player whose move is
    being processed, and a Board object b for the board on which the game is being played."""
    
    Player.__repr__(p)
    Board.__repr__(b)
    
    player = p.__repr__()
    print(player + '\'s'  , 'turn')
    a = p.checker
    move = p.next_move(b)
    
    print(a)
    add_move = b.add_checker(a, move)
    
    print(b)
    
    c = b.is_win_for(p.checker)
    d = b.is_win_for(p.opponent_checker())
    
    
    
    
    if c == True  :
        
        print(str(p.__repr__()) + '  ' + 'wins' + ' ' +  'in' + "  " + str(p.num_moves) + "  " + 'moves' )
        return True
    elif b.is_full() == True and c != True and d != True:
        print( 'It\'s a tie!' )
        return True
    else:
        return False
    

    
    
class  RandomPlayer(Player):
    
     """can be used for an unintelligent computer player that chooses at 
       random from the available columns"""
    
     def indice_available (self, b):
         
         """Creates an index of all possible legal moves possible"""
         a = []
         
         for i in range(b.width):
             if b.can_add_to(i) == True:
                 a += [i]
         return a     
     
     
     def next_move(self, b):
         
         """choose at random from the columns in the board b 
         that are not yet full, and return the index of that randomly selected column"""
         
         nextchoice = random.choice(self.indice_available(b))
         
         self.num_moves += 1
         return nextchoice
         
     
