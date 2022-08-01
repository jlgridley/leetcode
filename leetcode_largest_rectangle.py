#!/usr/bin/env python3

def maximal_first(matrix):
    # DP
    # create grid M of the same size as the n x m original matrix
    # go through grid and retain max size from:
    #   each square in the new matrix is: List[tuple, tuple, set of tuples]
    #   each tuple is the coordinate of the opposite corner of a complete rectangle
    #   for square (i, j), check the adjacent right and lower squares
    #   the first tuple is (i, x) in the right square
    #   the second tuple is (y, j) in the bottom square's set
    #   the set of tuples for (i, j) should be:
    #       intersection of the sets from the right and lower squares
    #       (i, j)
    """
    0 0 1
    1 1 1 0
    1 1 1 1
    1 1 1 1
    0 1 1

    Complexity: O((nm)^2)?
    """

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    biggest = 0
    rows = len(matrix)
    cols = len(matrix[0])
    M = [[[None, None, set()] for i in range(cols)] for j in range(rows)]
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            print("(" + str(i) + ", " + str(j) + "):")
            if matrix[i][j] == "1":
                M[i][j][2].add((i, j))
                if i + 1 < rows and matrix[i+1][j] == "1": # check neighbor below
                    M[i][j][0] = M[i+1][j][0]
                    M[i][j][2].add(M[i+1][j][0])
                    M[i][j][2].add((i+1, j))
                    curr_col = M[i+1][j][0][0] - i + 1
                    if biggest < curr_col:
                        biggest = curr_col
                else:
                    M[i][j][0] = (i, j)
                    if biggest < 1:
                        biggest = 1
                if j + 1 < cols and matrix[i][j+1] == "1": # check neighbor to left
                    M[i][j][1] = M[i][j+1][1]
                    M[i][j][2].add(M[i][j+1][1])
                    M[i][j][2].add((i, j+1))
                    curr_row = M[i][j+1][1][1] - j + 1
                    if biggest < curr_row:
                        biggest = curr_row
                else:
                    M[i][j][1] = (i, j)
                    if biggest < 1:
                        biggest = 1
                if j + 1 < cols and i + 1 < rows:
                    print("intersection:", M[i+1][j][2].intersection(M[i][j+1][2]))
                    M[i][j][2] = M[i][j][2].union(M[i+1][j][2].intersection(M[i][j+1][2]))
                    for corner_row, corner_col in M[i][j][2]:
                        height = corner_row - i + 1
                        length = corner_col - j + 1
                        area = height * length
                        if area > biggest:
                            biggest = area
            print(M[i][j], "\n")
    return biggest

def maximal_take2(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    biggest = 0
    rows = len(matrix)
    cols = len(matrix[0])
    M = [[[None, None, set()] for i in range(cols)] for j in range(rows)]
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            print("(" + str(i) + ", " + str(j) + "):")
            if matrix[i][j] == "1":
                M[i][j][2].add((i, j))
                if i + 1 < rows and matrix[i+1][j] == "1":
                    M[i][j][0] = M[i+1][j][0]
                    M[i][j][2].add(M[i+1][j][0])
                    M[i][j][2].add((i+1, j))
                    curr_col = M[i+1][j][0][0] - i + 1
                    if biggest < curr_col:
                        biggest = curr_col
                else:
                    M[i][j][0] = (i, j)
                    if biggest < 1:
                        biggest = 1
                if j + 1 < cols and matrix[i][j+1] == "1":
                    M[i][j][1] = M[i][j+1][1]
                    curr_row = M[i][j+1][1][1] - j + 1
                    M[i][j][2].add(M[i][j+1][1])
                    M[i][j][2].add((i, j+1))
                    if biggest < curr_row:
                        biggest = curr_row
                else:
                    M[i][j][1] = (i, j)
                    if biggest < 1:
                        biggest = 1
                if j + 1 < cols and i + 1 < rows:
                    print("intersection:", M[i+1][j][2].intersection(M[i][j+1][2]))
                    M[i][j][2] = M[i][j][2].union(M[i+1][j][2].intersection(M[i][j+1][2]))
                    for corner_row, corner_col in M[i][j][2]:
                        height = corner_row - i + 1
                        length = corner_col - j + 1
                        area = height * length
                        if area > biggest:
                            biggest = area
            print(M[i][j], "\n")
    return biggest

"""
Brute force solution:

Check every single possible rectangle to see if it's filled with 1s
(nm)^2 (choose every possibility of two opposite corners) * (nm) (check if every square within the rectangle is a 1)

obviously this is duplicating a lot of work. how not to duplicate?
slice out 0s with BFS leaving only the 1s?
have a hashtable saying if two corners are already filled with 1s
go column by column? skip over the pairs when a 0 is encountered
get intervals, then overlapping intervals
keep a max of the longest interval in every row
keep track of the depth of each still overlapping interval

list = []
for each row:
    start = -1
    max = 0
    for each square i in the row:
        if i == 1 and start == -1:
            start = i
        if i == 0 and start != -1:
            start = -1
            add (start, i-1) to the list
            max = largest of i-1-start+1 and max
    if start != -1:
        add (start, i-1) to the list
        max = largest of i-1-start+1 and max
    

"""

def maximal_take2(matrix):
    pass

input = [ \
  ["1","0","1","0","0"],\
  ["1","0","1","1","1"],\
  ["1","1","1","1","1"],\
  ["1","0","0","1","0"]\
]
input =[\
    ["0","1","1","0","1"],\
    ["1","1","0","1","0"],\
    ["0","1","1","1","0"],\
    ["1","1","1","1","0"],\
    ["1","1","1","1","1"],\
    ["0","0","0","0","0"]]
print(maximal(input))
