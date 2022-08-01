from collections import deque

class Solution:

    def get_index(self, square_num, n):
        row = n - ((square_num-1) // n + 1)
        col = (square_num - 1) % n
        if n % 2 == 0:
            if row % 2 == 0:
                col = n - col - 1
        elif row % 2 == 1:
            col = n - col - 1
        return row, col

    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        """
        Create a function that converts square numbers to indices
        Do BFS starting from board[n-1][0]
        A square shares edges with six edges ahead
        If one of them is a snake or ladder, the square shares an edge with the square that the snake or ladder goes to
        A square with a snake or ladder is not a node
        """
        n = len(board)
        last_row, last_col = self.get_index(n*n, n)
        if board[last_row][last_col] != -1 and board[last_row][last_col] != n*n:
            return -1
        queue = deque()
        first = 1
        first_row, first_col = self.get_index(first, n)
        if board[first_row][first_col] != -1:
            first = board[first_row][first_col]
        queue.appendleft((first, -1))  # square number, parent level
        levels = [-1 for i in range(n*n)]
        while queue:
            # print(queue)
            curr, parent = queue.pop()
            levels[curr-1] = parent + 1
            if curr >= n*n:
                break
            for i in range(curr+1, curr+7):
                if i < n*n + 1:
                    new_row, new_col = self.get_index(i, n)
                    destination = board[new_row][new_col]
                    if destination != -1:
                        if levels[destination-1] == -1:
                            queue.appendleft((destination, parent + 1))
                    elif levels[i-1] == -1:
                        queue.appendleft((i, parent + 1))

        return levels[-1]
