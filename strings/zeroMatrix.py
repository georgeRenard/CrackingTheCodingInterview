import sys
import numpy as np
from time import time

#sys.tracebacklimit = 0

# Considerations for improvement
# -----------------------------------------------------------
# Why shouldn't we check a particular row/col for multiple 0s - Answer: that pretty much does not matter... unfortunately


sys.setrecursionlimit(10000)


def problem():
    """ 
    Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column are set to 0. 
    """ 



def zero_matrix(matrix, rows, columns):
    
    # __brute_force(matrix, rows, columns)
    #__brute_force_optimized_1(matrix, rows, columns)
    __optimal(matrix, rows, columns)

# This algorithm runs in O(c^r) complexity, it basically goes through the matrix and looks for 0 elements
# r is the number of rows
# c is the number of cols
# P.S I completely underestimated the runtime ~ the growth is way bigger since we clear out the rows and cols without skipping them later
# This one is garbage and it is not working
def __brute_force(matrix, row_size, col_size):

    for row in range(row_size):
        for col in range(col_size):
            if matrix[row][col] == 0:
                zero_out_row_col(matrix, row_size, col_size, row, col) 


# The idea behind this improvement is that we reduce the runtime of the algorithm by keeping track of the rows and cols that are cleared out
# Yet, this solution is O(n) in terms of memory
# We can probably do better using a bit vector
def __brute_force_optimized_1(matrix, row_size, col_size):

    cleared = set()

    for row in range(row_size):
        
        if row in cleared:
            continue

        for col in range(col_size):
            
            if col in cleared:
                break 
    
            if matrix[row][col] == 0:     
                zero_out_row_col(matrix, row_size, col_size, row, col)
                cleared.add(row)
                cleared.add(col) 
                break


# Instead of using a set we can use bit vectors that will make the memory requirements even less
# O(1) memory
def __optimal(matrix, row_size, col_size):

    row_bit_vector = 1 << row_size
    col_bit_vector = 1 << col_size 

    for row in range(row_size):

        # Check whether the row is already zeroed out
        mask = 1 << row
        if mask & row_bit_vector != 0:
            continue
     
        for col in range(col_size):
            
            # Check whether the col is already zeroed out
            mask = 1 << col
            if mask & col_bit_vector != 0:
                continue 

            if matrix[row][col] == 0:
                bit_vectors = [row_bit_vector, col_bit_vector]
                zero_out_row(matrix, bit_vectors, row_size, col_size, row, col)
                row_bit_vector = bit_vectors[0]
                col_bit_vector = bit_vectors[1]
                break
                

# Unfortunately we cannot pass references in python, this might destroy the desired memory complexity 
# This function runs in O(r + c) where r is the row size and c is the column size
# Basically, what happens here is we waste couple array traversals since we can have multiple 0s in a single column
def zero_out_row_col(matrix, row_size, col_size, row, col):

    for i in range(row_size):
        matrix[i][col] = 0


    for i in range(col_size):
        matrix[row][i] = 0
   

def zero_out_row(matrix, bit_vectors, row_size, col_size, row, col):
    
    row_bit_vector = bit_vectors[0] 

    if (1 << row) & row_bit_vector != 0:
        return

    bit_vectors[0] = bit_vectors[0] | (1 << row)
    
    for i in range(col_size):
        if matrix[row][i] == 0:
            zero_out_col(matrix, bit_vectors, row_size, col_size, row, i)

        matrix[row][i] = 0


def zero_out_col(matrix, bit_vectors, row_size,  col_size, row, col):

    col_bit_vector = bit_vectors[1]

    if (1 << col) & col_bit_vector != 0:
        return
 
    bit_vectors[1] = bit_vectors[1] | 1 << col

    for i in range(row_size):
        if matrix[i][col] == 0:
            zero_out_row(matrix, bit_vectors, row_size, col_size, i, col)

        matrix[i][col] = 0 
 

# -----------------------------------------------------------------------------------------------------

# This method reads the matrix from the console
# We exclude it from the overal complexity of the solution
def read_matrix(matrix, rows, columns):
   
    for i in range(rows):
        column_string = input().split(' ') 
        column = map(int, column_string)
        matrix.append(column)
        if len(column) != columns:
            raise Exception("The column size is less than what is required")

    return matrix


# I basically fucked up. Apparently the recursion implementation in CPython is quite naive and unless you are sure that your recursion depth is not going to exceed the imposed limit, you should not implement a recursive solution, but rather, you should focus on an iterative one

def performance_test():

    rows = 1000
    cols = 800
    int_upper_bound = 100

    shape = (rows, cols)

    matrix = np.random.randint(int_upper_bound, size=shape)
    matrix1 = matrix[:][:]

    start = time()
    zero_matrix(matrix, rows, cols) 
    end = time() 
    
    my_solution = end - start
    print("Elapsed time: {0}".format(my_solution / 1000))

    start = time()
    solution(matrix1, rows, cols) 
    end = time()
    
    solution_runtime = end / start
    print("Elapsed time: {0}".format(solution_runtime / 1000))



def solution(matrix, row, col):

    def clearRow(matrix, col_size, row):
        for c in range(col_size):
            matrix[row][c] = 0 
    

    def clearCol(matrix, row_size, col):
        for r in range(row_size):
            matrix[r][col] = 0
 
    rowHasZeros = False
    colHasZeros = False
    
    for i in range(row):
        if matrix[i][0] == 0:
            colHasZeros = True

    for i in range(col):
        if matrix[0][i] == 0:
            rowHasZeros = True 

    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j]:
                matrix[0][j] = 0
                matrix[i][0] = 0


    for i in range(row):
        if matrix[i][0] == 0:
            clearRow(matrix, col, i) 

    for i in range(col):
        if matrix[0][i] == 0:
            clearCol(matrix, row, i) 

    if rowHasZeros:
        for i in range(col):
            matrix[0][i] = 0

    if colHasZeros:
        for i in range(row):
            matrix[i][0] = 0


if __name__ == '__main__':
    
    arguments = sys.argv[1:]
    
    performance_test()

    #matrix = []
    #m = int(arguments[0])
    #n = int(arguments[1])
    
    #read_matrix(matrix, m, n)

    #zero_matrix(matrix, m, n)

    #for r in matrix:
    #    print(r)
