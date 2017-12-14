from queue import Queue

from tree import Node


def _get_sum_of_subtree(root):
    if root is None:
        return 0
    return _get_sum_of_subtree(root.left) + root.value + _get_sum_of_subtree(root.right)


def check_if_sumtree(root):
    if root is None or (root.left is None and root.right is None):
        return True
    left_sum = _get_sum_of_subtree(root.left)
    right_sum = _get_sum_of_subtree(root.right)
    if root.value == left_sum + right_sum and check_if_sumtree(root.left) and check_if_sumtree(
            root.right
    ):
        return True
    return False


def vertical_sum_by_levels(root, sums, index):
    if root is None:
        return
    try:
        sums[index] += root.value
    except KeyError:
        sums[index] = root.value
    if root.left:
        vertical_sum_by_levels(root.left, sums, index - 1)
    if root.right:
        vertical_sum_by_levels(root.right, sums, index + 1)


def find_next_right_node(root, value):
    level = 0
    queue = Queue()
    queue.put((root, level))
    get_next = False
    while queue.qsize():

        current_node, level = queue.get()
        if get_next:
            if node_level == level:
                print('Next right found as ', current_node.value)
            else:
                print('No next right node')
            get_next = False
        if current_node.left:
            queue.put((current_node.left, level + 1))
        if current_node.right:
            queue.put((current_node.right, level + 1))
        if current_node.value == value:
            get_next = True
            node_level = level

def make_tree():
    return Node(
        18,
        left=Node(
            8,
            left=Node(3),
            right=Node(5),
        ),
        right=Node(
            2,
        )
    )


tree = make_tree()
print(check_if_sumtree(tree))
map = dict()
vertical_sum_by_levels(tree, map, 0)
print(map)
find_next_right_node(tree, 8)
find_next_right_node(tree, 3)
find_next_right_node(tree, 18)
