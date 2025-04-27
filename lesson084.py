
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
    def fix_up(self, index):

        parent_index = (index-1)//2

        # We consider all the items above till we hit the root node
        # If heap property is violated then we swap the parent-child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    # peek() return with the max item in O(1)
    def get_max(self):
        return self.heap[0]

    # Return the max and removes it as well
    # Remove the root node of the heap
    def poll(self):

        max_item = self.get_max()

        # Swap the root node with the last item and "heapify"
        self.heap[0], self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
        self.heap_size = self.heap_size - 1

        # Make sure the heap is "heapify"
        self.fix_down(0)

        return max_item

    # Starting with the root node downwards until the heap properties are no longer
    # violated - O(logN
    def fix_down(self, index):

        index_left = 2 * index + 1
        index_right = 2 * index + 2

        # in a max heap the parent is always greater than the children
        largest_index = index

        # Looking for the largest (parent or left node)
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            largest_index = index_left

        # If the right child is greater than the left child: largest is the right child
        if index_right < self.heap_size and self.heap[index_right] > self.heap[largest_index]:
            largest_index = index_right

        # If the parent is larger than the children: it is a valid heap so we terminate the
        # recursive function calls
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)





