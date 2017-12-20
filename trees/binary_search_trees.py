from traversals import print_inorder
from tree import Node


def bst_insert(root, value):
    if root is None:
        root = Node(value)
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            bst_insert(root.left, value)
    if value >= root.value:
        if root.right is None:
            root.right = Node(value)
        else:
            bst_insert(root.right, value)


def bst_search(root, key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return bst_search(root.right, key)
    bst_search(root.left, key)


def _leftmost(root):
    while root.left is not None:
        root = root.left
    return root


def bst_delete(root, key):
    if root is None:
        return root
    if root.value < key:
        root.right = bst_delete(root.right, key)
    if root.value > key:
        root.left = bst_delete(root.left, key)
    elif root.value == key:
        if root.left is None:
            tmp = root.right
            root = None
            return tmp
        if root.right is None:
            tmp = root.left
            root = None
            return tmp
        # If both child present, replace by inorder successor (or leftmost node)
        leftmost = _leftmost(root.right)
        root.key = leftmost.key
        root.right = bst_delete(root.right, leftmost.key)
    return root


def order_statistics_bst(root, k):
    global order
    if root is None:
        return
    if root.left:
        order_statistics_bst(root.left, k)
    order += 1
    if order == k:
        print(root.value)
    if root.right:
        order_statistics_bst(root.right, k)


curr_tree = Node(3)
bst_insert(curr_tree, 2)
bst_insert(curr_tree, 1)
bst_insert(curr_tree, 7)
bst_insert(curr_tree, 6)
print_inorder(curr_tree)
bst_delete(curr_tree, 6)
print_inorder(curr_tree)
order = 0
order_statistics_bst(curr_tree, 2)
