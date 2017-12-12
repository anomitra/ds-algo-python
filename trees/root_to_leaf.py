from tree import Node


def _is_leaf(node):
    if not node.left and not node.right:
        return True
    return False


def root_to_leaf(root, sum):
    if root is None:
        return
    if _is_leaf(root) and sum == root.value:
        print('A path is found')
        return

    if root.left:
        root_to_leaf(root.left, sum - root.value)
    if root.right:
        root_to_leaf(root.right, sum - root.value)


def root_to_leaf_with_path(root, sum, stack):
    if _is_leaf(root):
        if sum == root.value:
            stack.append(root.value)
            print('A path has been found')
            print(stack)
        return

    if root.left:
        stack.append(root.value)
        root_to_leaf_with_path(root.left, sum - root.value, stack)
        stack.pop()
    if root.right:
        stack.append(root.value)
        root_to_leaf_with_path(root.right, sum - root.value, stack)
        stack.pop()


def print_ancestors(root, target, path):
    if root.value == target:
        path.append(target)
        print('Found the target -> ', target)
        print('The path is ', path)
        return
    if root.left:
        path.append(root.value)
        print_ancestors(root.left, target, path)
        path.pop()
    if root.right:
        path.append(root.value)
        print_ancestors(root.right, target, path)
        path.pop()


def make_tree():
    return Node(
        10,
        left=Node(
            8,
            left=Node(3),
            right=Node(5),
        ),
        right=Node(
            2,
            left=Node(2),
        )
    )


tree = make_tree()
root_to_leaf(tree, 14)
stack = []
root_to_leaf_with_path(tree, 23, stack)
path = []
print_ancestors(tree, 5, path)
