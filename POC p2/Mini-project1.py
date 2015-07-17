"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        lst = list()
        self._human_list = list(lst,)
        self._zombie_list= list(lst,)
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col),)
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)     
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col),)
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        height = self.get_grid_height()
        width = self.get_grid_width()
        visited = poc_grid.Grid(height,width)
        distance_field = [[height * width for dummy_col in range(width)] 
                       for dummy_row in range(height)]
        boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            boundary_list = self._human_list
        elif entity_type == ZOMBIE:
            boundary_list = self._zombie_list
        else:
            print 'bad list'
        
        for cell in boundary_list:
            boundary.enqueue(cell)
            visited.set_full(cell[0],cell[1])
            distance_field[cell[0]][cell[1]]=0     
                                    
        while len(boundary)>0:
            current_cell = boundary.dequeue()
            distance = distance_field[current_cell[0]][current_cell[1]] + 1
            neighbor_cells = self.four_neighbors(current_cell[0],current_cell[1])
            for cell in neighbor_cells:
                if (visited.is_empty(cell[0],cell[1])) and (self.is_empty(cell[0],cell[1])):
                    visited.set_full(cell[0],cell[1])
                    distance_field[cell[0]][cell[1]] = distance
                    boundary.enqueue(cell)  
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for human_num in range(self.num_humans()):
            max_dist = 0
            human = self._human_list[human_num]
            move_list = list(human,)
            neighbor_cells = self.eight_neighbors(human[0],human[1])
            print 'neighbor_cells', neighbor_cells
            for cell in neighbor_cells:
                if (self.is_empty(cell[0],cell[1])):
                    dist = zombie_distance_field[cell[0]][cell[1]]
                    if dist > max_dist:
                        max_dist = dist
                        move_list = list(cell,)
                    elif dist == max_dist:
                        move_list.append(cell)
            self._human_list[human_num] = (move_list[0],move_list[1]) 
        print '[(0, 0)] needed in self._human_list[0]=', self._human_list[0]
        print 'move_list', move_list 
        return move_list          
            
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for zombie_num in range(self.num_zombies()):
            zombie = self._zombie_list[zombie_num]
            max_dist = human_distance_field[zombie[0]][zombie[1]]
            move_list = list(zombie,)
            neighbor_cells = self.four_neighbors(zombie[0],zombie[1])
            print 'neighbor_cells', neighbor_cells
            for cell in neighbor_cells:
                if (self.is_empty(cell[0],cell[1])):
                    dist = human_distance_field[cell[0]][cell[1]]
                    if dist < max_dist:
                        max_dist = dist
                        move_list = list(cell,)
                    elif dist == max_dist:
                        move_list.append(cell)
            self._zombie_list[zombie_num] = (move_list[0],move_list[1]) 
        print '[(0, 0)] needed in self._human_list[0]=', self._zombie_list[0]
        print 'move_list', move_list 
        return move_list 

    
    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        ans = ""
        for row in range(self._grid_height):
            ans += str(self._cells[row])
            ans += "\n"
        ans += 'Humans: ' + str(self._human_list)+ "\n"
        ans += 'Zombies: ' + str(self._zombie_list)+ "\n"
        return ans

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Apocalypse(30, 40))
