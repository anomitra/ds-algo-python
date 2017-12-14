from queue import Queue

from tree import Node


def left_view(root):
    queue = Queue()
    queue.put((root, 0))
    max_level = -1
    while queue.qsize():
        current_node, level = queue.get()
        if level > max_level:
            max_level += 1
            print(current_node.value, ' ')
        if current_node.left:
            queue.put((current_node.left, level + 1))
        if current_node.right:
            queue.put((current_node.right, level + 1))

def make_tree():
    return Node(
        18,
        left=Node(
            8,
        ),
        right=Node(
            2,
            left=Node(3),
            right=Node(5),
        )
    )


tree = make_tree()
left_view(tree)
