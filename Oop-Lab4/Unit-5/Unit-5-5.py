# Page 18
# Example 6 : Using lisst as stacks and queues

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped_item = stack.pop()
print("Popped item from stack:", popped_item)

from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
dequeued_item = queue.popleft()
print("Dequeued item from queue:", dequeued_item)    