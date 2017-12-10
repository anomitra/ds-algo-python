
def return_if_empty(func):
    def check_none(root, *args, **kwargs):
        if root is None:
            return
        func(root)
    return check_none