#
# 
#
# A Connect-Four Player class 
#
# 


from Board import Board



class Player :
    
    def __init__(self, checker):
        
        """constructs a new Player object by initializing the following two attributes:

            an attribute checker – a one-character string that represents the\
            gamepiece for the player, as specified by the parameter checker

            an attribute num_moves – an integer that stores how many moves the player
            has made so far. This attribute should be initialized to zero to signify that 
            the Player object has not yet made any Connect Four moves."""
        
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self) :
        
        """returns a string representing a Player object"""
        
        
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        
        """returns a one-character string representing 
        the checker of the Player object’s opponent. """
        
        if self.checker == 'X' :
            opponent_checker = 'O'
        else:
            opponent_checker = 'X'
        return opponent_checker    
    
    
    def  next_move(self, b):
        
        """ccepts a Board object b as a parameter and returns 
        the column where the player wants to make the next move"""
        
        choice = int(input('Enter a column: '))
        
        choice = int(choice)
        
        while b.can_add_to(choice) == False:
           
           print('Try Again!' )
           choice = int(input('Enter a column: '))
        
           choice = int(choice)
        
    
        self.num_moves += 1
        return choice
