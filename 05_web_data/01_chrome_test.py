from urllib.request import urlopen
from bs4 import BeautifulSoup

# 01 우리가 가져올 URL 정보
# 02 해당 사이트에서 내가 원하는 정보의 위치(span, id)
# url : https://finance.naver.com/sise/
# tag : span, id : KOSPI_now

##  html 코드를 요청해서 가져온다.
url = "https://finance.naver.com/sise/"
page = urlopen(url)
print(page)

## 구체적인 html 확인하고, 구조화
soup = BeautifulSoup(page, 'html.parser')
KOSPI = soup.find("span", id="KOSPI_now") # 태그명, 추가정보(id)
KOSDAQ = soup.find("span", id="KOSDAQ_now") # 태그명, 추가정보(id)
KPI200 = soup.find("span", id="KPI200_now") # 태그명, 추가정보(id)
print("\n현재 코스피:",KOSPI.text)
print("현재 코스닥:",KOSDAQ.text)
print("현재 코스피200:",KPI200.text,'\n')

popular = soup.find("ul", id="popularItemList")
print("인기 검색 종목:",popular.text)

major_abroad =  soup.find("ul", "lst_major")
print("주요 해외지수:",major_abroad.text)
