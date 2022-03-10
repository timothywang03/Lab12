# File: MinPriorityQueue.py

class MinPriorityQueue:
    def __init__(self):
        self.arr = list(None for x in range(10))
        self.size = 0

    def getSize(self):
        return self.size

    def getMin(self):
        return self.arr[0]

    def minHeapify(self, i):
        left = i * 2
        right = i * 2 + 1
        if left < self.size and self.arr[left] < self.arr[i]:
            smallest = left
        else:
            smallest = i
        if right < self.size and self.arr[right] < self.arr[smallest]:
            smallest = right

        if smallest != i:
            mid = self.arr[i]
            self.arr[i] = self.arr[smallest]
            self.arr[smallest] = mid

            self.minHeapify(self, smallest)

    def extractMin(self):
        if self.size < 1:   # makes sure that the queue is not empty
            return 'Heap Underflow'
        smallest = self.arr[1]
        self.arr[1] = self.arr[self.size]
        self.arr -= 1
        self.minHeapify(1)

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


queue = MinPriorityQueue()
queue.insert(4)
queue.insert(2)
queue.insert(1)
queue.insert(5)
queue.insert(3)
print(queue.arr)
