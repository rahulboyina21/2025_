Here’s your complete Python Recap in Markdown format:

# 🐍 Python Recap: Syntax & Essentials

## **1️⃣ Basic Python Syntax**
```python
# Variables and Data Types
x = 10        # Integer
y = 3.14      # Float
name = "Rahul" # String
is_valid = True # Boolean
lst = [1, 2, 3] # List
tpl = (4, 5, 6) # Tuple (Immutable)
st = {7, 8, 9}  # Set (Unique elements)
dct = {'key': 'value'} # Dictionary

# Printing
print("Hello, Python!") 

# Type Checking
print(type(x))  # <class 'int'>

2️⃣ Conditional Statements

x = 10
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Smaller")

3️⃣ Loops

# For loop
for i in range(5):  # 0,1,2,3,4
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

4️⃣ Functions

def add(a, b):
    return a + b

print(add(3, 4))  # Output: 7

5️⃣ List & Dictionary Comprehension

# List Comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Dictionary Comprehension
square_dict = {x: x**2 for x in range(5)} # {0:0, 1:1, 2:4, 3:9, 4:16}

6️⃣ Lambda Functions

add = lambda x, y: x + y
print(add(5, 10))  # 15

7️⃣ Exception Handling

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Done")

8️⃣ Classes & OOP

class Car:
    def __init__(self, brand):
        self.brand = brand  # Instance Variable

    def drive(self):
        return f"{self.brand} is driving"

# Object
my_car = Car("Tesla")
print(my_car.drive())  # Tesla is driving

9️⃣ Sorting

nums = [5, 2, 9, 1]
nums.sort()  # Ascending [1,2,5,9]
nums.sort(reverse=True)  # Descending [9,5,2,1]
sorted_list = sorted(nums)  # Returns a new sorted list

🔟 Built-in Functions

nums = [1, 2, 3, 4]
print(sum(nums))  # 10
print(len(nums))  # 4
print(max(nums))  # 4
print(min(nums))  # 1
print(abs(-10))   # 10

1️⃣1️⃣ String Operations

s = "Hello, World"
print(s.lower())  # hello, world
print(s.upper())  # HELLO, WORLD
print(s.split(",")) # ['Hello', ' World']
print("Rahul" in s)  # False

1️⃣2️⃣ Python Data Structures (Important for DSA)

Lists

arr = [1, 2, 3]
arr.append(4)  # [1,2,3,4]
arr.pop()      # Removes last element
arr.insert(1, 100)  # Inserts 100 at index 1

Tuples (Immutable)

tpl = (1, 2, 3)
print(tpl[0])  # 1

Sets (Unique)

s = {1, 2, 3, 3}  # {1, 2, 3}
s.add(4)
s.remove(2)
print(s)

Dictionaries (HashMaps)

d = {'name': 'Rahul', 'age': 25}
print(d['name']) # Rahul
d['age'] = 26  # Modify value
d['new_key'] = "new_value" # Add new key

1️⃣3️⃣ Important Python Libraries
	•	NumPy - Arrays & Math
	•	Pandas - Data Handling
	•	Matplotlib - Visualization
	•	Scikit-learn - ML
	•	TensorFlow / PyTorch - Deep Learning
	•	NetworkX - Graphs
	•	Collections - Advanced Data Structures
	•	Heapq - Priority Queues
	•	Deque (collections.deque) - Faster Queue Operations

1️⃣4️⃣ Algorithms & DSA Essentials in Python

Recursion

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

Sorting (QuickSort)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))

Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 3))  # 2

Stack & Queue

from collections import deque

stack = []  # Stack (LIFO)
stack.append(1)
stack.append(2)
stack.pop()

queue = deque()  # Queue (FIFO)
queue.append(1)
queue.append(2)
queue.popleft()

Graph BFS/DFS

from collections import deque

graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}

# BFS
def bfs(start):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(1)  # 1 2 3 4 5 6
