# Variables

it is like a container -- holds something for us, whatever you can fill --> data

What type of data ?
that is data types

## Numebers

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

### tell bottle that the value is actually a string

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

