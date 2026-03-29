def load_sudoku_file(file_path):
    all_sudokus = []
    num_for_sudoku = []

    with open(file_path,'r') as file:
        for line in file:
            line = line.strip()
            
           
            # Lägg till tidigare Sudoku i listan innan du börjar en ny
            if line.startswith('SUDOKU'):
                if num_for_sudoku:                    
                    all_sudokus.append(num_for_sudoku)
                num_for_sudoku = []
            
            elif line == 'EOF':
                if num_for_sudoku:
                    all_sudokus.append(num_for_sudoku)
                break
            
            # Är det siffor lägg till raden i num_for_sudoku
            elif line and line[0].isdigit():                
                row = [int(c) for c in line]
                num_for_sudoku.append(row)

    return all_sudokus