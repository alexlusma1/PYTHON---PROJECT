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