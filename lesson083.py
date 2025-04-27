
CAPACITY = 10

# Maximum heap (root node will be the largest item)
class HEAP:

    def __init__(self):
        # This is the actual number of items in the data structure
        self.heap_size = 0
        # The underlying list data structure
        self.heap = [0]*CAPACITY

    def insert(self, item):

        # When the heap is full
        if self.heap_size == CAPACITY:
            return

        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1

        # Check the heap properties
        self.fix_up(self.heap_size-1)

    # Starting with the actual node we have inserted up to the root node
    # We have to compare the values whether to make swap operations
    # O(logN) running time complexity
    def fix_up(self):
        pass

