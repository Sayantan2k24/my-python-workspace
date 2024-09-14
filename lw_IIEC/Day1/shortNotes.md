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

