from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            node = Node(value)
            self.root = node
            print(f"Adding first element: {self.root.value}")
            return

        current_node = self.root
        while True:
            if current_node.value < value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    node = Node(value)
                    current_node.right = node
                    # current_node = current_node.right
                    return
            else:
                if current_node.left:
                    current_node = current_node.left
                else:
                    node = Node(value)
                    current_node.left = node
                    # current_node = current_node.left
                    return

    def delete(self, value):
        pass

    def in_order_traversal(self):
        current = self.root
        print(f"The value of root = {current.value}")
        stack = []
        res = []

        while current is not None or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            res.append(current.value)
            current = current.right

        return res

    def recursive_inorder_traversal(self):
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            result.append(node.value)
            dfs(node.right)

        dfs(self.root)
        return result

    def pre_order_traversal(self):
        stack = [self.root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.value)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res

    def recursive_preorder_traversal(self):
        result = []

        def dfs(node):
            if node is None:
                return

            result.append(node.value)
            dfs(node.left)
            dfs(node.right)

        dfs(self.root)
        return result

    def post_order_traversal(self):
        current = self.root
        stack = []
        res = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.right

            current = stack.pop()
            res.append(current.value)

            current = current.left

        return res

    def recursive_postorder_traversal(self):
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.right)
            result.append(node.value)
            dfs(node.left)

        dfs(self.root)
        return result

    def find_height(self):
        if not self.root:
            return 0

        height = 0
        q = deque()
        q.append(self.root)
        q.append(None)

        while q:
            node = q.popleft()
            if node is None:
                height += 1

                if q:
                    q.append(None)

            else:
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return height

    def validate_bst(self):
        result = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            result.append(node.value)
            if node.right:
                dfs(node.right)

        dfs(self.root)
        print(result)

        for i in range(len(result)-1):
            if result[i] > result[i+1]:
                return False

        return True

    def node_path(self, value):
        result = []
        node = self.root
        result.append(node.value)
        while True:
            if node.value == value:
                return result

            if node.value < value:
                node = node.right
            else:
                node = node.left

            result.append(node.value)

        return -1

    def find_lowest_common_ancestor(self, list1, list2):
        i = len(list1) - 1
        j = len(list2) - 1
        while i > 0 and j > 0:
            if list1[i] == list2[j]:
                return list1[i]
            elif list1[i] < list2[j]:
                j -= 1
            else:
                i -= 1

        return -1


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(4)
    bst.insert(3)
    bst.insert(10)
    bst.insert(6)
    bst.insert(15)
    bst.insert(11)
    bst.insert(12)
    bst.insert(13)
    bst.insert(17)
    print(f"The inorder traversal: {bst.in_order_traversal()}")
    print(
        f"The recursive inorder traversal: {bst.recursive_inorder_traversal()}")
    print(f"The preorder traversal: {bst.pre_order_traversal()}")
    print(
        f"The recursive preorder traversal: {bst.recursive_preorder_traversal()}")
    print(f"The postorder traversal: {bst.post_order_traversal()}")
    print(
        f"The recursive postorder traversal: {bst.recursive_postorder_traversal()}")
    print(f"The height of the tree is {bst.find_height()}")
    print(f"Is this a binary search tree: {bst.validate_bst()}")
    print(f"The node path for 17 is {bst.node_path(17)}")
    print(f"The node path for 17 is {bst.node_path(6)}")
    list1 = bst.node_path(17)
    list2 = bst.node_path(13)
    print(
        f"The lowest common ancestors for 17 and 13 is {bst.find_lowest_common_ancestor(list1, list2)}")
