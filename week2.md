# Week 2
GitHub | Python Basics | Data Types and Logic Control

## Data Types

1. What type is 4?
2. What type is 4.0?
3. What type is 4 * 4.0?
4. `string = 'Hello'`
    a.  What is `len(string)`
5. You can concatenate strings together: `string + ' World'`
6. What type is None?
7. `l = [0, 1, 2, 3, 4]`
    To iterate through the list:
    ```
    for i in l:
        print(i)
    ```
    To add one value to the end of a list (order is preserved)
    `l.append(5)` What is the return value of `l.append(5)`?
    You can also concatenate lists:
    `l + [6, 7, 8]`
    or
    `l.extend([6, 7, 8])`
    You can reassign values by indexing into the list:
    `l[0] = 1`

8. `d = {'a': 0, 'b': 1, 'c': 2}`
    length of dictionary: `len(d)`
    keys of a dictionary must be unique:
    `d = {'a': 0, 'b': 1, 'c': 2, 'a': 3}`
    to iterate through dictionary:
    ```
    for key, val in d.items():
        print(key, val)
    ```
    ```
    for key in d.keys():
        print(key)
    ```
    ```
    for val in d.values():
        print(val)
    ```
    to get a value from the dictionary:
    `d['a']`
    to insert into dictionary:
    `d['d'] = 3`
9. `s = {0, 1, 2, 3}`
    Length of set: `len(s)`
    What do you get with `s[0]`?
    Note: orders are generally not preserved in dictionaries and sets. Be aware of this when using these data types
    Like dictionaries, sets have unique values:
    `{1, 2, 3, 4, 4, 1, 7}`
    or
    `{'h', 'e', 'l', 'l', 'o'}`
10. Tuples `t = (1, 2, 3)`
    You can get the size of the tuple `len(t)`
    Indexing into tuples:
    `t[0]`
    Iterating through tuples:
    ```
    for i in t:
        print(i)
    ```
    However, tuples are immutable:
    `t[0] = 1`


### Arithmetic Operations and Boolean Conditionals
What will be the output of this:
```
a = 5

if a == 5:
    print('a is equal to 5')
if a > 0:
    print('a is positive')
```

What will be the output of this:
```
a = 5

if a == 5:
    print('a is equal to 5')
elif a > 0:
    print('a is positive')
```
