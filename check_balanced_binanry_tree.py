class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def validate_tree(self):
        node = self.root
        height = 0

        def check_height(node):
            if node is None:
                return 0

            left_height = check_height(node.left)
            # if left_height == -1:
            #     return -1

            right_height = check_height(node.right)
            # if right_height == -1:
            #     return -1

            height = max(left_height, right_height) + 1
            print(f"height = {height}")
            return height

        return height


if __name__ == "__main__":
    pass
