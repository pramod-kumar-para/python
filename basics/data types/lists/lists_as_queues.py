
from collections import deque

numbers=deque([1,2,3,4])
numbers.append(5)
numbers.append(6)
numbers.append(7)
print(numbers)
numbers.popleft()
print(numbers)
numbers.popleft()
print(numbers)