class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU:
    # Cache is represented in Key, Value pair
    # Cache when requested, it must be obtained in O(1)
    # Cache must have a limit
    #
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lru_dictionary = {}

    def current_capacity(self):
        count = 0
        node = self.head.next
        while node != self.tail:
            count += 1
            node = node.next
        return count

    def remove_last(self):
        remove_node = self.tail.prev
        prev_node = remove_node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        del self.lru_dictionary[remove_node.key]

    def add_to_front(self, key, value):
        if self.current_capacity == self.capacity:
            self.remove_last()

        node = Node(key, value)
        self.lru_dictionary[key] = node
        front_node = self.head.next
        self.head.next = node
        node.prev = self.head
        front_node.prev = node
        node.next = front_node

    def get(self, key):
        value = None
        if key in self.lru_dictionary.keys():
            value = self.lru_dictionary[key].value

        return value

    def put(self, key, value):
        node = Node(key, value)
        self.add_to_front()
        pass


if __name__ == "__main__":
    lru = LRU(capacity=5)
    lru.put(1, 100)
    lru.put(2, 200)
    lru.get(5)
