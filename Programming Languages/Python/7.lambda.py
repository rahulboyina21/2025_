# Lambda values 1,2,3,4,5,6,7 : Expression 

var = lambda a,b,c: a+b+c 

print(var(1,2,3))

var1 = lambda a:sorted(a)

print(var1((2,12,12,1435,46,57,8,87,979,-123)))

# 🚀 When to Use Lambda?

# ✅ When you need a short, one-line function.
# ✅ When using map(), filter(), reduce(), or sorted().
# ✅ When you don’t want to define a full function with def.

"""

📌 map(), filter(), reduce(), and sorted() in Python

These higher-order functions allow you to process lists efficiently using lambda functions or normal functions.

1️⃣ map() – Apply a Function to Each Element

map(function, iterable) applies a function to every item in an iterable (e.g., list, tuple).

✅ Example: Squaring Each Number

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16]

🔹 How it works?
	•	lambda x: x ** 2 is applied to each element.
	•	Returns a new list with the transformed values.

2️⃣ filter() – Select Elements That Match a Condition

filter(function, iterable) keeps only the elements where the function returns True.

✅ Example: Keeping Only Even Numbers

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]

🔹 How it works?
	•	lambda x: x % 2 == 0 keeps only even numbers.
	•	Returns a filtered list.

3️⃣ reduce() – Combine Elements Into a Single Value

reduce(function, iterable) reduces a list to a single value by applying the function cumulatively.

📌 reduce() is inside the functools module.

✅ Example: Sum of All Elements

from functools import reduce

nums = [1, 2, 3, 4]
sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)  # Output: 10

🔹 How it works?
	•	First, adds 1 + 2 = 3
	•	Then, adds 3 + 3 = 6
	•	Then, adds 6 + 4 = 10
	•	Final result: 10

✅ Example: Finding the Maximum Number

from functools import reduce

nums = [3, 5, 2, 8, 1]
max_num = reduce(lambda x, y: x if x > y else y, nums)
print(max_num)  # Output: 8

🔹 How it works?
	•	Compares each pair, keeping the larger number.

4️⃣ sorted() – Sort Elements Based on a Key

sorted(iterable, key=function, reverse=False) sorts a list based on a function.

✅ Example: Sorting Numbers (Ascending)

nums = [5, 2, 8, 1, 9]
sorted_nums = sorted(nums)
print(sorted_nums)  # Output: [1, 2, 5, 8, 9]

✅ Example: Sorting Words by Length

words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['kiwi', 'apple', 'cherry', 'banana']

🔹 How it works?
	•	lambda x: len(x) sorts words based on their length.

✅ Example: Sorting in Reverse Order

nums = [5, 2, 8, 1, 9]
sorted_desc = sorted(nums, reverse=True)
print(sorted_desc)  # Output: [9, 8, 5, 2, 1]

🚀 Summary: When to Use Each?

Function	Purpose	Returns
map()	Transform each item	List of transformed values
filter()	Keep only items that meet a condition	Filtered list
reduce()	Reduce a list to a single value	A single result
sorted()	Sort elements	Sorted list

Would you like more examples or a specific use case? 😊

"""


li = [1,2,3,4,5,6,7,8,9,10]

var1=list(map(lambda x:x**2,li))

print(var1)

var2 = list(filter(lambda x:x**x <=256,li))

print(var2)
from functools import reduce
var3 = reduce(lambda x,y:(x*y)//2,li)
print(var3)

print(sorted(li,reverse=True))
