from collections import deque

def levelOrder(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        node = q.popleft()
        result.append(node.data)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return result
