"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    print 'input line ' + str(line)
    result = list()
    if len(line)==1:
        result = line
    else:
        lst = list()
        for dummy_num in line:
            if dummy_num != 0:
                lst.append(dummy_num)
        skip_pos = False
        for dummy_index in range(len(lst)-1):
            if not skip_pos:
                if (lst[dummy_index] != 0)and(lst[dummy_index] == lst[dummy_index+1]):
                    result.append(2*lst[dummy_index])
                    skip_pos = True
                else:
                    result.append(lst[dummy_index])
                    skip_pos=False
            else:
                skip_pos = False
        if (not skip_pos) and (len(lst)>0):
            result.append(lst[-1])
        if len(result) < len(line):
            for dummy_i in range(len(line)-len(result)):
                result.append(0)
    print "output : " + str(result)  
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = list()
        self._base_line = dict()
        self.reset()
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        print 'reset'
        self._cells = [[0 for dummy_x in range(self._grid_width)] 
                       for dummy_y in range(self._grid_height)]
        self.new_tile()
        self.new_tile()
        up_line = list()
        down_line = list()
        left_line = list()
        right_line = list()
        for col in range(self.get_grid_width()):
            up_line.append([0, col])
            down_line.append([self.get_grid_height()-1, col])
        for row in range(self.get_grid_height()):
            left_line.append([row, 0])
            right_line.append([row, self.get_grid_width()-1])
        self._base_line[UP] = up_line
        self._base_line[DOWN] = down_line
        self._base_line[LEFT] = left_line
        self._base_line[RIGHT] = right_line
        print self
        print up_line, down_line 
        print left_line, right_line
        print 'reset done'
        
                
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        max_row = self.get_grid_height()
        max_col = self.get_grid_width()
        result = ''
        for dummy_row in range(max_row):
            result+= ' '.join(str(self.get_tile(dummy_row, dummy_col)) 
                              for dummy_col in range(max_col))
            result+='\n'  
        return result
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        print 'new run'
        legal_move = False
        if direction == LEFT or direction == RIGHT:
            max_col = self.get_grid_height()
            max_row = self.get_grid_width()
        else:
            max_col = self.get_grid_width()
            max_row = self.get_grid_height()
            
            
        for dummy_col in range(max_col):            
            lst = list()
            line = list()
            for dummy_row in range(max_row):
                print 'baseline:' + str(self._base_line[direction])
                print 'dummy_col %d' % dummy_col
                print 'dummy_row %d' % dummy_row
                print 'offsets: %s' % str(OFFSETS[direction])
                print self.get_grid_width(), self.get_grid_height()
                col = self._base_line[direction][dummy_col][0]+OFFSETS[direction][0]*dummy_row
                row = self._base_line[direction][dummy_col][1]+OFFSETS[direction][1]*dummy_row
                print 'col, row:'
                lst.append([col, row])
                print ' move: %d;%d' % (col,row)
                line.append(self.get_tile(col,row))
            merged = merge(line)
            for dummy_row in range(len(lst)):
                if self.get_tile(lst[dummy_row][0],lst[dummy_row][1]) != merged[dummy_row]:
                    legal_move = True    
                self.set_tile(lst[dummy_row][0],lst[dummy_row][1],merged[dummy_row])
        if legal_move:   
            self.new_tile()
               
    def new_tile(self): 
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        print 'start add new tile'
        col = random.randrange(self.get_grid_width())
        row = random.randrange(self.get_grid_height())
        if self.get_tile(row, col) != 0:
            while self.get_tile(row, col) != 0:
                col = random.randrange(self._grid_width)
                row = random.randrange(self._grid_height)
#                print ' Row:Col: %d:%d'%(row, col)
#        print 'generate Row:Col: %d:%d'%(row, col)
        dummy_i = random.randrange(100)        
        if dummy_i<90: 
            self.set_tile(row, col,2)
        else:
            self.set_tile(row, col,4) 
        print 'End add new tile'

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value
                
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        value = self._cells[row][col]
        return value


poc_2048_gui.run_gui(TwentyFortyEight(4, 5))

