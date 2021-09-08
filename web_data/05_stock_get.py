# 3-6 실습 - 코스피 정보 가져오기
# 3-6 실습 - 거래량, 장중최고, 52주최고
# 3-7 (추가) 투자자별 매매동향, 프로그램 매매동향
# 3-8 실습 - 시황뉴스

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')
print(soup.title,'\n')

# 코스피 정보가져오기
print("(1) 코스피 정보 가져오기")
kospi_now = soup.find('em', id='now_value')
print('현재 코스피 : ',kospi_now.text)

# 거래량 천주 정보 가져오기
deal_info = soup.find('td', id='quant')
print('    거래량 : ', deal_info.text)

# 장중 최고, 52주 최고
high_value = soup.find('td', id='high_value')
low_value = soup.find('td', id='low_value')
max_52week = soup.find('td', class_= 'td')
min_52week = soup.find('td', class_= 'td2')
print('  장중최고 : ', high_value.text)
print('  장중최저 : ', low_value.text)
print('  52주최고 : ', max_52week.text)    # 틀렸음: 다양한 태그에 같은 class명이 ㅣㅇㅅ어서 안됌
print('  52주최저 : ', min_52week.text)
print()

# 52주 최고를 가져오는 또다른 방법
print('  52주최고 가져오는 방법 (id활용하지 않고 태그 검생을 통해)')
tmp_index = soup.find("table", class_="table_kos_index")
tmp_52week = tmp_index.find_all("tr")[2].find('td')
print('  52주최고 : ',tmp_52week.text)
print()


print("(2) 시황 뉴스 가져오기")
# 시황뉴스 가져오기
tmp_news = soup.find_all("ul", class_ = "sise_report")      # 두 번째 이후에 있는 요소 값 가져오기 위해 find_all 사용
print("클래스명이 'sise_report'인 ul태그의 개수 : ",len(tmp_news))    # 개수를 확인함으로서 겹치는 게 있는 지 확인
tmp_news = soup.find("ul", class_ = "sise_report")          # 첫 번째 요소에 있기떄문에 굳이 find_all 해줄 필요없다
print()
tmp_news_title = tmp_news.find_all('span', class_="tit")

# 리스트 안에 담긴 태그중 텍스트만 출력
print('(2-2) 시황뉴스 제목(text값만) 출력(list에 담긴 tag중 text값만)')
for one in tmp_news_title:
    print("->",one.text)
print()

# 리스트 안에 태그 중 텍스트만 담기
news_title = []
print('(2-3) 시황뉴스 제목(text값만) 리스트에 담기')
for one in tmp_news_title:
    news_title.append(one.text)
print(news_title)

#시황뉴스 제목 목록을 csv파일로 만들기
print('(2-4) csv와 excel로 변환하기')
import pandas as pd
dat = pd.DataFrame({"시황뉴스 : ":  news_title})
print(dat)
dat.to_csv("news.csv", index=True)               # index 넣기
dat.to_excel("news_excel.xlsx", index=False)    # index 안넣기
print()




# 시황정보 리포트 가져오기
print("(3) 시황정보 리포트 가져오기")
tmp_info = soup.find_all("ul", class_ = "sise_report")[1]
tmp_info_title = tmp_info.find_all('span',class_='tit')
print(tmp_info_title)
print()

print("(3-2) 시황정보 제목(text값만) 출력")
for one in tmp_info_title:
    print("->",one.text)
print()


print('(3-3) 시황정보 제목(text값만) 리스트에 담기')
info_title = []
for one in tmp_news_title:
    info_title.append(one.text)
print(info_title)
print()