import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # should add an item to the back of the queue.
        self.storage.add_to_tail(value) 

        # increment the size
        self.size += 1
        
    def dequeue(self):
        # should remove and return an item from the front of the queue.
        if self.size == 0:
            return

        else:
            value = self.storage.remove_from_head()

            # decrease size
            self.size -= 1

        return value

    def len(self):
        # returns the number of items in the queue.
        return self.storage.__len__()
