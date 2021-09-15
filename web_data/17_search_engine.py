from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://news.naver.com/'
driver = webdriver.Chrome('./data/chromedriver')
driver.get(url)

# 검색 입력창 xpath : //*[@id="lnb.searchForm"]/fieldset/input[1]
# 검색 버튼 xpath : //*[@id="lnb.searchForm"]/fieldset/button

a = driver.find_element_by_xpath('//*[@id="lnb.searchForm"]/fieldset/input[1]')
b = driver.find_element_by_xpath('//*[@id="lnb.searchForm"]/fieldset/button')

a.send_keys("미세먼지")
b.click()

page = driver.page_source
soup = BeautifulSoup(page,'lxml')
soup.title

all_news = soup.find("li",class_='bx')

