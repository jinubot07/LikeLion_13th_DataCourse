from urllib.request import urlopen
from bs4 import BeautifulSoup

# url :
# tag , id, class:
# 다우산업지수, 나스닥 종합, S&P
# 다우산업 지수 : 태그span 클래스명point_status

url = "https://finance.naver.com/sise/"
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')
print(soup.title)

#dow = soup.find("span","point_status")
#print("다우산업지수:",dow.text)

data = soup.find("ul", class_="lst_pop")
data_all = data.find_all("a")
value_all = data.find_all("span", "dn")

for one in data_all:
    print(one.text)
for one in value_all:
    print(one.text)