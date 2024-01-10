# Python Data Structures - List and Tuples

## Overview

This repository provides an introduction to two fundamental data structures in Python: Lists and Tuples. These structures allow you to organize and manipulate collections of data in your Python programs.

## Table of Contents

1. [Lists](#lists)
   - [Introduction](#introduction)
   - [Creating Lists](#creating-lists)
   - [Accessing Elements](#accessing-elements)
   - [Modifying Lists](#modifying-lists)
   - [Common List Operations](#common-list-operations)
   - [List Comprehensions](#list-comprehensions)

2. [Tuples](#tuples)
   - [Introduction](#introduction)
   - [Creating Tuples](#creating-tuples)
   - [Accessing Elements](#accessing-elements)
   - [Immutable Nature](#immutable-nature)
   - [Tuple Packing and Unpacking](#tuple-packing-and-unpacking)
   - [Common Tuple Operations](#common-tuple-operations)

3. [Choosing Between Lists and Tuples](#choosing-between-lists-and-tuples)
4. [Best Practices](#best-practices)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

## Lists

### Introduction

A list is a versatile and dynamic data structure in Python that allows you to store and manipulate a collection of items. Lists are mutable, meaning you can modify their content by adding, removing, or modifying elements.

### Creating Lists

```python
# Creating a list
my_list = [1, 2, 3, 'apple', 'banana', True]
```

### Accessing Elements

```python
# Accessing elements
first_element = my_list[0]
last_element = my_list[-1]
```

### Modifying Lists

```python
# Modifying elements
my_list[0] = 99
my_list.append('orange')
my_list.extend([4, 5, 6])
```

### Common List Operations

```python
# Common operations
length = len(my_list)
sorted_list = sorted(my_list)
reversed_list = reversed(my_list)
```

### List Comprehensions

```python
# List comprehensions
squares = [x**2 for x in range(1, 6)]
```

## Tuples

### Introduction

A tuple is a collection similar to a list, but with the key difference that it is immutable. Once a tuple is created, you cannot modify its content. Tuples are commonly used when the data should remain constant throughout the program.

### Creating Tuples

```python
# Creating a tuple
my_tuple = (1, 2, 3, 'apple', 'banana', True)
```

### Accessing Elements

```python
# Accessing elements
first_element = my_tuple[0]
last_element = my_tuple[-1]
```

### Immutable Nature

```python
# Trying to modify a tuple will result in an error
# my_tuple[0] = 99  # Uncommenting this line will raise a TypeError
```

### Tuple Packing and Unpacking

```python
# Tuple packing and unpacking
coordinates = (3, 4)
x, y = coordinates
```

### Common Tuple Operations

```python
# Common operations
length = len(my_tuple)
concatenated_tuple = my_tuple + (4, 5, 6)
```

## Choosing Between Lists and Tuples

- Use lists when you need a collection that can be modified.
- Use tuples when the data should remain constant (immutable).

## Best Practices

- Choose lists for dynamic collections and tuples for static collections.
- Use meaningful variable names to enhance code readability.
- Leverage list comprehensions for concise and expressive code.

## Examples

Explore the `examples/` directory for practical demonstrations of working with lists and tuples in Python.
