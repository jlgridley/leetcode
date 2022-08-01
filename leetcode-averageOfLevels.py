from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        averages = []
        q = deque()
        q.append((root, 0))
        total = 0
        numNodes = 0
        currLevel = 0
        while q:
            curr, level = q.popleft()
            if currLevel != level:
                averages.append(total/float(numNodes))
                currLevel = level
                numNodes = 1
                total = curr.val
            else:
                total += curr.val
                numNodes += 1
            if curr.left:
                q.append((curr.left, currLevel+1))
            if curr.right:
                q.append((curr.right, currLevel+1))
        averages.append(total/float(numNodes))
        return averages


sol = Solution()

twenty = TreeNode(20, TreeNode(15), TreeNode(7))
root = TreeNode(3, TreeNode(9), twenty)

print(sol.averageOfLevels(root))
