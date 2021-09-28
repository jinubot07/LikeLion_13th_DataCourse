from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

## 댓글 1페이지의 댓글(10개) 전체 가져오기
url1 = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page=1"
page = urlopen(url1)
soup = BeautifulSoup(page, "html.parser")
comment_all = soup.find_all('td', class_='title')
# comment_all[0] 에는 댓글 내용이 포함된 영화 리뷰 관련 태그와 함께 리스트에 저장되어있음.
# comment_all 에서 7번째 요소에 영화 리뷰 관련 내용이 있음
print(" * comment_all의 갯수 = 댓글의 갯수 :",len(comment_all))
print(" * 첫 번째 comment_all에 담긴 내용물 :",comment_all[0])
print(" * comment_all의 children : ",list(comment_all[0].children))

comment_list =[]
for one in comment_all:
    temp = list(one.children)[6].strip()
    #print(temp)
    comment_list.append(temp)

print(comment_list)
dict_dat = {  '영화 리뷰(댓글)' : comment_list }
dat = pd.DataFrame(dict_dat)
dat.to_csv("영화리뷰.csv", index=False)
dat.to_excel("영화리뷰.xlsx", index=False)
