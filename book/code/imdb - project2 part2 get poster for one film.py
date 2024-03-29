# div class_=poster --> a['href'] --> div[1] class_=pswp__zoom-wrap --> img[1]['src']

from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url = 'http://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2398042102&pf_rd_r=0PS12P50E86XYMR1RVR3&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'

options = webdriver.ChromeOptions()
options.headless  = False

chrome_driver_path = r'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path, 
						options=options)


driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

div = soup.find('div', class_ = 'poster')

a = div.find('a')

url = 'http://www.imdb.com' + a['href']
print(url)

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

all_div = soup.find_all('div', class_ = 'pswp__zoom-wrap')

all_img = all_div[1].find_all('img')

print(all_img[1]['src'])

f = open('first_image.jpg', 'wb')
f.write(requests.get(all_img[1]['src']).content)
f.close()

driver.quit()




