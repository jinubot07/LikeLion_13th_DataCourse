# 코스닥 정보에 대한 지수 정보 파일 하나 만들기
# 시황정보 뉴스 20210908_14_news.csv
# 시황정보 리포트 20210908_14_report.csv
# 인기검색어 20210908_14_pop_world.csv
# 가장 많이 본 뉴스 20210908_14_cnt_news.csv

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')
##---------------------------------------------------------------
# 시황정보 뉴스 (정보가져오기)
news = soup.find_all("ul",class_="sise_report")[0]
news_title = news.find_all('span',class_='tit')
print("<시황정보 뉴스>")
news=[]
for one in news_title:
    print(one.text)
    news.append(one.text)

# 시황정보 뉴스 (csv파일로 변환하기)
news_csv = pd.DataFrame({"시황정보 뉴스": news})
# print(news_csv)
news_csv.to_csv("20210908_14_news.csv", index=True)     # index 넣기
#---------------------------------------------------------------
# 시황정보 리포트 (정보가져오기)
report = soup.find_all("ul",class_="sise_report")[1]
report_title = report.find_all('span',class_='tit')
print("\n<시황정보 리포트>")
report=[]
for one in report_title:
    print(one.text)
    report.append(one.text)

# 시황정보 리포트 (csv파일로 변환하기)
report_csv = pd.DataFrame({"시황정보 리포트": report})
# print(report_csv)
report_csv.to_csv("20210908_14_report.csv", index=True)     # index 넣기
#---------------------------------------------------------------
# 인기검색어(정보가져오기)
pop_box = soup.find_all("div", class_="box_type_r_top")[0]
pop_list = pop_box.find_all("a", class_="company") # pop_box.find_all("td") 가 아님

print("\n<인기검색어>")
pop=[]
for one in pop_list:
    print(one.text)
    pop.append(one.text)
# for one in pop_list:
#     print(one.find('a', class_='company').text)

# 인기검색어 (csv파일로 변환하기)
pop_csv = pd.DataFrame({"시황정보 인기검색어": pop})
pop_csv.to_csv("20210908_14_pop_world.csv", index=True)     # index 넣기
