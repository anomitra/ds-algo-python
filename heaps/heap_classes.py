class Heap(object):

    def __init__(self):
        self.array = [-1]

    def size(self):
        return len(self.array) - 1

    def show(self):
        print(*self.array[1:], sep=' ')

    def move_up(self, index):
        return NotImplementedError()

    def insert(self, element):
        self.array.append(element)
        self.move_up(self.size())

    def pop(self):
        current_size = self.size()
        element = self.array[1]
        self.array[1] = self.array[current_size]
        self.array = self.array[:-1]
        self.move_down(1)
        return element

    def move_down(self, index):
        return NotImplementedError()

    def heapify(self, array):
        self.array = [-1] + array[:]
        mid = len(array) // 2
        for i in range(mid, 0, -1):
            self.move_down(i)

    def peek(self):
        return None if self.size() == 0 else self.array[1]


class MinHeap(Heap):

    def move_up(self, index):
        while index // 2 > 0:
            if self.array[index] < self.array[index // 2]:
                temp = self.array[index]
                self.array[index] = self.array[index // 2]
                self.array[index // 2] = temp
            index = index // 2

    def move_down(self, index):

        while True:
            min_below = self.min_child(index)
            if min_below and self.array[min_below] < self.array[index]:
                self.array[min_below], self.array[index] = self.array[index], self.array[min_below]
            else:
                return
            index = min_below

    def min_child(self, index):

        if index * 2 < self.size():

            left = index * 2
            right = index * 2 + 1
            l_val = self.array[left]
            r_val = self.array[right] if self.size() > right else None
            if not r_val:
                return left
            else:
                if l_val > r_val:
                    return right
                else:
                    return left


class MaxHeap(Heap):

    def move_up(self, index):
        while index // 2 > 0:
            if self.array[index] > self.array[index // 2]:
                temp = self.array[index]
                self.array[index] = self.array[index // 2]
                self.array[index // 2] = temp
            index = index // 2

    def move_down(self, index):

        while True:
            min_below = self.min_child(index)
            if min_below and self.array[min_below] > self.array[index]:
                self.array[min_below], self.array[index] = self.array[index], self.array[min_below]
            else:
                return
            index = min_below

    def min_child(self, index):

        if index * 2 < self.size():

            left = index * 2
            right = index * 2 + 1
            l_val = self.array[left]
            r_val = self.array[right] if self.size() > right else None
            if not r_val:
                return left
            else:
                if l_val < r_val:
                    return right
                else:
                    return left

# heap = MaxHeap()
# for i in range(1, 17):
#     heap.insert(i)
# for i in range(16):
#     heap.pop()
#     # heap.show()
