import numpy as np

# THIS CODE WAS NO MADE BY ME

def spiral_matrix_generator(n):
    if n < 1:
        return []

    matrix = [[0] * n for _ in range(n)] # create a n x n matrix
    row, col, direction = 0, 0, 0 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up

    for i in range(n * n):
        matrix[row][col] = i + 1
        next_row, next_col = row + directions[direction][0], col + directions[direction][1] # next position

        if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):# if next position is out of bound or has been visited
            direction = (direction + 1) % 4 # change direction. n % m = n if n < m  else n % m = n - m if n >= m

        row += directions[direction][0] # update position
        col += directions[direction][1] # update position

    return np.array(matrix) # convert to numpy array

print(spiral_matrix_generator(5))