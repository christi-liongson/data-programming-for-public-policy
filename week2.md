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
    `l.append(5)`
    You can also concatenate lists:
    `l + [6, 7, 8]`
    or
    `l.extend([6, 7, 8])`
8. `d = {'a': 0, 'b': 1, 'c': 2}`
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
    to insert into dictionary:
    d['d'] = 3
9. `s = {0, 1, 2, 3}`
    What do you get with `s[0]`?