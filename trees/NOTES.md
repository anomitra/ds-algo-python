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

### Populate inorder successor in `next` reference

> Question: Given a Binary Tree where each node has following structure, write a function to populate next pointer for all nodes. The next pointer for every node should be set to point to inorder successor.

**Solution:** Traverse the given tree in a reverse inorder traversal. Pass the previous node reference as a function argument, and set it in the current node.

```python

def populate_next_recursively(tree, next=None):
    populate_next_recursively(tree.right, next)
    tree.next = next
    next = tree
    populate_next_recursively(tree.left, next)

populate_next_recursively(root)
```

### Foldable binary trees

> Question: Given a binary tree, find out if the tree can be folded or not. A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other. An empty tree is considered as foldable.

**Solution:** Mirror the left subtree, and then compare if it is structurally similar to the right subtree. If that condition holds, then the tree is foldable.

### Remove paths where `sum >= k`

> Question: For a binary tree, a complete path is defined as a path from root to a leaf. The sum of all the nodes on that path is defined as it's sum. Given a number K, you have to remove (prune the tree) all nodes which don’t lie in any path with sum>=k.

**Solution:** Traverse the tree, and recursively keep calculating the sum of each path.
We use a function argument like `sum_till_now` to maintain the sum of the path, and use
different variables for the left and right subtree (so that we get sums of both
subtrees independently).

Then, when we reach a leaf, we check if either sum has reached `k` or not. If not, then we
delete the node and continue the traversal. In this manner, all nodes are deleted in a bottom up manner.