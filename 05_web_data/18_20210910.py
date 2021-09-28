from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.amazon.com/'
driver = webdriver.Chrome('./data/chromedriver')
driver.get(url)

searchlot = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbtn = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')

word = 'computer'
searchlot.clear()
searchlot.send_keys(word)

searchbtn.click()

page = driver.page_source  # html 소스코드 가져오기
soup = BeautifulSoup(page,'html.parser')
print(soup.title)

tmp = soup.find_all('h2','a-size-mini a-spacing-none a-color-base s-line-clamp-2')[0]
print(tmp.a.attrs['href']) #print(tmp.a['href'])
# current_url = current_url + tmp.a.attrs['href']