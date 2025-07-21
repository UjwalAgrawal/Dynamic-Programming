# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    res = [root.val]

    def helper(node):
        if not node:
            return 0

        left_max = max(helper(node.left), 0)
        right_max = max(helper(node.right), 0)
        res[0] = max(res[0], node.val + left_max + right_max)
        return node.val + max(left_max, right_max)

    helper(root)
    return res[0]
