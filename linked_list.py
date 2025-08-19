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
        if not current:
            print("insert_node: Head is empty")
            self.head = Node(data)
            return

        while current:
            print("insert_node: Moving to next node")
            if current.next:
                current = current.next
            else:
                break

        new_node = Node(data)
        current.next = new_node

    def delete_node(self, data):
        pass

    def print_list(self):
        current = self.head
        if current:
            print(f"print_list: {current.data}")
        else:
            print("print_list: Empty List")

        while current:
            current = current.next
            if current:
                print(f"print_list: {current.data}")


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.print_list()
    mylist.insert_node(10)
    mylist.insert_node(20)
    mylist.insert_node(30)
    mylist.insert_node(40)
    mylist.print_list()
