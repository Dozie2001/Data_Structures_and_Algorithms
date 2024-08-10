"""An Implementation of a LinkedList
Inserting values at the Start of a LinkedList - O(1)
Inserting Values at the middle - O(n)
Reading or accessing indexed Value - O(n)
Deleting Values at the begining - O(1)
Deleting Values in the middle - O(n)
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next



class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def __repr__(self) -> str:
        if self.head is None:
            return "Linked list is Empty"
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '->'
            itr = itr.next

        return llstr
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_value(self, data: list):
        self.head = None

        for d in data:
            self.insert_at_end(d)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        

        return count
    
    def remove(self, index):
        count = self.get_length()
        if index < 0 or index >= count:
            raise ValueError("Invalid Index")

        if index == 0:
            self.head = self.head.next
        itr = self.head


        for i in range(count):
            if i == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self, index, data):
        count = self.get_length()

        if index < 0 or index >= count:
            raise ValueError("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        for i in range(count):
            if i == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next



if __name__ == "__main__":
    new = LinkedList()
    new.get_length()
    new.insert_value(['I', 'm', 'name'])
    print(new)
    print(new)
    new.insert_at(2, 3)
    print(new)
