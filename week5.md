# Week 4

Intro to Data

## Import

Examples from: [Real Python](https://realpython.com/python-import/#basic-python-import)

```python
import math
math.pi
```

Usually, imports are made at the top of your code, before any additional operations.

You can import specific variables or functions from the module using `from`. This improts the function into the global namespace.

```python
from math import pi
pi
```

Here, `math` acts as a namespace that keeps all the attributes of the modules together.

You can see the contents of the namespace with `dir()`

```python
dir() # Shows everything that's in the global namespace
dir(math) # Displays contents of the math namespace
```

You can also rename modules or attributes as they are imported.

```python
import math as m
m.pi
```

```python
from math import pi as PI
PI
```

