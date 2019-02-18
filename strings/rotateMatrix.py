import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def problem():
    """
    Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 
    """

# According to my calculations, in order to perform the rotation in place, we need to do a specific cell value rotation
# If we want to move a single pixel, we would have to move all the corresponding pixels untill we find the one that goes to the current rotated pixel's place
# We need to do some sort of up-right-down-left motion
# This function works in O(r * c) where r are the rows and c are the columns
# In reality it is faster by a factor of 16
def rotateMatrix(matrix, rows, columns):
    """
    This function rotates an image/matrix by 90 degrees clockwise
    
    Solution Steps:
    Step 1: Go through half the diagonal (bottom left to upper right)
    Step 2: Rotate four cells on each iteration 
    """    
    offset = 0
    for row_bottom_offset in range(rows - 1, rows // 2, -1):
       
        col_left_offset = 1 
        for row in range(row_bottom_offset, offset, -1):
            
           current = matrix[row][offset]
           matrix[row][offset] = matrix[row_bottom_offset][-offset - col_left_offset] 
           matrix[row_bottom_offset][-offset - col_left_offset] = matrix[rows - row - 1][-offset - 1]
           matrix[rows - row - 1][-offset - 1] = matrix[rows - row_bottom_offset - 1][offset + col_left_offset - 1]
           matrix[rows - row_bottom_offset - 1 ][offset + col_left_offset - 1] = current

           col_left_offset += 1

        offset += 1

def rotateImage(image):
    
    image_matrix = mpimg.imread(image) 
    image_matrix_copy = image_matrix.copy()
    image_matrix_copy = image_matrix_copy[0:300, 0:300, :1].reshape(300, 300)
    rotateMatrix(image_matrix_copy, image_matrix.shape[0], image_matrix.shape[1] - 32)
    plt.imshow(image_matrix_copy, cmap='gray')
    plt.show()

if __name__ == '__main__':

    args = sys.argv[1:]
    
    if len(args) >= 3:
        rotateImage(args[2])        
        exit()
    
    #matrix = [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3 ,4 ,5 ,6 ,7 ,8], [1, 2, 3 ,4 ,5 ,6 ,7 ,8], [1, 2, 3 ,4 ,5 ,6 ,7 ,8], [1, 2, 3 ,4 ,5 ,6 ,7 , 8], [1, 2, 3 ,4 ,5 ,6 ,7 , 8], [1, 2, 3 ,4 ,5 ,6 ,7 , 8], [1, 2, 3 ,4 ,5 ,6 ,7 ,8]] 

    shape = (int(args[0]), int(args[1]))
    matrix = np.random.randint(255, size=shape)
    #shape = (8, 8)
    #for r in matrix:
    #    print(r)

    #print("\n")
    rotateMatrix(matrix, shape[0], shape[1]) 
    #for r in matrix:
    #    print(r)
