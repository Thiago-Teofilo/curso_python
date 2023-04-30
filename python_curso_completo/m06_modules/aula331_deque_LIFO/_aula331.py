from collections import deque
import os

os.system("cls")


queue: deque[int] = deque()
queue.append(3)
queue.append(4)
queue.append(5)
queue.appendleft(8)

queue.popleft()
print(queue)