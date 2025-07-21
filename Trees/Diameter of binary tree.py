# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    maxi = [0]

    def dfs(node):
        if not node:
            return 0
        lh = 1 + dfs(node.left)
        rh = 1 + dfs(node.right)
        maxi[0] = max(maxi[0], lh + rh - 2)
        return max(lh, rh)
    dfs(root)
    return maxi[0]

if __name__ == '__main__':
    root = TreeNode(1)
    two = TreeNode(2)
    root.left = two
    three = TreeNode(3)
    root.right = TreeNode(3)
    two.left = TreeNode(4)
    two.right = TreeNode(5)
    res = diameterOfBinaryTree(None, root)  # Output: 3

    print(f"Diameter of Binary Tree: {res}")
