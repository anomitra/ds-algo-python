class Node(object):

    def __init__(self, key, left=None, right=None):

        self.left = None
        self.right = None
        if left and isinstance(left, Node):
            self.left = left
        if right and isinstance(right, Node):
            self.right = right
        self.value = key
