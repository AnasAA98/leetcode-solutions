# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []
        def dfs(node, curr, path):
            if not node:
                return
            curr += node.val
            path.append(node.val)
            if not node.left and not node.right and curr == targetSum:
                res.append(path[:])
                path.pop()
                return
            dfs(node.left,curr, path)
            dfs(node.right,curr, path)
            path.pop()
            return
        dfs(root,0,[])
        return res
