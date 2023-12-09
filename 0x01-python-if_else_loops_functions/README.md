# Python Basics: Conditionals and Loops

## Introduction

This README provides a brief overview of basic control flow structures in Python, including `if` statements, `else` statements, loops (`for` and `while`), and functions.

## 1. `if` Statements

In Python, `if` statements are used for conditional execution. They allow you to execute a block of code if a certain condition is met.

```python
# Example of an if statement
x = 10
if x > 5:
	    print("x is greater than 5")
		```

## 2. `else` Statements

`else` statements can be combined with `if` statements to specify a block of code to be executed when the condition in the `if` statement is not met.

```python
# Example of an if-else statement
y = 3
if y > 5:
	    print("y is greater than 5")
		else:
			    print("y is not greater than 5")
				```

## 3. Loops

### 3.1 `for` Loop

The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, or string).

```python
# Example of a for loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
	    print(num)
		```

### 3.2 `while` Loop

The `while` loop is used to repeatedly execute a block of code as long as the specified condition is true.

```python
# Example of a while loop
count = 0
while count < 5:
	    print(count)
		    count += 1
			```

## 4. Functions

Functions in Python allow you to encapsulate and reuse a block of code. They are defined using the `def` keyword.

```python
# Example of a function
def greet(name):
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")
```

---

Feel free to experiment with these examples and explore more advanced features of conditionals, loops, and functions in Python. The best way to learn is by writing your own code and practicing these concepts in different scenarios. Happy coding!
