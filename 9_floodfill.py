# an image is represented by a m x n integer grid, image
# image[i][j] represents a pixel value for the image
# given three ints sr,sc,color perform a flood fill starting from image[sr][sc]

# flood fill is considered the starting pixel plus any pizels connected 4-directionally, also with the same color plus any pixels 4-directionally to those pixels

# return the modifies image

# image = [[],[],[]...]
from turtle import color


imageex = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
    ]
outputex = [
    [2,2,2],
    [2,2,0],
    [2,0,1]
    ]

def flood_fill(image, sr, sc, color):
    # edge case: the starting pixel is already the color of new color, do nothing
    if image[sr][sc] == color:
        return image
    
    def helper(image, sr, sc, color, new_color):
        # base case: image[sr][sc] is out of bounds THEN is it's not equal to color
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
            return
        # gets past here, we're in bounds
        elif image[sr][sc] != color:
            return
        # recursive case: change the color of the pixel then call this function on left, right, up, down pixels
        else:
            image[sr][sc] = new_color
            helper(image, sr+1, sc, color, new_color)
            helper(image, sr-1, sc, color, new_color)
            helper(image, sr, sc+1, color, new_color)
            helper(image, sr, sc-1, color, new_color)

    # call helper on the starting pixel
    helper(image, sr, sc, image[sr][sc], color)
    return image

