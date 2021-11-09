"""


"""

import os

def prGreen(skk): return ("\033[92m{}\033[00m" .format(skk))

class KakuroBoard:
    """
    
    """

    def __init__(self, n_row, n_col):
        self.n_row = n_row
        self.n_col = n_col
        self.board = [['*' for row in range(n_col) ]for col in range(n_row)]
        self.solution_board = None
    
    def showEmptyBoard(self):
        """
        Print the empty board
        """
        print(self._show(self.board, 1))
    
    def showSolutionBoard(self):
        """
        Print the board solution 
        """
        if self.solution_board is not None:
            print(self._show(self.solution_board, 1))

    def _show(self, board, color):
        """
        Convert board to string
        """
        board_to_print = ""
        for i, line in enumerate(board):
            board_to_print += "\t"
            for j, element in enumerate(line):
                if element == '*':
                    board_to_print += "[ * ]\t"
                elif element == '_':
                    if color == 1:      
                        board_to_print += "[ " + prGreen("_") + " ]\t"  
                    else:
                        board_to_print += "[ _ ]\t" 
                elif isinstance(element, list):
                    tmp = str(element[0]) + "\\" + str(element[1])
                    board_to_print += f"{tmp:^5}" + "\t"
                else:
                    if color == 1:      
                        board_to_print += "[ " + prGreen(str(element)) + " ]\t"  
                    else:
                        board_to_print += "[ " + str(element) + " ]\t"  
            board_to_print += "\n"  
        return board_to_print

    def generate(self):
        """
        Generate the Kakuro Board
        """
        self.board = [['*', '*', '*', [23, ''], [4, '']],
           ['*', '*', [6, 11], '_', '_'],
           ['*', [3, 9], '_', '_', '_'],
           [['', 12], '_', '_', '_', '*'],
           [['', 4], '_', '_', '*', '*']]

        """
        [['*', '*', '*', [23, ''], [4, '']],
           ['*', '*', [6, 11], 8, 3],
           ['*', [3, 9], 2, 6, 1],
           [['', 12], 2, 1, 9, '*'],
           [['', 4], 1, 3, '*', '*']]
           """
    
    def load(self):
        """
        Load a new Kakuro Board
        """
        print("This is the current board:\n")
        self.showEmptyBoard()

        # Load the board proceeding by rows and then by columns
        print("Insert:\n\t* for a empty cell,\n\t_ for a empty cell to fill,\n\tvertical_sum/horizontal_sum for a sum cell (i.e. 4/ or /12 or 4/12).\n")
        for i, line in enumerate(self.board):
            for j, element in enumerate(line):
                ans = input("Insert in " + str(i) + ", " + str(j) + " : ")
                if '/' in ans: 
                    tmp = ans.split("/")
                    if tmp[0] != '':
                        tmp[0] = int(tmp[0])
                    if tmp[1] != '':
                        tmp[1] = int(tmp[1])
                    line[j] = [tmp[0], tmp[1]]
                else:
                    line[j] = ans
        

    def solve(self):
        """
        Solve the board and store the solution in self.solution_board
        """
        self.solution_board = self.board
        #Do something
        self.solution_board = [['*', '*', '*', [23, ''], [4, '']],
           ['*', '*', [6, 11], 8, 3],
           ['*', [3, 9], 2, 6, 1],
           [['', 12], 2, 1, 9, '*'],
           [['', 4], 1, 3, '*', '*']]
        
    def save(self, name):
        # Path 
        path = "../KakuroBoardSample/"
            
        # Create the directory 
        try: 
            os.mkdir(path) 
        except OSError as error: 
            #print(error)
            pass
        
        # File Content
        tmp = "The original board is:\n" + self._show(self.board, 0)
        if self.solution_board is not None:
            tmp += "\n\nThe solution is:\n" + self._show(self.solution_board, 0)
        
        # Write to file
        f = open(path + name + ".txt", "w")
        f.write(tmp)
        f.close()