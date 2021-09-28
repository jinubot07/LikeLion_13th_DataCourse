from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://pythonstart.github.io/web/'
start = time.time()
driver = webdriver.Chrome('./data/chromedriver')
driver.get(url)

a_tag = driver.find_element_by_id('rank')
print(a_tag.text)
print()


a_tag = driver.find_elements_by_name('link_get')
print(a_tag)
print()

for one in a_tag:
    print(one.text)
print('==================')


content = driver.find_elements_by_css_selector('body ul a #rank')
print(content)
for one in content:
    print(one.text)
print('==================')

content = driver.find_elements_by_tag_name('ul a')
print(content)
for one in content:
    print(one.text)
print('==================')

content = driver.find_elements_by_link_text('01. 제목가져오기(title)')
print(content)
for one in content:
    print(one.text)
print('==================')