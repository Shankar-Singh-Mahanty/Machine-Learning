class BST:
    def __init__(self, key):
        self.key = key
        self.lChild = None
        self.rChild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lChild:
                self.lChild.insert(data)
            else:
                self.lChild = BST(data)
        else:
            if self.rChild:
                self.rChild.insert(data)
            else:
                self.rChild = BST(data)

    def search(self, data):
        if self.key is None:
            print("Tree is empty!")
            return False
        if self.key == data:
            return True
        if self.key > data:
            if self.lChild:
                return self.lChild.search(data)
            else:
                return False
        else:
            if self.rChild:
                return self.rChild.search(data)
            else:
                return False

    def __delitem__(self, key):
        if self.key is None:
            print("Tree is empty!")
            return
        if key < self.key:
            if self.lChild:
                self.lChild = self.lChild.__delitem__(key)

            else:
                print("Given node is not present in the tree.")
        elif key > self.key:
            if self.rChild:
                self.rChild = self.rChild.__delitem__(key)
            else:
                print("Given node is not present in the tree.")
        else:
            if self.lChild is None:
                temp = self.rChild
                return temp
            if self.rChild is None:
                temp = self.lChild
                return temp
            node = self.rChild
            while node.lChild:
                node = node.lChild
            # Replace the current node with the successor node
            node = node
            # Delete the successor node from the right subtree
            del node.rChild[node.key]
        return self

    def inorder(self):
        if self.lChild:
            self.lChild.inorder()
        print(self.key, end=" ")
        if self.rChild:
            self.rChild.inorder()

    def height(self):
        # Base case: empty subtree has height 0
        if self is None:
            return 0
        # Recursive case: non-empty subtree has height 1 + max of left and right subtrees
        else:
            # Check if left child is None
            if self.lChild is None:
                left_height = 0
            else:
                left_height = self.lChild.height()
            # Check if right child is None
            if self.rChild is None:
                right_height = 0
            else:
                right_height = self.rChild.height()
            return 1 + max(left_height, right_height)


root = BST(25)
# Insert 5 elements into the tree.
list1 = [10, 33, 17, 49]
for i in list1:
    root.insert(i)
print("The root node's key is", root.key)
print("After inserting 5 elements into the tree, the inorder traversal is:")
root.inorder()
print()

# Search for a specific element in the tree.
print("Searching for 33 in the tree returns", root.search(33))

# Delete an element from the tree
del root[17]
# Print the tree using inorder traversal.
print("After deleting an element from the tree, the inorder traversal is:")
root.inorder()
print()

# Find the height of the binary search tree.
print("The height of the binary search tree is:", root.height())
