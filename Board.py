#
# 
#
# A Connect Four Board class
#
# 
#


class Board:
    
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    


    def __repr__(self):
        
        """ Returns a string representation of a Board object.
        """
        s = ''         # begin with an empty string

        
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
       
            
       
        for c in range(2*self.width + 1):
            s += '-'
            
        s += '\n' 
        
        
        for r in range(1):
            s += ' '
            
            for c in range(self.width):
                
                if c %10 >= 1:
                    c = c%10
                elif c%10 == 0:
                    c = 0
                s += str(c) +  ' '
            
        return s

    def add_checker(self, checker, col):
        
        
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
       
        
        a = self.height - 1
        
        while self.slots[a][col] != ' ' :
                
               a -= 1       
               
        self.slots[a][col] = checker
   
    
    def add_checkers(self, colnums):
        
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    
    def  __init__(self, height, width):
        
        """constructs a new Board object by initializing the following three attributes:

            an attribute height that stores the number of rows in the board,
            as specified by the parameter height

            an attribute width that stores the number of columns in the board, 
            as specified by the parameter width

            an attribute slots that stores a reference to a two-dimensional 
            list with height rows and width columns that will be used to store 
            the current contents of the board."""
            
        
        self.height = height
        self.width = width    
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def reset(self):
        
        """returns a string representing a Board object."""
        
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = ' '
        return        
                
    def can_add_to(self, col) :
        
        
        """returns True if it is valid to place a checker in the column
        col on the calling Board object. Otherwise, it should return False."""
        
        
        if col < 0 :
            return False
        elif col > self.width - 1 :
            return False
        
        a = self.slots[0][col]
        
        if a == ' ' :
            return True
        else:
            return False
        
    def is_full(self):
        
         """returns True if the called Board object 
        is completely full of checkers, and returns False otherwise."""
         
         a = 0
         for c in range(self.width):
             if self.can_add_to(c) == True:
                 a += 1
                 
         if a == 0 :
             return True
         else:
             return False
         
    def remove_checker(self, col):
        
        """removes the top checker from column col of the called Board object. 
        If the column is empty, then the method should do nothing."""
        
       
        
        for r in range(self.height):
        
           if self.slots[r][col] != ' ' :
                
            
             self.slots[r][col] = ' '
           
             break
        
        
    def is_horizontal_win(self, checker):
        
     """ Checks for a horizontal win for the specified checker.
         """
         
     for row in range(self.height):
        for col in range(self.width - 3):
            # Checks if the next four columns in this row
            # contain the specified checker.
            if self.slots[row][col] == checker and \
               self.slots[row][col + 1] == checker and \
               self.slots[row][col + 2] == checker and \
               self.slots[row][col + 3] == checker:
                return True

    # if we make it here, there were no horizontal wins
     return False   


    def is_vertical_win(self, checker):
        
     """ Checks for a vertical win for the specified checker.
    """
    
     for row in range(self.height - 3):
        for col in range(self.width):
            # Check if the next four columns in this row
            # contain the specified checker.
            if self.slots[row][col] == checker and \
               self.slots[row + 1][col] == checker and \
               self.slots[row + 2][col] == checker and \
               self.slots[row + 3][col] == checker:
                return True

    # if we make it here, there were no horizontal wins
     return False  
 
    def is_diagonal_win(self, checker):
        
     """ Checks for a horizontal win for the specified checker.
    """
    
     for row in range(self.height - 3):
        for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
            if self.slots[row][col] == checker and \
               self.slots[row - 1][col + 1] == checker and \
               self.slots[row -2 ][col + 2] == checker and \
               self.slots[row - 3][col + 3] == checker:
                return True
            
     for row in range(self.height-3):
        for col in range(3,self.width):      
            if self.slots[row][col] == checker and \
               self.slots[row + 1][col - 1] == checker and \
               self.slots[row  + 2 ][col - 2] == checker and \
               self.slots[row + 3][col - 3] == checker:
                
                return True
    # if we make it here, there were no horizontal wins
     return False
 
    def is_win_for(self, checker):
        
        """accepts a parameter checker that is either 'X' or 'O', and returns
        True if there are four consecutive slots 
        containing checker on the board. Otherwise, it should return False."""
        
        assert(checker == 'X' or checker == 'O')
        
        if self.is_vertical_win(checker) == True:
            return True
        
        elif self.is_horizontal_win(checker) == True:
            return True
        
        elif self.is_diagonal_win(checker) == True :
           return True
       
        else:
            return False