# Data Structures
Resources:

https://www.coursera.org/learn/data-structures/home/welcome

https://leetcode.com/explore/

## List

A python list contains more storage space than is needed to store the items currently in the list. This extra space, the size of which can be up to twice the necessary capacity, allows for quick and easy expansion as new items are added to the list.

## Array

A one-dimensional array is composed of multiple sequential elements stored in contiguous bytes of memory and allows for random access to the individual elements. Compared to list, to use array, you have to know the size of the array beforehand, and cannot change it later.

## Map

Similar to python dictionary.

## Set

A set is a container that stores a collection of unique values over a given comparable domain in which the stored values have no particular ordering. The key of a map is a set as it is not allow to have repetitions.

## Link List
In python, every time when you insert an element to a list, new storage of the entire list will be created and the elemenets need to be shifted to move room. This means it is quite not efficient when the list is large. Therefore, in this situation, we used link list instead, which doesn't recreate the storage neither does it require shifting. However, it does eliminate the constant time direct element access available with the array and Python list. As its name implies, the link strucutre has to been accessed based on the 'link order'. The singly linked list is a linear structure in which traversals start at the front and progress, one element at a time, to the end. Other variations include the circularly linked, the doubly linked, and the circularly doubly linked lists.

```
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
def append(self, new_element):
    current = self.head
    if self.head:
        while current.next:
            current = current.next
        current.next = new_element
    else:
        self.head = new_element
```

## Stack

First in last out structure. Python already has an implementation of stack using list, you can use append and pop directly.

```
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]

```

or with a linked list, you can do 
```
def delete_first(self):
    deleted = self.head
    if self.head:
        self.head = self.head.next
        deleted.next = None
    return deleted
```

## Queue
A queue is the opposite as a stack, it is first in first out. It has a head and a detail. Adding an element from the top is called 'enqueue', removing an element from the bottom is called 'deque'. A dqueue is a double queue, which you can add and remove things from both ways. A priority queue is a queue where you added 'priority' into the element, the highest priority element will always get removed first, which is not following the first in first out rule. However, if there is a tie in priority, the oldest element will be removed first.

<img src = images/queue.png height = 200>

In python, there is a deque implementation:
```
from collections import deque
```

## Hash table
https://www.youtube.com/watch?v=KyUTuwz_b7Q

The index of the hash table is hidden in the content/value. In other words, the address of each key is calculated using the key iteself. The function to transfer the value to the index is called the hush function. 

Isertion, deletion and retrieval occur all in O(1).

#### Collisions: when two items have the same index

Load factor = number of item stored / total size of the hash table

#### Solutions for collisions:

(1) open addressing: place the later item into the next avaiable location, this is called linear probing. You can also use other algorithm to place the items in another address, such as plus 3 rehash, quadratic probing (failed attempts)^2, double hashing

(2) close addressing: used a linked list. The index is the head of the linked list. Items have the same index are stored in the same linked list.

#### Objective of hash function:

(1) minimize collisions

(2) uniform distribution of hash values

(3) easy to calcultate

(4) resolve any collisons

## Tree
Tree is an extension of linked list. Instead of having only one next elements, a tree can have many. A tree can also be visualized as a graph. A tree doesn't have circle, regardless of the directions of the edges. In a tree, there is only one parents node, but one parent node can have many children nodes. Node without any children is called leaves. Node without a parent is called the root. 

The common used tree is a binary tree, which has no more than 2 children for every node.

search - O(N)

delete - O(N)

insert - O(logN)

### Red-black-tree

A way to keep the tree balanced. It has following rules:

1. Each node is either red or black.

2. The root is black. 

3. All leaves (NIL) are black.

4. If a node is red, then both its children are black.

5. Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.

During insertion, you always insert a red node, but it can be changed color later.

## Heap
An array represented by an almost (unless you insert null then it is totally) compeleted binary tree. Although it is a tree structure, it is often stored as an array to save space. 

<img src = images/treevsarray.png height = 200>

When a value is extracted and removed from the heap, it can only come from the root node. In the array from: A node of a tree (i) has parents(i/2) and left node (2 * i) and right node (2 * i + 1), i starting from 1 in root.

Max Heap: The key of a node >= the key of its children

<img src = 'images/heap.png'>


Inserting or removing a node in the max heap is O(logN) - worst case senario need to work all the way up to the root (logN levels)
Creating a max heal is O(N) by doing bottom up - building the heat from the bottom and work the way up, when you reach the top, the worst case is that node need to move all the way down, but as there is less node has large height, we can prove that it has a linear upper bound: https://www.youtube.com/watch?v=MiyLo8adrWw

Doing a heap sort is O(NlogN)

## Graph
A graph is also called network. Tree is a special case of tree. It has nodes (vertices) and edges. Edges can have direction and weights. 

Connectivity: The minimum number of nodes that need to be removed to make a graph become disconnected. 

Graph representation:

Vertex object: edges:xx
Edge object: vertices: xx

1. Edge list:
[[0,1], [1,2], [1,3], [2,3]] each number is the vertex of the edge

<img src = images/graph1.png height = 200>

2. Adjacency list

<img src = images/graph2.png height = 200>

3. Adjacency Matrix

<img src = images/graph2.png height = 200>

Symetric matrix where one edges appears twice. Each row/column represents one vertex. Unless there is an edge linked back to the vertex itself, the central diagnose direction is always zero.

## Acknowledgement:
https://github.com/joeyajames/Python/tree/master/LinkedLists




