# Search
## Binary search
Use the divide and conqueue algorithm, to cut the sorted array by half and compare.

## Sort
### Bubble sort

Compare every two elements one by one for N-1 times, each time, the largest element will bubble up to the right. It is an inplace algorithm that doesn't require extra memory.

Time complexicity: O(N^2)

Space complexicity: O(1)

<img src = images/Bubble-sort-example-300px.gif>

image from wikipedia: By Swfung8 - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=14953478

### Merge sort
Another example of divide and conqueue. First divide the list into the smallest unit (1 element), then compare each element with the adjacent list to sort and merge the two adjacent lists. Finally all the elements are sorted and merged.

Time complexicity: O(NlogN)

Space complexicity: O(N)

<img src = images/Merge-sort-example-300px.gif>

### Quick sort
It is another inplace algorithm. It chose a pivot and move everything larger than it to one side, and everything smaller than it to another side. The pivot is the element that is in the correct position after the iteration. The worst case, it has time complexicity of N^2. However, the average time complexicity is NlogN. 


Space complexicity: O(N)

<img src = images/Sorting_quicksort_anim.gif>

image from wikipedia: By en:User:RolandH, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=1965827


