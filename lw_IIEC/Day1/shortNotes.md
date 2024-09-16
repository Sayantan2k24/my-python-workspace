# Variables

It is like a container -- holds something for us, whatever you can fill --> data

What type of data?
That is data types

## Numbers

```
>>> bottle = 5
>>> print(bottle)
5
>>> type(bottle)
<class 'int'>
```

## String

```
>>> bottle = vimal
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'vimal' is not defined
>>>
```

Tell bottle that the value is actually a string.

```
>>> bottle = "vimal"
>>> print(bottle)
vimal
>>> type(bottle)
<class 'str'>
```

## Type Inference

whenver you create a variable , you have to tell what kind of values you want to fill

Type x = data

There is a limitation --> the bottle will only hold that kind of value

But in python -- it auto detect the data type -- you don't have to tell explictly.

x = 5

python is not strongly typed.

Users don't have to tell the data type before filling the variable with data.

```
>>> x = 5

>>> x = "vimal"
```

Think of it as if they automatically do type Conversion behind the scene. (Data Type Casting)

Check with type() function

```
>>> x  = 5
>>> type(x)
<class 'int'>
>>> x = "vimal"
>>> type(x)
<class 'str'>
>>> x = 6.7
>>> type(x)
<class 'float'>
>>>
```

Python will automatically find for you what is the data type and change the type of the variable when user is assigning the new value to the same variable.
--> Type Inference

### Boolean type

True is predefined Boolean value, with cap T at start.
False is predefined Boolean type too.

```
x = True
type(x)

>>> x = True
>>> type(x)
<class 'bool'>
>>>
>>> x = true
type(x)Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>>
>>> x = "True"
>>> type(x)
<class 'str'>
>>>
```

These are the Primitive Data type

# x holds the mem addr not the data directly

At runtime,
`x = 5`

means x holds a reference to the memory address where the value 5 is stored in RAM.

x refers to the memory location of the data, not the data itself directly.

# REPL

REPL stands for Read-Eval-Print Loop. It's an interactive environment that:

Reads user input (code).
Evaluates the input (executes it).
Prints the result.
Loops back to accept new input.

Python's REPL can be accessed by simply running python in the terminal. It allows you to test code quickly and see results in real-time.

```
>>> x = "vimal"
>>> x
'vimal'
>>> print(x)
vimal
>>>
```

## Use case of \_ in python

### temp variable `_`

In python, whatever output you print last , thhe output also they store in some temp variable name `_` (undescore)
Use case --> whatever last output comeup -- we may not know what is the value but `_` keeps on tracking and we can do soemthign like encryption or add other things on it etc etc.

```
>>> x = 5+7
>>> x
12
>>> _
12
>>> 6*8
48
>>> _
48
>>> _ + 2
50
>>>
```

```
>>> 6*6*6
216
>>> 6**2 # power
36
>>>
```

```
>>> db = [1,2,3,4]
>>> j,k,l = db
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 3)
>>>
>>> _,j,k,l = db
>>> j,k,l
(2, 3, 4)
>>> _
1
```

In Python, _ is often used as a throwaway variable to ignore values you don't need.
In the above example, _ is used to unpack and discard the first element of the list db while assigning the remaining elements to j, k, and l.

This practice signals that \_ is not important for further operations.

It saves space by avoiding the creation of extra variables for values not needed in further operations.
Using \_ helps prevent errors during unpacking when some values are irrelevant.

## Loop

Repeat block of code.

1. Iteration
   a. for
   b. while
   c. do while

2. Recursion --> Using function

## Indentation

## bool(expression)

## print() and escape sequence

```
>>> s =  "this is Linux World"
>>> print(s)
this is Linux World
>>>
>>> s =  "this is \nLinux World"
>>> print(s)
this is
Linux World
>>>
```

print() behind the scene tells that after I print some string I will always run one escape sequence that is `\n`

`\n` is for new line

### where it is written

```python
print("string", end='\n')
print("string")
# Behind the scene inside the print() there is one keyword `end`.
# after it prints something, it will always run the new line at the end
```

To tell print() that I don't want you to run a new line at the end , in fact I want you to do nothing after you print something. Just use `end=''`

```python
print("string", end='')
```

We can try any pattern printing too after print the string

```python
>>> s =  "this is Linux World"
>>> print(s, end='...............')
this is Linux World...............>>>

```

Even before running the new line we can print some pattern

```python
>>> s =  "this is Linux World"
>>> print(s, end='...............\n')
this is Linux World...............
>>>
```

Another escape sequence is `\t` for tab or giving some extra spaces

```python
>>> s =  "this is Linux \t World"
>>> print(s)
this is Linux    World
>>>
>>> s =  "this is Linux World"
>>> print(s, end='........\t........\t.........')
this is Linux World........     ........        .........>>> print(s, end='........\t........\t.........\n')
this is Linux World........     ........        .........
>>>
```


# Run os related commands using os module and subprocess
```python
>>> import subprocess
>>> import os
>>> # Pass the command as a list of arguments
>>> firefox_path = subprocess.run(["which", "firefox"], capture_output=True, text=True)
>>> # firefox_path = subprocess.run("which firefox", shell=True, capture_output=True, text=True)
>>> 
>>> firefox_path = subprocess.run("which firefox", shell=True, capture_output=True, text=True)
>>> os.system(firefox_path.stdout.strip())
Gtk-Message: 11:29:02.083: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
```

