---
layout: default
---

#### The Big Picture

![](https://cdn-images-1.medium.com/max/800/1*8B-fOXenzIDWg-CXTTwK9g.png)

In this chapter we will take overview on steps need to be done with every web scraping task. Actually this is a really simple process.

**Step 1** : Web scraping task always start with a web page and information we want to scrape. So the first step always about understand web page and find out where information we care about located. Knowledge from this step will be used in final step to actually scrape data.

**Step 2** : Actual data is located inside HTML page, so at this step we need to download html page. We will use `Selenium Web Driver` for downloading web page.

**Step 3** : After have html content, we use `Beautiful Soup` to parse it. After parse we will easily search for wanted information

**Step 4** : Final step is about scrape data and store to file for a database. In this book we will simply store data to file.

#### Selenium Web Driver

We use `selenium web driver` to control browser. Input is a `URL` and output is web page HTML content.

```python
import  requests

url = 'https://www.youtube.com'
response = requests.get(url)
print(response.content)
```



Second reason to use selenium is some time in order to go to page contain needed information, we need to do some action on browser like login, click to access some where.

#### Beautiful Soup

After html content is render with selenium web driver, we need `beautiful soup` to parse this html to pull out target data.

Before use beautiful soup we need to know where our data located inside html structure. Normally we will use chrome developer tool to do this. Then finally we could pull out texts or links from html.