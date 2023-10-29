# Treap_ADT

* A treap is a binary search tree that maintains a heap property. Each node in the treap has two attributes: a key and a priority. The keys follow the binary search tree property, and the priorities follow the max-heap property. 
* Specifically, for any node in the treap, the key of the node is greater than or equal to all keys in its left subtree and less than or equal to all keys in its right subtree. 
* The priorities are assigned randomly, and the treap is constructed such that the priorities satisfy the max-heap property. 
* This combination of properties ensures that the treap is both a binary search tree and a max-heap, allowing efficient search, insertion, and deletion operations.
* The key operations in a treap include rotation, searching, insertion, and deletion. Rotations are used to maintain the heap property during insertion and deletion. 
* There are two types of rotations: right rotation and left rotation. Right rotation is performed when a left child has a higher priority than its parent, and left rotation is performed when a right child has a higher priority than its parent. * These rotations are used to maintain the max-heap property after insertion and deletion operations. Searching in a treap is similar to searching in a regular binary search tree. 
* Insertion involves adding a new node with a given key and a randomly generated priority while maintaining the treap properties. 
* Deletion removes a node with a given key from the treap while preserving the binary search tree and max-heap properties. 
* Treaps find applications in various areas such as randomized binary search trees, priority queues, and optimization algorithms where balancing search and insertion operations is crucial for performance.

# CODE
TreapNode Class:

This class represents a node in the Treap data structure. Each node contains an element (the value of the node), left and right pointers (pointing to the left and right children, respectively), and a priority value used for maintaining the heap property.

## Methods
|Operations| Specifications|
|----------|---------------|
|Constructor (__init__)|: Initializes an empty Treap by setting the root to None.
|is_empty() Method|: Checks if the Treap is empty.
|make_empty() Method|: Makes the Treap logically empty by setting the root to None.
|_insert(x, t) Method|: Recursive method to insert a new element x into the Treap rooted at node t.
|insert(x) Method|: Public method to insert a new element into the Treap. It calls the _insert method.
|_rotate_right(y) and _rotate_left(x) Methods|: Perform right and left rotations, respectively, to maintain the heap property of the Treap during insertion.
|_search(x, t) Method|: Recursive method to search for an element x in the Treap rooted at node t.
|search(x) Method|: Public method to search for an element in the Treap. It calls the _search method.
|_count_nodes(t) Method|: Recursive method to count the number of nodes in the Treap rooted at node t.
|count_nodes() Method|: Public method to get the total number of nodes in the Treap. It calls the _count_nodes method.
|_inorder(t), _preorder(t), _postorder(t) Methods|: Recursive methods to perform inorder, preorder, and postorder traversals, respectively, on the Treap rooted at node t.
|inorder(), preorder(), postorder() Methods|: Public methods to get lists representing the inorder, preorder, and postorder traversals, respectively. These methods call the corresponding recursive traversal methods.

##Main Program:
The main part of the program is a loop where the user can choose different operations to perform on the Treap: insertion, search, counting nodes, checking if the Treap is empty, and making the Treap empty.

After each operation, the program displays the Treap in inorder, preorder, and postorder traversals.

The program continues to run until the user chooses to exit.

