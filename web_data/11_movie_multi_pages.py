from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

### 1~5 페이지 가져오기
basic_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page="

comment_list_5pages = []
for i in range(1,6,1):
    real_url = basic_url+str(i)
    page = urlopen(real_url)
    soup = BeautifulSoup(page,'html.parser')
    comment_all = soup.find_all('td',class_='title')
    #print(len(comment_all))

    for one in comment_all:
        temp = list(one.children)[6].strip()
        # print(temp)
        comment_list_5pages.append(temp)
        print(temp)

print(comment_list_5pages)

dict_dat = {  '영화 리뷰(댓글)' : comment_list_5pages }
dat = pd.DataFrame(dict_dat)
dat.to_csv("영화리뷰(1~5페이지).csv", index=True)
dat.to_excel("영화리뷰(1~5페이지).xlsx", index=True)