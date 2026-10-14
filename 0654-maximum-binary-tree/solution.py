# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        def build(num): # num is an array 
            if not num:
                return None
            root = TreeNode(max(num))
            idx = num.index(root.val)
            root.left = build(num[:idx])
            root.right = build(num[idx + 1:])
            return root
        return build(nums)


