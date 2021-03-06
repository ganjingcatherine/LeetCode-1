"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        
        leftMax = 0
        if root.left:
            leftMax = self.maxDepth(root.left)
            
        rightMax = 0
        if root.right:
            rightMax = self.maxDepth(root.right)
            
        return max(leftMax,rightMax)+1