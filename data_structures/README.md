# Data Structures
Resources:

https://www.coursera.org/learn/data-structures/home/welcome

https://leetcode.com/explore/

## Link List
In python, every time when you insert an element to a list, new storage of the entire list will be created and the elemenets need to be shifted to move room. This means it is quite not efficient when the list is large. Therefore, in this situation, we used link list instead, which doesn't recreate the storage neither does it require shifting. However, it does eliminate the constant time direct element access available with the array and Python list. As its name implies, the link strucutre has to been accessed based on the 'link order'. The singly linked list is a linear structure in which traversals start at the front and progress, one element at a time, to the end. Other variations include the circularly linked, the doubly linked, and the circularly doubly linked lists.

## Heap
An array represented by an almost (unless you insert null then it is totally) compeleted binary tree. When a value is extracted and removed from the heap, it can only come from the root node. A node of a tree (i) has parents(i/2) and left node (2 * i) and right node (2 * i + 1), i starting from 1 in root.

Max Heap: The key of a node >= the key of its children

<img src = 'images/heap.png'>


Inserting or removing a node in the max heap is O(logN) - worst case senario need to work all the way up to the root (logN levels)
Creating a max heal is O(N) by doing bottom up - building the heat from the bottom and work the way up, when you reach the top, the worst case is that node need to move all the way down, but as there is less node has large height, we can prove that it has a linear upper bound: https://www.youtube.com/watch?v=MiyLo8adrWw

Doing a heap sort is O(NlogN)

## Acknowledgement:
https://github.com/joeyajames/Python/tree/master/LinkedLists




