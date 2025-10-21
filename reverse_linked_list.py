class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_linked_list(self):
        prev = None
        node = self.head
        while node is not None:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        self.head = prev
        return


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.reverse_linked_list()
