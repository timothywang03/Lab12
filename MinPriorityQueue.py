# File: MinPriorityQueue.py - Timothy Wang

from random import randint


class MinPriorityQueue:
    def __init__(self, capacity):
        self.arr = list(None for x in range(capacity))
        self.size = 0
        self.capacity = capacity

    def getSize(self):
        return self.size

    def getArr(self):
        return self.arr

    def getCapacity(self):
        return self.capacity

    def minHeapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2

        # finds the minimum value amongst the current, left, and right
        if left < self.size and self.arr[left] < self.arr[i]:
            smallest = left
        else:
            smallest = i
        if right < self.size and self.arr[right] < self.arr[smallest]:
            smallest = right

        # replaces the minimum values
        if smallest != i:
            mid = self.arr[i]
            self.arr[i] = self.arr[smallest]
            self.arr[smallest] = mid

            self.minHeapify(smallest)

    def extractMin(self):
        if self.size < 1:   # makes sure that the queue is not empty
            return 'Heap Underflow'
        smallest = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1

        # replaces the root node with the last value, removes the last value
        self.arr[self.size] = None

        # calls the organizing function to reheapify
        self.minHeapify(0)
        return smallest

    def insert(self, key):
        self.size += 1  # increments queue size to accomodate new queue entry
        self.arr[self.size - 1] = 999999999999999
        if key > self.arr[self.size - 1]:
            return 'New key smaller than current key'

        self.arr[self.size - 1] = key   # set the new space to the new key
        i = self.size - 1
        while i > 0 and self.arr[i // 2] > self.arr[i]:
            mid = self.arr[i]
            self.arr[i] = self.arr[i // 2]
            self.arr[i // 2] = mid
            i = i // 2


queue = MinPriorityQueue(10)
queue.insert(4)
queue.insert(2)
queue.insert(1)
queue.insert(5)
queue.insert(3)
queue.extractMin()
queue.extractMin()
print(queue.arr)


def k_values():
    """Given a random list of 1000 integers, read them one by one and save the largest values in the min_queue"""
    queue = MinPriorityQueue(10)    # setting 10 as the k value
    numbers = list(randint(0, 1000) for x in range(1000))
    for x in numbers:
        if queue.getSize() == queue.getCapacity():
            queue.extractMin()
        queue.insert(x)
    print(queue.arr)


k_values()
