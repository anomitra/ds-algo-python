"""
There are given n ropes of different lengths, we need to connect these ropes into one rope.
The cost to connect two ropes is equal to sum of their lengths. We need to connect the ropes with minimum cost.
"""
from heaps.heap_classes import MinHeap


def connect_ropes(arr):
    heap = MinHeap()
    heap.heapify(arr)
    cost = 0
    while heap.size() != 1:
        smallest = heap.pop()
        second_smallest = heap.pop()
        joining_cost = smallest + second_smallest
        cost += joining_cost
        heap.insert(joining_cost)
    return cost


arr = [4, 3, 2, 6]
print(connect_ropes(arr))
