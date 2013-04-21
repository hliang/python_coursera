# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """
        (Rat, str, int, int) -> NoneType
        symbol of the rat displayed,
        location of the rat,
        number of sprouts eaten by the rat
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, newrow, newcol):
        """
        (Rat, int, int) -> NoneType
        Set the rat's row and col instance variables to the given row and column.
        """
        self.row = newrow
        self.col = newcol
 
    def eat_sprout(self):
        """
        (Rat) -> NoneType
        Add one to the rat's instance variable num_sprouts_eaten.
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        (Rat) -> str
        Return a string representation of the rat, in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.
        For example: 'J at (4, 3) ate 2 sprouts.'
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)
       
class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """
        (Maze, list of list of str, Rat, Rat) -> NoneType
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0
        for r in range(len(maze)):
            for c in range(len(maze[r])):
                if maze[r][c] == SPROUT:
                    self.num_sprouts_left += 1

    def is_wall(self, row, col):
        """
        (Maze, int, int) -> bool
        Return True if and only if there is a wall at the given row and column of the maze.
        """
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """
        (Maze, int, int) -> str
        Return the character in the maze at the given row and column. If there is a rat at that location, then its character should be returned rather than HALL.
        """
        if row == self.rat_1.row and col == self.rat_1.col:
            return RAT_1_CHAR
        if row == self.rat_2.row and col == self.rat_2.col:
            return RAT_2_CHAR
        return self.maze[row][col]

    def move(self, rat, vertical_move, horizontal_move):
        """
        (Maze, Rat, int, int) -> bool
        Move the rat in the given direction, unless there is a wall in the way. Also, check for a Brussels sprout at that location and, if present:
        * have the rat eat the Brussels sprout,
        * make that location a HALL, and
        * decrease the value that num_sprouts_left refers to by one.
        Return True if and only if there wasn't a wall in the way.
        """
        # location player intends to move into
        tobe_pos_row = rat.row + vertical_move
        tobe_pos_col = rat.col + horizontal_move
        # move will be successful if the intended location is not a wall
        if not self.maze[tobe_pos_row][tobe_pos_col] == WALL:
            # move rat into new location
            rat.set_location(tobe_pos_row, tobe_pos_col)
            # eat sprout if there is one there
            if self.maze[tobe_pos_row][tobe_pos_col] == SPROUT:
                rat.eat_sprout()
                self.maze[tobe_pos_row][tobe_pos_col] = HALL
                self.num_sprouts_left -= 1
            return True # move successful

    def __str__(self):
        """
        (Maze) -> str
        Return a string representation of the maze, using the format shown in this example
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        maze_sum = ''
        for r in range(len(self.maze)):
            for c in range(len(self.maze[r])):
                maze_char_in_sum = self.get_character(r, c)
                # if there is a mouse in there
                if r == self.rat_1.row and c == self.rat_1.col:
                    maze_char_in_sum = self.rat_1.symbol
                elif r == self.rat_2.row and c == self.rat_2.col:
                    maze_char_in_sum = self.rat_2.symbol
                maze_sum += maze_char_in_sum
            maze_sum += '\n'
        maze_sum += '{0} at ({1}, {2}) ate {3} sprouts.\n'.format(self.rat_1.symbol, self.rat_1.row, self.rat_1.col, self.rat_1.num_sprouts_eaten) + '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.rat_2.symbol, self.rat_2.row, self.rat_2.col, self.rat_2.num_sprouts_eaten)
        return maze_sum

