class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()

            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))

            if not node.left and not node.right:
                res.append(path)

        return res
