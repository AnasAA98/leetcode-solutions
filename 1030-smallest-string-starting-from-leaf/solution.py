# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        def dfs(node, path,res):
            if not node:
                return res
            if not node.left and not node.right:
                path.append(chr(ord('a') + node.val))
                word = "" .join(path[::-1])
                path.pop()
                res = min(res, word)
                return res
            path.append(chr(ord('a') + node.val))
            left = dfs(node.left,path,res)
            right = dfs(node.right, path,res)
            path.pop()
            return min(left,right)
        return dfs(root,[],"}")
        

