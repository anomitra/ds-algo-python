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

def top_view(root):
    queue = Queue()
    queue.put((root,0))
    hd_covered = []
    while queue.qsize():
        current_node, hd = queue.get()
        if hd not in hd_covered:
            hd_covered.append(hd)
            print(current_node.value)
        if current_node.left:
            queue.put((current_node.left, hd-1))
        if current_node.right:
            queue.put((current_node.right, hd+1))

def bottom_view(root):
    queue = Queue()
    queue.put((root,0))
    bottom_nodes = {}
    while queue.qsize():
        current_node, hd = queue.get()
        bottom_nodes[hd] = current_node.value
        if current_node.left:
            queue.put((current_node.left, hd-1))
        if current_node.right:
            queue.put((current_node.right, hd+1))
    print(bottom_nodes)


def right_view(root, level):
    global max_level
    if root is None:
        return
    if level > max_level:
        print(root.value)
        max_level = level
    if root.right:
        right_view(root.right, level+1)
    if root.left:
        right_view(root.left, level+1)

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
top_view(tree)
bottom_view(tree)
max_level = 0
right_view(tree, 1)
