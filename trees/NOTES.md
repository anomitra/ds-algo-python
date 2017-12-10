# Miscellaneous Notes on Trees

#### Delete a Tree

Traverse the tree in postorder, and delete the node instead of printing it.

#### Iterative Postorder Traversal

Do a normal iterative traversal, and maintain a dictionary of visited nodes.
If a node is not visited, add it's left and right nodes to the stack. If a node is visited,
pop it from the stack and print it's content.

