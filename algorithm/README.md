# Algorithm 

Resource: 

Programming practice: https://practice.geeksforgeeks.org/; Hacker earth; Hacker rank; Leetcode

MIT open course: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/

https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513

Book: http://home.ustc.edu.cn/~huang83/ds/Data%20Structures%20and%20Algorithms%20Using%20Python.pdf

http://web.karabuk.edu.tr/hakankutucu/CME222/MIT[1].Press.Introduction.to.Algorithms.2nd.Edition.eBook-TLFeBOOK.pdf

https://runestone.academy/runestone/books/published/pythonds/index.html

### Recursion

A recursive algorithm must have a base case.

A recursive algorithm must change its state and move toward the base case.

A recursive algorithm must call itself, recursively.

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

A divide-and-conquer algorithm does more work thannecessary, repeaedly sovlving the common subsubproblem. A dynamic-programming algorithm, on contrast, only solve the subsubproblems just once and then saves its answer in a table, thereby avoiding the same problem. Typically, it is used in optimization problems, where there are many possible solutions.

The four steps of dynamic programming:

1. Characterize the structure of an optimal solution.

2. Recursively define the value of an optimal solution.

3. Compute the value of an optimal solution, typically in a bottom-up fashion.

4. Construct an optimal solution from computed information. (This can be omitted if we don't need to solution itself, but only the optimal value.)


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

One famous algorithm is called [Dijkstra's Algorithm](https://www.youtube.com/watch?v=zXfDYaahsNA):

First we give all node a distance property, the distance of the starting node is 0, while the rest is infinity. A common implementation of the algorithm is to used the min priority queue to get the minimum value. We start from the starting node, and update the distance property of the node that it connected, which equal to the weight of the edge. Then pick the node with the smallest number in the distance queue. 

A naive implementation of this algorithm will result in O(VE), as we search each Vertice, and for each vertice, we search each edge.

If the priority queue was implemented efficiently, the runtime is O((|E|+|V|)log(|V|)).

We can also use heap instead of priority queue.

### Knapsack problem:

You have a bag to pack with weight limit. You want to pack as many items as possible. How to choose the item?

1. Brute force: O(2^n) - think about each item as either 0 or 1. 0 means packing, 1 means no.
This is an exponential time, we would prefer a polynomial time algorithm, such as O(n^2) or linear time, such as O(3n).

### Traveling salesman problem

It is an NP hard problem.

### Memoization
Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. (Source: wikipedia)

In python, it can be simpliy done by using lru_cache on top your orignal recursive function. See my [example:](https://github.com/YIZHE12/DataScienceMakeEasy/blob/master/algorithm/recursive/Fibonacci.ipynb)

```
from functools import lru_cache

@lru_cache(maxsize = 1000)
def get_fib(position):
    if position == 0:
        return(0)
    if position == 1:
        return(1)
    else:
        output = get_fib(position-1)+get_fib(position-2)
        return(output)
    return -1
```

### Tail recursion
Tail recursion is a recursion where the recursive call is the final instruction in the recursion function. And there should be only one recursive call in the function.

The benefit of having tail recursion is that it could avoid the accumulation of stack overheads during the recursive calls, since the system could reuse a fixed amount space in the stack for each recursive call. 

A tail recursion function can be executed as non-tail-recursion functions, i.e. with piles of call stacks, without impact on the result. Often, the compiler recognizes tail recursion pattern, and optimizes its execution. However, not all programming languages support this optimization. For instance, C, C++ support the optimization of tail recursion functions. On the other hand, Java and Python do not support tail recursion optimization.

