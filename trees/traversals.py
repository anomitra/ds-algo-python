from queue import Queue

from decorators import return_if_empty
from tree import Node


def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print(root.value, end=' ')
    print_inorder(root.right)


def print_preorder(root):
    if root is None:
        return
    print(root.value, end=' ')
    print_preorder(root.left)
    print_preorder(root.right)


@return_if_empty
def print_postorder(root):
    if root is None:
        return
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.value, end=' ')


def iterative_preorder(root):
    # Preorder is root, left and then right.
    if root is None:
        return

    stack = list()
    stack.append(root)

    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node.value, end=' ')
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)


@return_if_empty
def iterative_postorder(root):
    # Postorder is left, right and then root.

    if root is None:
        return

    stack = list()
    stack.append(root)
    visited = {}
    while len(stack) > 0:
        current_node = stack[-1]
        if not visited.get(current_node):
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            visited[current_node] = True
        else:
            print(current_node.value, end=' ')
            stack.pop()


def _height(root):
    if root is None:
        return 0
    r_height = _height(root.right) + 1
    l_height = _height(root.left) + 1
    return max(r_height, l_height)


def level_order_traversal(root):
    if root is None:
        return

    queue = Queue()
    queue.put(root)

    while True:

        if queue.qsize() == 0:
            break

        while queue.qsize() != 0:
            current = queue.get()
            print(current.value, end=' ')
            if current.left:
                queue.put(current.left)
            if current.right:
                queue.put(current.right)


def _sum_each_diagonal(root, vertical_distance, store):
    if root is None:
        return store
    try:
        store[vertical_distance] += root.value
    except KeyError:
        store[vertical_distance] = root.value
    _sum_each_diagonal(root.left, vertical_distance + 1, store)
    _sum_each_diagonal(root.right, vertical_distance, store)


def diagonal_sum(root):
    diagonals = {}
    _sum_each_diagonal(root, vertical_distance=0, store=diagonals)
    print(diagonals)


def leaf_traversal(root, leaves):
    if root is None:
        return

    leaf_traversal(root.left, leaves)
    if root.left is None and root.right is None:
        leaves.append(root.value)
    leaf_traversal(root.right, leaves)


def check_leaf_traversal_same(tree1, tree2):
    leaves1 = []
    leaf_traversal(tree1, leaves1)
    leaves2 = []
    leaf_traversal(tree2, leaves2)
    if leaves1 == leaves2:
        print('Leaves are same')
    else:
        print('Leaves are not same')


def vertical_traversal(root, level, store={}):
    if root is None:
        return
    vertical_traversal(root.left, level - 1, store)
    try:
        store[level].append(root.value)
    except KeyError:
        store[level] = [root.value]
    vertical_traversal(root.right, level + 1, store)


def make_tree():
    root = Node(1)
    root.left = Node(2, left=Node(4), right=Node(5))
    root.right = Node(3, left=Node(6), right=Node(7))
    return root


tree = make_tree()
print_inorder(tree)
print()
print_preorder(tree)
print()
print_postorder(tree)
print()
iterative_preorder(tree)
print()
iterative_postorder(tree)
print()
level_order_traversal(tree)
print()
diagonal_sum(tree)
print()
leaves = []
leaf_traversal(tree, leaves)
print(leaves)
check_leaf_traversal_same(tree, tree)
vertical = {}
vertical_traversal(tree, 0, vertical)
print(vertical)
