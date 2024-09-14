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

### **Functionalities We Can Apply on a List in Python:**

Every data structure comes with its own built-in functions and methods that are tailored to the type of data and the operations it needs to support.

These features are designed to make CRUD (Create, Read, Update, Delete) operations and other manipulations efficient and convenient based on the specific use case.

Use dir() function to see all the methods relevant to one Data Structure.

Use help() function to know the use of particular method

```
>>> db
['vimal', 'pop', 'eric', 'krish', 'amit']
>>>
>>> type(db)
<class 'list'>
>>>
>>> dir(db)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> help(db.index)

Help on built-in function index:

index(value, start=0, stop=9223372036854775807, /) method of builtins.list instance
    Return first index of value.

    Raises ValueError if the value is not present.


```

1. **Append Elements:**

   - Add an element to the end of the list.

   ```python
   db.append("new_item")
   ```

2. **Insert Elements:**

   - Insert an element at a specific position.

   ```python
   db.insert(1, "new_item")
   ```

3. **Extend List:**

   - Add multiple elements from another list.

   ```python
   db.extend(["item1", "item2"])
   ```

4. **Remove Elements:**

   - Remove the first occurrence of a specific value.

   ```python
   db.remove("pop")
   ```

5. **Pop Elements:**

   - Remove and return the last item (or by index).

   ```python
   db.pop()        # Removes last item
   db.pop(2)       # Removes item at index 2
   ```

6. **Clear List:**

   - Remove all elements from the list.

   ```python
   db.clear()
   ```

7. **Index:**

   - Get the index of the first occurrence of a value.

   ```python
   db.index("krish")
   ```

8. **Count Elements:**

   - Count the occurrences of a specific value.

   ```python
   db.count("vimal")
   ```

9. **Sort List:**

   - Sort the list in ascending (default) or descending order.

   ```python
   db.sort()          # Ascending order
   db.sort(reverse=True)  # Descending order
   ```

10. **Reverse List:**

    - Reverse the order of elements in the list.

    ```python
    db.reverse()
    ```

11. **Copy List:**

    - Create a shallow copy of the list.

    ```python
    db_copy = db.copy()
    ```

12. **Length of List:**
    - Get the number of elements in the list.
    ```python
    len(db)
    ```

### IN USE

```
>>> db = ["vimal", "pop", "eric", "krish", "amit"]
>>>
>>> db.append("tom")
>>>
>>> db.append("sarah")
>>>
>>> db.append("linux")
>>>
>>> db
['vimal', 'pop', 'eric', 'krish', 'amit', 'tom', 'sarah', 'linux']
>>>
>>> db.index("tom")
5
>>>
>>> db[5]
'tom'
>>> db[5] = "tommy"
>>>
>>> db
['vimal', 'pop', 'eric', 'krish', 'amit', 'tommy', 'sarah', 'linux']
```

Retrieving and updating like this is a 2 steps approach

```
>>> db
['vimal', 'pop', 'eric', 'krish', 'amit', 'tommy', 'sarah', 'linux']
>>> db.index("pop")
1
>>> db[1] = "poppy"
>>>
>>> db
['vimal', 'poppy', 'eric', 'krish', 'amit', 'tommy', 'sarah', 'linux']
>>>
```

Let's do it in one statement and make it shorter.

```
>>> db
['vimal', 'poppy', 'eric', 'krish', 'amit', 'tommy', 'sarah', 'linux']
>>>
>>> db[ db.index("poppy") ] = "pop"
>>> db
['vimal', 'pop', 'eric', 'krish', 'amit', 'tommy', 'sarah', 'linux']
>>>

```
