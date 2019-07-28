https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513

## Graph search 

- 0(N), no go back to the same node twice

## Tree search
#### Breadth-First Search [(BFS)](https://github.com/YIZHE12/DataScienceMakeEasy/blob/master/data_structures/binary_tree.ipynb) 
- level first -> visit all nodes in the same level first before visiting the child nodes

Preorder -> root first, then left, then right

Inorder ->  left, root in the middle, then right

Postorder -> left, right, root at the end

#### Depth-First Search (DFS) 
- if a node has a child, visit the child node first

#### Binary search tree (BST)
- a tree structure is pre-sorted so that left node < right node, children < parents

<img src = images/BST.png height = 200>

search, insert, delete - O(logN) for balanced BST, for unbalanced BST, it is O(N)
