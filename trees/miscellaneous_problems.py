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
