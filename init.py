class Node:
    """
    A single node in a Singly Linked List.
    Contains data and a reference to the next node.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None  # Pointer to the next node in the list

    def __repr__(self):
        """Provides a helpful string representation for debugging."""
        return f"Node(data={self.data})"

class SinglyLinkedList:
    """
    Basic implementation of a Singly Linked List with a simple insertion method.
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        """Inserts a new node at the head of the list (O(1))."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def print_list(self):
        """Traverses the list and prints all data."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# Example Usage:
# llist = SinglyLinkedList()
# llist.insert_at_beginning(30)
# llist.insert_at_beginning(20)
# llist.insert_at_beginning(10)
# llist.print_list() # Output: 10 -> 20 -> 30 -> None
