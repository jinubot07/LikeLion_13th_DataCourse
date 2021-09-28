from urllib.request import urlopen
from bs4 import BeautifulSoup

# 옥션 가방
url = "http://browse.auction.co.kr/search?keyword=%EA%B0%80%EB%B0%A9&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%EA%B0%80%EB%B0%A9&acode=SRP_SU_0100&arraycategory=&encKeyword=%EA%B0%80%EB%B0%A9"
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')
print(soup.title)

bag_tag = soup.find('span','text--title')
print(bag_tag)

# 롯데ON 가바
url = "https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EA%B0%80%EB%B0%A9&mallId=1"
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')
print(soup.title)

bag_lotte = soup.find('div','srchProductUnitTitle')
print(bag_lotte)

# 스타일 난다
url = "https://stylenanda.com/product/search.html?sort_method=6&x=0&y=0&keyword=%EA%B0%80%EB%B0%A9"
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')
print(soup.title)

bag_style = soup.find('div','name').find_all('span',style='font-size:12px;color:#000000;')[1].text
print(bag_style)


from selenium import webdriver
driver = webdriver.Chrome('./data/chromedriver')
