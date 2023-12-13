# Implement a singly linked list in python to perform the following operations.
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def delete_begin(self):
        if self.head is None:
            print("LL is empty. So, can't delete nodes.")
        else:
            self.head = self.head.ref

    def search(self, ll, key):
        if self.head is None:
            return False
        if ll.data == key:
            return True
        return self.search(ll.ref, key)

    @staticmethod
    def reversePrint(head):
        if head is None:
            return
        LinkedList.reversePrint(head.ref)
        print(head.data, "--->", end=" ")


LL1 = LinkedList()

# Insert 5 elements at the beginning of the list.
LL1.add_begin(10)
LL1.add_begin(25)
LL1.add_begin(49)
LL1.add_begin(63)
LL1.add_begin(98)  # 10 will be printed at last due to insertion at beginning.
print("Created Linked List is:-")
LL1.print_LL()

# Delete an element from the list.
LL1.delete_begin()
print("\nUpdated Linked List is:-")
LL1.print_LL()

# Search for a specific element in the list.
value = 49
found = LL1.search(LL1.head, value)
if found:
    print(f"\n{value} is present in the linked list.")
else:
    print(f"\n{value} is not present in the linked list.")

# Print the elements of the list in reverse order.
print("Linked List in reverse order is:-")
LL1.reversePrint(LL1.head)
