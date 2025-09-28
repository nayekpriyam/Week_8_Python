def diameter(root):
    diameter_val = [0]

    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter_val[0] = max(diameter_val[0], left + right + 1)
        return 1 + max(left, right)

    depth(root)
    return diameter_val[0]
