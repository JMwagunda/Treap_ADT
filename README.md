# Treap_ADT
TreapNode Class:

This class represents a node in the Treap data structure. Each node contains an element (the value of the node), left and right pointers (pointing to the left and right children, respectively), and a priority value used for maintaining the heap property.

TreapTree Class:

This class represents the Treap data structure. It contains methods for various operations on the Treap.

Constructor (__init__): Initializes an empty Treap by setting the root to None.

is_empty() Method: Checks if the Treap is empty.

make_empty() Method: Makes the Treap logically empty by setting the root to None.

_insert(x, t) Method: Recursive method to insert a new element x into the Treap rooted at node t.

insert(x) Method: Public method to insert a new element into the Treap. It calls the _insert method.

_rotate_right(y) and _rotate_left(x) Methods: Perform right and left rotations, respectively, to maintain the heap property of the Treap during insertion.

_search(x, t) Method: Recursive method to search for an element x in the Treap rooted at node t.

search(x) Method: Public method to search for an element in the Treap. It calls the _search method.

_count_nodes(t) Method: Recursive method to count the number of nodes in the Treap rooted at node t.

count_nodes() Method: Public method to get the total number of nodes in the Treap. It calls the _count_nodes method.

_inorder(t), _preorder(t), _postorder(t) Methods: Recursive methods to perform inorder, preorder, and postorder traversals, respectively, on the Treap rooted at node t.

inorder(), preorder(), postorder() Methods: Public methods to get lists representing the inorder, preorder, and postorder traversals, respectively. These methods call the corresponding recursive traversal methods.

Main Program:
The main part of the program is a loop where the user can choose different operations to perform on the Treap: insertion, search, counting nodes, checking if the Treap is empty, and making the Treap empty.

After each operation, the program displays the Treap in inorder, preorder, and postorder traversals.

The program continues to run until the user chooses to exit.