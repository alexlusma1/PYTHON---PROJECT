Create a function that takes in two parameters: rows, and columns, both of which are integers. 
The function should then proceed to draw a playing board
the same number of rows and columns as specified. After drawing the board, your function should return True.



def draw_board(rows, columns):
    for row in range(rows):
        # Print the horizontal lines
        print(" ---" * columns)
        
        # Print the vertical lines
        print("|   " * (columns + 1))
    
    # Print the bottom horizontal line
    print(" ---" * columns)
    
    return True

# Example usage:
rows = 3
columns = 3
draw_board(rows, columns)
