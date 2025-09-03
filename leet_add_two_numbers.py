from linked_list import LinkedList, Node


def add_two_numbers(head1: Node, head2: Node):
    node1 = head1
    number1sum = node1.data
    node2 = head2
    number2sum = node2.data

    ten_multiple = 1
    while node1.next is not None:
        node1 = node1.next
        ten_multiple *= 10
        number1sum += node1.data * ten_multiple

    ten_multiple = 1
    while node2.next is not None:
        node2 = node2.next
        ten_multiple *= 10
        number2sum += node2.data * ten_multiple

    return number1sum + number2sum


def create_list(my_list: LinkedList, n):
    while n > 0:
        last_digit = n % 10
        my_list.insert_node(last_digit)
        n = n // 10

    return my_list.head


if __name__ == "__main__":
    list1 = LinkedList()
    list1.head = create_list(list1, 109)
    list1.print_list()

    list2 = LinkedList()
    list2.head = create_list(list2, 209)
    list2.print_list()

    total = add_two_numbers(list1.head, list2.head)
    print(f"The total is = {total}")
    list3 = LinkedList()
    list3.head = create_list(list3, total)
    list3.print_list()
