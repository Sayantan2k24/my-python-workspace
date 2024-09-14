# Data Structure

A way to organize and store multiple data elements, making CRUD (Create, Read, Update, Delete) operations easier.

## List

List is a data strcuture in python -- often known as array in some other Programming langs.

A List in Python is used to store multiple values in a single variable, typically when managing similar types of data.

```
>>> db
['vimal', 'pop', 'eric']
>>> type(db)
<class 'list'>
>>> db[0]
'vimal'
>>> for i in db:
...   print(i)
...
vimal
pop
eric
```

It is better way of management not to store different types of data in same list together.

```
>>> db = [1,"vimal", "hello123@gmail.com"]
>>> db
[1, 'vimal', 'hello123@gmail.com']
```

### **Indexing in Python**

In Python, **indexing** for sequences (like lists) starts from **0**, meaning the first element is at index `0`, the second at index `1`, and so on.

### **List Example:**

```python
fruits = ["apple", "banana", "cherry"]

# Accessing elements by index
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry
```

- **`fruits[0]`** refers to the first element, `"apple"`.

### **Slicing in Python**

**Slicing** is a way to extract a portion of a sequence (like a list or string) using a range of indices.

### **Syntax:**

```python
list[start:end]
```

- **start**: Starting index (inclusive).
- **end**: Ending index (exclusive).

### **List Slicing Example:**

```python
numbers = [10, 20, 30, 40, 50]

# Slice from index 1 to 3 (20, 30)
print(numbers[1:3])  # Output: [20, 30]
```

Same with string types also

```
>>> db = ["vimal", "pop", "eric", "krish", "amit"]
>>> db
['vimal', 'pop', 'eric', 'krish', 'amit']
>>> db[:]
['vimal', 'pop', 'eric', 'krish', 'amit']
['pop', 'eric', 'krish']
>>> db[:4]
['vimal', 'pop', 'eric', 'krish']
>>> db[0:3]
['vimal', 'pop', 'eric']
>>> db[:3]
['vimal', 'pop', 'eric']
>>> db[2:]
['eric', 'krish', 'amit']
>>>
```

The ending point in the range will be excluded, so db[0,3] it will print till index 2 and will not print the element at index 3

```
db = ["vimal", "pop", "eric", "krish", "amit"]

db[:]        # Outputs entire list: ['vimal', 'pop', 'eric', 'krish', 'amit']

db[:4]       # Slices from the start to index 3 (index 4 excluded): ['vimal', 'pop', 'eric', 'krish']

db[0:3]      # Slices from index 0 to 2 (index 3 excluded): ['vimal', 'pop', 'eric']

db[:3]       # Slices from start to index 2 (same as above): ['vimal', 'pop', 'eric']

db[2:]       # Slices from index 2 to the end: ['eric', 'krish', 'amit']
```
