# Week 3
Functions | Global and Local Variables

## Functions

```
def calc_hypotenuse(a, b):
    '''
    Calculates hypotenuse of a right triangle

    Inputs:
        a (numeric): Length of side a
        b (numeric): Length of side b
    Returns: Float
    '''

    c = (a**2 + b**2) ** (1/2)
    return c
```

Parts of a function:
* `def` - keyword, followed by the function name. The start of the function block.
* parameters - values inside a function.
* docstring: Statement about the function. As a best practice it shouold include
    the high-level description of the function, the inputs, and what the function
    returns
* codeblock
* return expression: signifies the end of a function, can also pass an expression
    back to the caller.


If `calc_hypotenuse(3, 4)` is 5, then the value of `x = calc_hypotenuse(3, 4)`
is also 5.0.

What should `a` output?

### Required arguments, keyword arguments, and default arguments
The first argument in the slide is a required argument. For required arguments,
the order matters.

```
def ret_info(name, location, weather):
    return "Name: {}, Location: {}, Weather: {}".format(name, location, weather)
```

`ret_info("Abby", "Hyde Park", "Sunny")`

`ret_info(location="Hyde Park", weather="Sunny", name="Abby")`

What would be the return of `ret_info()`?

```
def ret_info(name="Abby", location="Hyde Park", weather="Sunny"):
    return "Name: {}, Location: {}, Weather: {}".format(name, location, weather)
```

What would return with `ret_info()`?

You can override default arguments:
`ret_info(weather="Rainy")`

Positional arguments must come before keyword arguments.

### Lambda functions
Example:

```
x = 3
lambda x: x ** 2
```

## Local and Global Variables

```
x = "Global Variable"

def my_func():
    print(x, "is inside the function")

my_func()
print(x, "is outside the function")
```

What if we want to change the global variable inside the function?

```
def my_func():
    x = x + ' is changed inside this function'
    print(x)
```

What would be the output of `my_func()`?

Local Variables:
```
def my_func():
    y = "Local Variable"
    print(y)
```

What is the expected output of `my_func()`? What is the expected output of
`y`?

Globals can be very helpful when you have code that would rely on the same value!

# Classes and Methods

```
class MyClass:
    class_attribute = 'class attribute!'

    def __init__(self):
        self.attribute_a = 'attribute a'
        self.number_one = 1
```

I can create a new instance of the class by calling `my_instance = MyClass()`.
And access the attributes through dot notation: `my_instance.attribute_a`
and `my_instance.number_one`.

As seen in the lecture, putting a parentheses after MyClass is important in
the definition when it comes to inheritance. If there is no inheritance, you do
not need parentheses.

Note how the naming convention for classes and variables are different! Functions
and variables in Python use snakecase, and classes use camel case.

```
class Vehicle:
    def __init__(self, v_type, wheels, motor):
        self.v_type = v_type
        self.wheels = wheels
        self.motor = motor
    def drive(self):
        return "I am driving my {} with {} wheels.".format(self.v_type, self.wheels)
```

Some examples of this vehicle class:

```
my_bike = Vehicle('bike', 2, False)
my_bike.drive()
```

```
my_car = Vehicle('car', 4, True)
my_car.drive()
```

What is the output of `type(my_bike)`?