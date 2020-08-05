# Week 7

Plotting and Matplotlib

Source: [matplotlib Tutorial documentation](https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)

To make a simple line graph in matplotlib:

```python
plt.plot([1, 2, 3, 4])
```


If you provide a single list or array to plot, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you. Since python ranges start with 0, the default x vector has the same length as y but starts with 0. Hence the x data are [0, 1, 2, 3].

If you want to plot x and y, you can add them as separate lists or arrays:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
```

What is in the output? Ex: [<matplotlib.lines.Line2D at 0x1160c7c10>]
This is an object that Matplotlib has created. If you just see this output when graphing, simply add plt.show() to a new line

Or in Jupyter notebook when importing matplotlib, use `%matplotlib inline`

There is an optional third argument after the x and y for color and line type. Default is `'b-'`, which is a solid blue line.

If we want to change it to green dots, we can update the code to:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'go')
```

Note that this uses lists, but you'd more likely use Pandas or Numpy. Actually if you put in a list, matplotlib will convert
it to a numpy array before plotting.

### Using subplots

`subplots()` is a utility wrapper function that allows you to organize the layout
of your figure. If you want to use legends or make multiple plots, or make layout
changes, you will need to use subplots

```python
x = range(300)
y = np.random.rand(300)
fig, ax = plt.subplots()
ax.plot(x, y)
```

To show a legend:

```python
fig, ax = plt.subplots()
ax.plot(x, y, label='Random Numbers')
ax.legend()
```

You can update the x, y axis labels and a title:

```python
fig, ax = plt.subplots()
ax.plot(x, y, label='Random Numbers')
ax.legend()
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Chart title')
```

### Plotting with Pandas

Pandas uses matplotlib (by default) to make plots of series or DataFrames.
[Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)

To test this out:

```python
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
df.head()
```

```python
df.plot()
```

You can also select which column to graph on:

```python
df['sepal_length'].plot()
```