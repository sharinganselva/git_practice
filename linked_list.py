class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        pass

    def insert_node(self, data):
        current = self.head
        while current.next:
            current = current.next

        new_node = Node(data)
        current.next = new_node

    def delete_node(self, data):
        pass

    def print_list(self):
        current = self.head
        if current:
            print(current.data)
        else:
            print("Empty List")

        while current.next:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.print_list()
    mylist.insert_node(10)
    mylist.print_list()
    mylist.insert_node(20)
    mylist.print_list()
