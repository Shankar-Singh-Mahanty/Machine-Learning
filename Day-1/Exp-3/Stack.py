# Implement a stack using a python list to perform the following operations.
stack = []
print("Stack: ", stack)

# Push 5 elements onto the stack.
stack.append(8)
stack.append(2)
stack.append(6)
stack.append(0)
stack.append(5)
print("Stack: ", stack)

# Pop 2 elements from the stack.
print(stack.pop(), " is popped.")      # LIFO
print(stack.pop(), " is popped.")
print("Updated Stack: ", stack)

# Check if the stack is empty.
if stack == []:
    print("True: Stack is empty.")
else:
    print("False: Stack is not empty.")
