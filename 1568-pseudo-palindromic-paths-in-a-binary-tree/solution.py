# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode | None) -> int:
        count = [0] * 10
        def dfs(root):
            if not root:
                return 0
            count[root.val] += 1
            if not root.left and not root.right:
                odd_count = 0
                for c in count:
                    odd_count += 1 if c % 2 != 0 else 0
                res = 1 if odd_count <= 1 else 0
            else:
                res = dfs(root.left) + dfs(root.right)
            count[root.val] += 1
            return res 
        return dfs(root)

