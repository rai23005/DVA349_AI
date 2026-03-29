
#Domains: The digits 1–9
from load_sudoku_from_file import load_sudoku_file


DOMAIN = list(range(1, 10))

#variabler: tomma cellpositioner (row, column)
def make_sudoku_grid ():
    
    
    variables = []
    for row in range(9):
        for col in range(9):
            variables.append((row, col))
    return variables

#kontroll om en siffra kan placeras i en viss position i Sudoku-rutnätet
def constraints_rule(sudoku_grid , row, col, num):
    
    # check if the number is already in the same row
    for check_colum in range(9):
        if sudoku_grid [row][check_colum] == num:
            return False

    # check if the number is already in the same column
    for check_row in range(9):
        if sudoku_grid [check_row][col] == num:
            return False

    # check 3x3-boxen
    box_row_start = row - row % 3
    box_col_start = col - col % 3
    for r in range(3):
        for c in range( 3):
            if sudoku_grid [box_row_start + r][box_col_start + c] == num:
                return False

    return True

def solve_with_variables(sudoku_grid , variables, idx=0):
    
    # alla variabler tilldelade,-> löst sudoku
    if idx == len(variables):
        return True  

    #next variable 
    row, col = variables[idx]

    #kontroll om cellen ej är noll, om så är det redan tilldelat en siffra, gå vidare till nästa variabel
    if sudoku_grid[row][col] > 0:
        return solve_with_variables(sudoku_grid, variables, idx + 1)
   

    for num in DOMAIN:
        if constraints_rule(sudoku_grid , row, col, num):
            sudoku_grid [row][col] = num
            
            if solve_with_variables(sudoku_grid , variables, idx + 1):
                return True
            
            # Går inte lösa-> backtrack
            sudoku_grid [row][col] = 0 
    return False

def print_sudoku(sudoku):
    variables = make_sudoku_grid()
    if not solve_with_variables(sudoku, variables):
        print("Could not solve the Sudoku.")
        return


    #Printa ut lösning 
    for row in range(len(sudoku)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - ")

        for col in range(len(sudoku[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
           
            value = sudoku[row][col]
            char = str(value) 

            if col == 8:
                print(char)
            else:
                print(char + " ", end="")


def start_lab():
    print("\n##################################################################################################\n")
    print("LAb 2 - Sudoku Solver")

    #load sudokus from file
    sudokus = load_sudoku_file("Assignment_2_sudoku.txt")


    for idx, sudoku in enumerate(sudokus):
        print(f"Solutions for Sudoku number {idx+1}:\n")
        print_sudoku(sudoku)
        print("\n")