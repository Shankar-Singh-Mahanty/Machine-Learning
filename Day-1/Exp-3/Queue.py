# Implement a queue using python list to perform the following operations.
queue = []
print("Queue: ", queue)

# Enqueue 5 elements into the queue.
queue.append(2)
queue.append(1)
queue.append(7)
queue.append(8)
queue.append(5)
print("Queue: ", queue)

# Dequeue 3 elements from the queue.
print(queue.pop(0), " is popped")
print(queue.pop(0), " is popped")       # FIFO
print(queue.pop(0), " is popped")
print("Updated queue: ", queue)

# Check if the queue is empty.
if queue == []:
    print("True: queue is empty.")
else:
    print("False: queue is not empty.")
