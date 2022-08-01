#!/usr/bin/env python3

"""
Brute-force solution:

O(n^3): for each element, check the difference between it and every other element and check for any numbers with the same diff
        then use the sum from 1 to n-2 thing
        Adding the differences of an already discovered sequence using every other element?
        Keep track of already-seen diffs and the elements involved in them


Sort and use indices? No: the size of the element doesn't really matter; it's the difference

Graph? Directed?
n^2 to build the graph
hashmap of the weights of the edges from each node?
Adding the differences of an already discovered sequence using every other element?
Keep track of already-seen diffs and the elements involved in them
processing it is still n^3 in the worst case

dynamic programming:



"""

"""
First problem description:

Input: array of signed integers

An "arithmetic sequence" is a sequence of at least 3 numbers such that the difference between any two consecutive numbers is the same.

Arithmetic sequence:
2 4 6 8

Not an arithmetic sequence:
1 5 6 -2

How many arithmetic sequences among consecutive elements are in the array?

Input: [10, 2, 4, 6, 36]
Output: 1

Input: [1, 4, 7, 8, 16, 24]
Output: 2

Input: [2, 4, 6, 8]
Output: 3
(the arithmetic sequences are 2, 4, 6; 4, 6, 8; and 2, 4, 6, 8)

____________________________
Second problem description:

What if it need not be immediately consecutive?

e.g.
Input: [1, 3, 4, -2, 10, 7]
Output: 1 (from 1 4 7) (but not 4 7 10)

"""

def numSlices(A):
    """
    advance end of window until the difference between elements changes
        keep pointers on the start and end of the window (initialized to the same element)
        while end < len(A) - 1:
            initialize the first difference in the current window (end + 1 - end) and advance end to end + 1
            keep incrementing end every time the same difference is found again
            once a different difference (or the end of the array) is found:
                if end - start + 1 > 3:
                    sum from 1 to n - 2 (where n = end - start + 1)
                place start on end
    for each largest window of length n > 2:
        window of size 3: n - 2
        window of size 4: n - 3
        .
        .
        .
        window of size n: n - (n - 1) = 1

    linear time
    """
    if len(A) < 3:
        return 0
    start = 0
    end = 0
    slices = 0
    while end < len(A) - 2:
        diff = A[end + 1] - A[end]
        end += 1
        while end < len(A) - 1:
            new_diff = A[end + 1] - A[end]
            if new_diff == diff:
                end += 1
            else:
                break
        window_size = end - start + 1
        if window_size > 2:
            slices += ((window_size - 2) * (window_size - 1)) // 2
        start = end
    return slices
"""
    0123456
    1135
     s e
"""

A = [1, 2, 3, 4]
print(numSlices(A))
