"""
We are given a list of N unsorted elements, we need to find minimum number of steps in which the elements of the
list can be added to make all the elements greater than or equal to K. We are allowed to add two elements together and
make them one.
"""
from heaps.heap_classes import MinHeap


def change_array(array, min_elem):
    heap = MinHeap()
    heap.heapify(array)
    operations = 0
    while heap.peek() < min_elem:
        a = heap.pop()
        b = heap.pop()
        heap.insert(a + b)
        operations += 1
    return operations


print(change_array([1, 10, 12, 9, 2, 3], 6))
