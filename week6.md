# Week 6

Pandas

## Merging

Merge joins two dataframes.

Different types of merges:

* left: use only keys from the left frame
* right: use only keys from the right frame
* outer: use union of keys of both frames
* inner (default): use intersection of keys of both frames

This can be specified through the 'on' argument.
Using these two dataframes, how would I merge
them together?

```python
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
```

I would use:

```python
pd.merge(left, right, on='key')
```

What if the columns are different? (Rename key in left to key1 and key in right to key2)

```python
pd.merge(left, right, left_on='key1', right_on='key2')
```

### Types of merges

Go back and change 'K3' to 'K4' in the left dataframe. Remove the renaming of key1 and key2.

Now say I use `pd.merge(left, right, on='key', how='left')`. What values
should I expect to see in the resulting dataframe from the left? What values
should I expect to see in the resulting dataframe from the right?

We would see K4 from the left dataframe, but since there is no K4 in the right
dataframe, it would be NaN values for C and D.  What happened to K3? Since
K3 is in the right dataframe but not in the left dataframe, it is not displayed
in the dataframe.

What would I expect to see from `pd.merge(left, right, on='key', how='right')`?
Similar, we would see only values K0 - K3, but no K4. K3's A and B would be blank.

`pd.merge(left, right, how='outer')`?
Would have everthing

`pd.merge(left, right, how='inner')`?
Would only have shared keys -- in this case, K0- K2

Other ways you can merge:

`left.merge(right, on='key')` -- this is similar to `pd.merge(left, right, on='key')`

Note: left.merge result is still the same original dataframe. This does not
modify the original dataframe.

### Merging with indexes

`left.merge(right, left_index=True, right_index=True)`
Merges based on index

## Reshaping

### Wide to Long

Using this dataframe:

```python
data_url = "https://goo.gl/ioc2Td"
gapminder = pd.read_csv(data_url)
lifeExp = gapminder.loc[:, gapminder.columns.str.contains('^life|^c')]
```

How would we make this from a wide to a long dataframe, with countries and years
as the index?

```python
pd.wide_to_long(life_exp, stubnames=, i=, j=, sep='_') #what do we put in stubnames, i, and j?
```

default for sep is ''.

One solution:
```python
pd.wide_to_long(life_exp, stubnames='lifeExp', i='country', j='year', sep='_')
```

### Unstack

Unstacking would make our long dataset back into wide

```python
long_df = pd.wide_to_long(life_exp, stubnames='lifeExp', i='country', j='year', sep='_')
long_df['lifeExp'].unstack()
```

How could we use pivot to make the same dataframe for `long_df.reset_index()`?

```python
long_df.reset_index().pivot(index=, columns=, values=)
```

One answer:

```python
long_df.reset_index().pivot(index='country', columns='year', values='lifeExp')
```


## Groupby

Say I want to use life_exp. What would I use if I want to group by continent?

```python
life_exp.groupby('continent')
```

This just creates a group object, so I can apply functions onto this, such as:

```python
life_exp.groupby('continent').sum()
```

You can also use this with python's lambda and Panda's apply.

```python
continent_groups = long_df.groupby('continent')
long_df.groupby('continent').apply(lambda x: len(x))
long_df.groupby('continent').apply(len)
```

the above are the same!

Some changes