---
layout: default
---

## the big picture

In this post we will explain how to do web scraping with beautiful soup and selenium.

In this post we will explain how to do web scraping with beautiful soup and selenium.

![](https://cdn-images-1.medium.com/max/800/1*8B-fOXenzIDWg-CXTTwK9g.png)

### selenium web driver

Any data scraping task start with a url to page which contain data need to be scraped. Selenium web driver will take input url and produce content in html.

Some people will ask, why we need selenium ? because we could simply use package like `requests` to download html from input url.

First reason is now a day, a lot of modern web page is dynamic meain contain javascript. Actual html content only be created when javascript code running through browser.

For example if you run following code, console will print out only js code due to `requests` could not handle js

```python
import  requests

url = '[https://www.youtube.com/'](https://www.youtube.com/%27)  
response = requests.get(url)  
print(response.content)
```

Second reason to use selenium is some time in order to go to page contain needed information, we need to do some action on browser like login, click to access some where.

### beautiful soup

After html content is render with selenium web driver, we need `beautiful soup` to parse this html to pull out target data.

Before use beautiful soup we need to know where our data located inside html structure. Normally we will use chrome developer tool to do this. Then finally we could pull out texts or links from html.