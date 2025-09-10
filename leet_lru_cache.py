class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.dict = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def remove_from_cache(self, node):
        next = node.next
        prev = node.prev

        node.prev.next = next
        node.next.prev = prev

    def get_from_cache(self, key):
        if key not in self.dict:
            raise KeyError(f"Key {key} not found in Cache")

        node = self.dict[key]
        self.remove_from_cache(node)
        self.add_to_front(node)
        return node.value

    def put_to_cache(self, key, value):
        if key not in self.dict:
            node = Node(key, value)
            self.dict[key] = node
            if len(self.dict.keys()) >= self.capacity:
                lru = self.tail.prev
                self.remove_from_cache(lru)
                del (self.dict[lru.key])
            self.add_to_front(node)
        else:
            node = self.dict[key]
            self.remove_from_cache(node)
            node.value = value
            self.add_to_front(node)

    def print_lru_keys(self):
        node = self.head
        print("The Linked List")
        while node.next is not None:
            print(f"The linked list key: {node.key} and value: {node.value}")
            node = node.next


if __name__ == "__main__":
    my_cache = LRUCache(5)
    my_cache.put_to_cache(1, 100)
    my_cache.put_to_cache(2, 200)
    my_cache.put_to_cache(3, 300)
    my_cache.print_lru_keys()
    print(f"Getting from cache for key 1: {my_cache.get_from_cache(1)}")
    print(f"Getting from cache for key 2: {my_cache.get_from_cache(2)}")
    my_cache.put_to_cache(1, 1000)
    my_cache.print_lru_keys()
    my_cache.put_to_cache(4, 400)
    my_cache.put_to_cache(5, 500)
    my_cache.put_to_cache(6, 600)
    my_cache.put_to_cache(6, 6000)
    my_cache.print_lru_keys()
