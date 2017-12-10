# Miscellaneous Notes on Trees

### Delete a Tree

Traverse the tree in postorder, and delete the node instead of printing it.

### Iterative Postorder Traversal

Do a normal iterative traversal, and maintain a dictionary of visited nodes.
If a node is not visited, add it's left and right nodes to the stack. If a node is visited,
pop it from the stack and print it's content.

### Diameter of a Tree

> The diameter or width of a tree is the number of nodes on the longest path between two leaves in
 the tree.

At any given node, the diameter of the subtree rooted in that particular node is equal to the maximum of

 - the diameter of it's left subtree
 - the diameter of it's right subtree
 - the longest path between leaves which passes through it

To find the third, we find the height of it's left and right subtrees. Then we recursively compare it to the first two.

```python
l_height = height(root.left)
r_height = height(root.right)

left_diameter = diameter(root.left)
right_diameter = diameter(root.right)

return max(left_diameter, right_diameter, l_height + r_height + 1)
```

### Check if a binary tree is height-balanced

Check height difference between left subtree and right subtree is less than one, and recursively
check if it's left and right subtrees are height-balanced. If these conditions are met, then the tree
is height-balanced.
