# Week 8

## Web Scraping

Steps to Webscraping

1. Inspect the website. Go to the page adn see how the webpage is organized. Visually, locate the information you need.
2. If you are scraping multiple webpages, look at the URL. What information is encoded in the base URL and query parameters?
3. Inspect the site using developer tools. Look at the source code. Where in the HTML structure is the content located?

The more you explore the webpage, the easier building the scraper will be!

Note: Not all websites are scrapeable, or at least easily scrapeable.

## Requests

The requests library allows you to send HTTP/1.1 requests using Python to
access headers, form data, text, and other parameters.

```python
import requests
r = requests.get('https://www.uchicago.edu/about/')
```

Now investigate what `r` is:

```python
type(r)
```

We see that it is a Response object. There is a lot to do with the Response.
The first thing we would want to do is check the status code, to make sure
we are successful in accessing the page.

```python
r.status_code
```

If successful, `r.status_code` will be 200. If we change the URL so it is broken,
we would still get a Response object, but the status code will be 404.

To see the html code, we can look at `r.text`.

Now that we have the HTML string, how do we make sense of it?

## Crash Course in HTML

Before we dive into BeautifulSoup, a crash course in HTML.

The basis of HTML are tags and attributes.

Tags are used to mark the start of an HTML element and enclosed in angle brackets. Most tags need to be opened and closed.

HTML attributes contain additional pieces of information. For example, in an image, src and alt are attributes of the img tag

Tags are nested, and tags need to be closed in the order they were opened.


## BeautifulSoup

First, import the library's BeautifulSoup object:

```python
from bs4 import BeautifulSoup
```

Then create a BeautifulSoup Object:

```python
soup = BeautifulSoup(r.text, 'lxml')
```

For speed, lxml is recommended. There are ~5 parsers to choose from in the documentation.

Once you have the soup created, you can find all items with a specific tag:

```python
divs = soup.find_all('div')
divs
```

And index into it like a list:

```python
divs[0]
```

You can also index into the tags (finds the first instance)

```python
soup.find_all('div')[0].div.div.ul
```