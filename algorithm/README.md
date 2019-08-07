# Algorithm 

Resource: 

Programming practice: https://practice.geeksforgeeks.org/; Hacker earth; Hacker rank; Leetcode

MIT open course: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/

https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513

Book: http://home.ustc.edu.cn/~huang83/ds/Data%20Structures%20and%20Algorithms%20Using%20Python.pdf

http://web.karabuk.edu.tr/hakankutucu/CME222/MIT[1].Press.Introduction.to.Algorithms.2nd.Edition.eBook-TLFeBOOK.pdf

### Divide and Conquer

### Randomized Algorithm

### Greedy Algorithm: 
A loose definition Tim Roughgarden: from iteratively make "my opic" decision - decision that seems to be good at the time, and hope everyting workds out at the end. A more formal definition: A greedy algorithm is an algorithmic paradigm that follows the problem solving heuristic of making the locally optimal choice at each stage[1] with the intent of finding a global optimum. 

Many greeydy algorithm is actually not correct!

Exp: [Dijkstra's shortest path algorithm](https://www.youtube.com/watch?v=_lHSawdgXpI) It is not correct if the edge is negative. O(E + VlogV)
``` 
 1  function Dijkstra(Graph, source):
 2
 3      create vertex set Q
 4
 5      for each vertex v in Graph:             
 6          dist[v] ← INFINITY                  
 7          prev[v] ← UNDEFINED                 
 8          add v to Q                      
10      dist[source] ← 0                        
11      
12      while Q is not empty:
13          u ← vertex in Q with min dist[u]    
14                                              
15          remove u from Q 
16          
17          for each neighbor v of u:           // only v that are still in Q
18              alt ← dist[u] + length(u, v)
19              if alt < dist[v]:               
20                  dist[v] ← alt 
21                  prev[v] ← u 
22
23      return dist[], prev[]
```
If we are only interested in a shortest path between vertices source and target, we can terminate the search after line 15 if u = target. Now we can read the shortest path from source to target by reverse iteration:

    1  S ← empty sequence
    2  u ← target
    3  if prev[u] is defined or u = source:          // Do something only if the vertex is reachable
    4      while u is defined:                       // Construct the shortest path with a stack S
    5          insert u at the beginning of S        // Push the vertex onto the stack
    6          u ← prev[u]                           // Traverse from target to source

### Dynamic programming




## Tree search
#### Breadth-First Search [(BFS)](https://github.com/YIZHE12/DataScienceMakeEasy/blob/master/data_structures/binary_tree.ipynb) 
- level first -> visit all nodes in the same level first before visiting the child nodes

Preorder -> root first, then left, then right

Inorder ->  left, root in the middle, then right

Postorder -> left, right, root at the end

#### Depth-First Search (DFS) 
- if a node has a child, visit the child node first

#### Binary search tree [(BST)](https://github.com/YIZHE12/DataScienceMakeEasy/blob/master/data_structures/Binary_search_tree.ipynb)
- a tree structure is pre-sorted so that left node < right node, children < parents

<img src = images/BST.png height = 200>

search, insert, delete - O(logN) for balanced BST, for unbalanced BST, it is O(N)

## Graph search 

- 0(N), no go back to the same node twice
- Also has [DFS and BST](https://github.com/YIZHE12/DataScienceMakeEasy/blob/master/data_structures/Graph_dfs_bfs.ipynb)

### Shortest path problem:
1. Unweighted graph

It is just a DFS or BST problem until you find the node you are looking for.

2. Weighted graph

One famous algorithm is called Dijkstra's Algorithm:
First we give all node a distance property, the distance of the starting node is 0, while the rest is infinity. A common implementation of the algorithm is to used the min priority queue to get the minimum value. We start from the starting node, and update the distance property of the node that it connected, which equal to the weight of the edge. Then pick the node with the smallest number in the distance queue. It is O(|V|^2). If the priority queue was implemented efficiently, the runtime is O(|E|+|V|log(|V|)).

### Knapsack problem:

You have a bag to pack with weight limit. You want to pack as many items as possible. How to choose the item?

1. Brute force: O(2^n) - think about each item as either 0 or 1. 0 means packing, 1 means no.
This is an exponential time, we would prefer a polynomial time algorithm, such as O(n^2) or linear time, such as O(3n).

### Traveling salesman problem

It is an NP hard problem.




