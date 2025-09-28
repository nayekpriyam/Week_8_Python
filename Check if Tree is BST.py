def isBST(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.data < high):
        return False
    return isBST(root.left, low, root.data) and isBST(root.right, root.data, high)
