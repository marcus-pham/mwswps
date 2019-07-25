---
layout: default
---

## The Big Picture

In this post we will explain how to do web scraping with beautiful soup and selenium.

![](https://cdn-images-1.medium.com/max/800/1*8B-fOXenzIDWg-CXTTwK9g.png)

### Selenium Web Driver

Any data scraping task start with a URL to page which contain data need to be scraped. Selenium web driver will take input URL and produce content in html.

Some people will ask, why we need selenium ? because we could simply use package like `requests` to download html from input URL.

First reason is now a day, a lot of modern web page is dynamic mean contain JavaScript. Actual html content only be created when JavaScript code running through browser.

For example if you run following code, console will print out only JavaScript code due to `requests` could not handle js

```python
import  requests

url = 'https://www.youtube.com'
response = requests.get(url)
print(response.content)
```



Second reason to use selenium is some time in order to go to page contain needed information, we need to do some action on browser like login, click to access some where.

### Beautiful Soup

After html content is render with selenium web driver, we need `beautiful soup` to parse this html to pull out target data.

Before use beautiful soup we need to know where our data located inside html structure. Normally we will use chrome developer tool to do this. Then finally we could pull out texts or links from html.