import random

class TreapNode:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right
        self.priority = random.randint(1, 1000000)

class TreapTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def make_empty(self):
        self.root = None

    def _insert(self, x, t):
        if t is None:
            return TreapNode(x)
        if x < t.element:
            t.left = self._insert(x, t.left)
            if t.left.priority < t.priority:
                t = self._rotate_right(t)
        elif x > t.element:
            t.right = self._insert(x, t.right)
            if t.right.priority < t.priority:
                t = self._rotate_left(t)
        return t

    def insert(self, x):
        self.root = self._insert(x, self.root)

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _search(self, x, t):
        if t is None:
            return False
        if x < t.element:
            return self._search(x, t.left)
        elif x > t.element:
            return self._search(x, t.right)
        else:
            return True

    def search(self, x):
        return self._search(x, self.root)

    def _count_nodes(self, t):
        if t is None:
            return 0
        return 1 + self._count_nodes(t.left) + self._count_nodes(t.right)

    def count_nodes(self):
        return self._count_nodes(self.root)

    def _inorder(self, t):
        if t is not None:
            yield from self._inorder(t.left)
            yield t.element
            yield from self._inorder(t.right)

    def inorder(self):
        return list(self._inorder(self.root))

    def _preorder(self, t):
        if t is not None:
            yield t.element
            yield from self._preorder(t.left)
            yield from self._preorder(t.right)

    def preorder(self):
        return list(self._preorder(self.root))

    def _postorder(self, t):
        if t is not None:
            yield from self._postorder(t.left)
            yield from self._postorder(t.right)
            yield t.element

    def postorder(self):
        return list(self._postorder(self.root))

# Main function
if __name__ == "__main__":
    treap = TreapTree()

    while True:
        print("\nSelect one of the operations for the Treap Data Structure\n")
        print("1. To insert a new node in the Treap Data Structure.")
        print("2. To Search a node from the Treap Data Structure.")
        print("3. To count nodes in the Treap Data Structure.")
        print("4. To check if the Treap Data Structure is empty?.")
        print("5. To make Treap Data Structure empty.")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter integer element to insert: "))
            treap.insert(value)
        elif choice == 2:
            value = int(input("Enter integer element to search: "))
            print("Search result:", treap.search(value))
        elif choice == 3:
            print("Nodes =", treap.count_nodes())
        elif choice == 4:
            print("Empty status =", treap.is_empty())
        elif choice == 5:
            print("\nTreap Cleared")
            treap.make_empty()
        else:
            print("Wrong Entry")

        print("\nIn-order:", treap.inorder())
        print("Pre-order:", treap.preorder())
        print("Post-order:", treap.postorder())

        continue_operation = input("Do you want to continue? (Type 'y' or 'n'): ").lower()
        if continue_operation != 'y':
            break
