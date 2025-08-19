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
            if current.next:
                current = current.next
            else:
                break

        new_node = Node(data)
        current.next = new_node

    def add_at_head(self, data):
        current = self.head
        new_node = Node(data)

        if current:
            new_node.next = current
        else:
            self.head = new_node

        self.head = new_node

    def delete_node(self, data):
        print(f"delete_node: Deleting {data} ...")
        current = self.head
        if not current:
            print("delete_node: Cannot find the data")
            return

        if current and current.data == data:
            self.head = current.next
            print(f"delete_node: Successfully Deleted - {current.data}")
            return

        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            print("delete_node: Cannot find the data")
            return

        deleted_data = current.next.data
        if current.next.next:
            current.next = current.next.next
        else:
            current.next = None

        print(f"delete_node: Successfully Deleted - {deleted_data}")

    def print_list(self):
        print("Printing List...")
        current = self.head
        if current:
            print(f"{current.data} ")
        else:
            print("print_list: Empty List")

        while current:
            current = current.next
            if current:
                print(f"{current.data} ")

    def is_a_cycle(self):
        slow = fast = self.head
        while slow and fast:
            if fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False

            return True

    def reverse_list(self):
        print("Reversing in Progress...")
        ready_to_break = False
        current = self.head

        if not current:
            print("reverse_list: Cannot reverse. Its a empty list")
            return

        if not current.next:
            print("Cannot reverse. The list has only one element")
            return

        # setting previous | current | after pointers
        previous = current
        current = current.next
        if current.next:
            after = current.next
        else:
            ready_to_break = True

        # reverse logic for head and second node
        previous.next = None
        print(f"Moving the head to Tail. {previous.data} is pointing to None")
        current.next = previous
        print(
            f"Second points to first. {current.data} is pointing to {previous.data}")

        if ready_to_break:
            self.head = current
            return

        while True:
            previous = current
            current = after

            if current.next:
                after = current.next
            else:
                ready_to_break = True

            # reverse logic
            current.next = previous

            print(f"{current.data} is pointing to {previous.data}")
            if ready_to_break:
                self.head = current
                break


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.print_list()
    mylist.insert_node(50)
    mylist.insert_node(50)
    mylist.insert_node(20)
    mylist.insert_node(30)
    mylist.insert_node(40)
    mylist.print_list()
    # mylist.reverse_list()
    mylist.print_list()
    mylist.delete_node(20)
    mylist.delete_node(40)
    mylist.delete_node(10)
    mylist.delete_node(50)
    mylist.delete_node(50)
    mylist.print_list()
    print(f"Is this list a cycle? {mylist.is_a_cycle()}")
