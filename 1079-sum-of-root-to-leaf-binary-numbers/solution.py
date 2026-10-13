# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        def dfs(root, path):
            if not root:
                return 0
            if not root.left and not root.right:
                path.append(str(root.val))
                temp = "".join(path)
                res = int(temp, 2)
                path.pop()
                return res
            path.append(str(root.val))
            left = dfs(root.left, path)
            right = dfs(root.right, path)
            path.pop()
            return left + right
        return dfs(root, [])


                

