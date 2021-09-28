from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./data/chromedriver')

url = "https://www.amazon.com/"
driver.get(url)

# 검색창 요소
sel_input = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
# 검새버튼 요소
sel_button = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
# 검색 작업 시작
word = 'computer'
sel_input.clear()
sel_input.send_keys(word)
sel_button.click()

# 브라우져 html 소스코드 파싱
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
# soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
print(soup.title)

current_url = driver.current_url

tmp = soup.find_all('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')[0]
print(tmp)
print(tmp.span.text)
print()
print(tmp.a.attrs['href'])


current_url + tmp.a.attrs['href']


#### 아마존 리뷰 가져오기

driver =webdriver.Chrome('./data/chromedriver')
url = 'https://www.amazon.com/HP-24-inch-Computer-Processor-24-dd0010/dp/B0849GZCQR/ref=sr_1_2?dchild=1&keywords=computer&qid=1631254252&sr=8-2'
driver.get(url)

# 첫 번째 리뷰 버튼 : //*[@id="acrCustomerReviewText"]
first_review = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
first_review.click()

# 두 번째 리뷰 버튼 선택 :  //*[@id="reviews-medley-footer"]/div[2]/a
second_review = driver.find_element_by_xpath(' //*[@id="reviews-medley-footer"]/div[2]/a')
second_review.click()

# 페이지 정보를 넘겨 받고, 하나의 리뷰 가져오기
page =driver.page_source # 하나의 페이지 정보 전달
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

# 하나의 정보 확인
txt = soup.find_all('span',class_= 'a-size-base review-text review-text-content')
print(txt[0].text.strip())

all_r = soup.find_all('span',class_='a-size-base review-text review-text-content')

all_review = []
for one in all_r:
    tmp = one.text
    review = tmp.strip()
    all_review.append(review)

all_review
