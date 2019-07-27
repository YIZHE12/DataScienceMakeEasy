# Search
## Binary search
Use the divide and conqueue algorithm, to cut the sorted array by half and compare.

## Sort
### Bubble sort
Compare every two elements one by one for N-1 times, each time, the largest element will bubble up to the right. It is an inplace algorithm that doesn't require extra memory.

Time complexicity: O(N^2)

Space complexicity: O(1)

### Merge sort
Another example of divide and conqueue. First divide the list into the smallest unit (1 element), then compare each element with the adjacent list to sort and merge the two adjacent lists. Finally all the elements are sorted and merged.

<img src = images/Merge-sort-example-300px.gif>

Time complexicity: O(NlogN)

Space complexicity: O(N)

