import numpy as np

def spiral_matrix_generator(n):
    if n < 1:
        return []

    matrix = [[0] * n for _ in range(n)]
    row, col, direction = 0, 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(n * n):
        matrix[row][col] = i + 1
        next_row, next_col = row + directions[direction][0], col + directions[direction][1] 

        if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
            direction = (direction + 1) % 4

        row += directions[direction][0]
        col += directions[direction][1]

    return np.array(matrix)

print(spiral_matrix_generator(5))