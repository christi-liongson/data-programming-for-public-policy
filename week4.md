# Week 4
Inheritance | PEP8

## Inheritance

Source: https://www.w3schools.com/python/python_inheritance.asp

Here we can create a parent class:
```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def print_name(self):
        print(self.first_name, self.last_name)
```

Creating a person, we can use `person = Person('Regina', 'King')`. And print
their name using `person.print_name()`

Now to create a child class:
```python
class Student(Person):
    pass
```

Now, if we create a new student, `student = Student('Billy', 'Porter')`, we can
use the same methods within the Person class because the Student class inherits
from the Person class. `student.print_name()`

We can also create a child class with functions specific to the student:
```python
class Student(Person):
    def __init__(self, first_name, last_name, enrolled_class):
        self.first_name = first_name
        self.last_name = last_name
        self.enrolled_class = enrolled_class
    def print_enrollment(self):
        print("{} is enrolled in {}".format(self.first_name, self.enrolled_class))
```

If we recreate the student `student = Student('Billy', 'Porter', 'Dance')`, we can
call `student.print_enrollment()`. We can also still call the person method `student.print_name()`. 
However, with the Person `person = Person('Regina', 'King')`,
running `person.print_enrollment()` will result in an error.

## Generators

Helpful if you want to return back to a sequence. For instance, if you have a
sequence of odd numbers and you pause partway through and then return to it,
you will have to recreate the entire sequence in memory. This can be expensive.
Generator implementation for this use is memory-friendly since it remembers where
it is in the sequence.

Also good for 'infinite' streams of data.

```python
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
```

You can work through the function now by assigning the function to a variable,
`a = my_gen()` and then using `next(a)` to work through the function.

## Assertions

```python
assert Expression, Arguments
```

Python evalutes the assertion. If true, Python continues with the script. If
false, Python will raise the assertion error.

```python
def spell_string(word):
    assert isinstance(word, str), "Not a string!"
    return [letter for letter in word]
```

(Have someone explain what this function does)

What happens if I call `spell_string("Hello")`?  What about `spell_string(8)`?

## Try Except

```python
try:
    print(x)
except:
    print('An exception occurred')
```

If x is undefined, what should output?

You can also see the error calling it in the except:

```python
try:
    print(x)
except Exception as e:
    print(e)
    print('An exception occurred')
```

In the above example, the except captures all errors, not just a specific error.

You can also specify the type of error in the except:

```python
try:
    print(x)
except NameError:
    print('This is a NameError')
except Exception as e:
    print(e)
    print('An exception occurred')
```

Since `print(x)` results in a NameError, the interpreter will locate the NameError
Exception and do that action. You can add additional exception blocks for every
error type.

```python
try:
    print(x)
except NameError:
    print('This is a NameError')
except Exception as e:
    print(e)
    print('An exception occurred')
finally:
    print('This action is done')
```

If i run this, what should return? If I run this after setting `x=5`, what
returns?

Adding finally at the end of the block will execute the expressions in the
`finally` block regardless of whether or not there has been a try or except.
