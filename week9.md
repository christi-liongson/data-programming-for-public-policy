# Week 9

Housekeeping: Does anyone want a lab next week? If so, anything you would like me to cover?

## Requests

There are two main types of techniques to get data from a server:

* GET: Request data from server. This is what you've done during the web scraping assignment.
* POST: Sends data to a server. You can see POST requests when submitting a form

### POST Requests for Web-Scraping

One example of how POST requests can be used for web-scraping are pages where
data can only be accessed through a form:

[https://ww2.energy.ca.gov/almanac/renewables_data/wind/index_cms.php](https://ww2.energy.ca.gov/almanac/renewables_data/wind/index_cms.php)

* Before crawling the page, we go through the three steps:

1. Inspect the website visually
2. Inspect the URL (if you are crawling multiple pages programatically)
3. Inspect the HTML code

How would you inspect this page if you were to crawl this?

### Another use for POST Requests

Another way you can apply POST requests to web-scraping are through webpages that
are behind a user login.

Using the example of this [Demo Website]('http://testing-ground.scraping.pro/login'),
let's look at the form and HTML. What fields are there? What would we see if
we enter the right credentials? What is the POST request URL?

Note: Sometimes, there are elements part of the login form that are hidden from
the browser, so it is always good to look at the HTML.

```python
USERNAME = 'admin'
PASSWORD = '12345'
url = 'http://testing-ground.scraping.pro/login?mode=login'
payload = {'usr': USERNAME,
           'pwd': PASSWORD}
```

(Payload is transmitted data. You can also name this dictionary anything you want)

Create a request.sessions() object. This allows you to stay logged in
while web scraping multiple pages.

```python
session_requests = requests.Session()
response = session_requests.post(url, data=payload)
```

Now, if we scrape the page, we can identify if it's successful

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')
soup.find("div", id='case_login')
```
