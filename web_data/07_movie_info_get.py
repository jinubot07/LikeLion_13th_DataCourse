from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')


# 영화 제목
print('영화 제목 정보 가져오기')
movie_info = soup.find_all("dl",class_="lst_dsc")
list_title = []
for one in movie_info:
    movie_title = one.find("a").text
    #print(movie_title)
    list_title.append(movie_title)

print(len(list_title),list_title)
print()

## csv, xlsx파일에 추가하기
movie_title_csv = pd.DataFrame({"상영작/예정작 영화 제목": list_title})
movie_title_csv.to_csv("movie_title.csv", index=True)     # index 넣기

#########################################################################
# 평점 가져오기
print('영화 평점 정보 가져오기')
movie_info = soup.find_all("dl",class_="lst_dsc")
list_rate = []
for one in movie_info:
    movie_rate = one.find("span", class_="num").text
    list_rate.append(movie_rate)
print(len(list_rate),list_rate)
print()

## csv, xlsx파일에 추가하기
movie_rate_csv = pd.DataFrame({"상영작/예정작 영화 평점": list_rate})
movie_rate_csv.to_csv("movie_rate.csv", index=True)     # index 넣기

# 평점 가져오기(선생님 코드)
print('평점 정보 가져오기(강사님코드)')
score_all = soup.find_all("dl", class_='info_star')

all_score = []
for one in score_all:
    one_score = one.find('span', class_="num").text
    all_score.append(one_score)
print(len(all_score),all_score)
print()

#########################################################################
# 예매율 정보 가져오기
print('예매율 정보 가져오기(강사님코드)')
tmp_book = soup.find_all("dl", class_='info_exp')
# print( score_all[2].find('span',class='num').text)

list_rate_book = []
for one in tmp_book:
    one_rate = one.find('span',class_='num').text
    list_rate_book.append(one_rate)
print(len(list_rate_book),list_rate_book)
print()

#########################################################################
# 참여명수 정보 가져오기
print('참여명수 정보 가져오기')
movie_info = soup.find_all('dl', class_='info_star')

list_staff=[]
for one in movie_info:
    staff_num = one.find('em').text
    list_staff.append(staff_num)
print(len(list_staff),list_staff)
print()
#########################################################################
# 타이틀, 평점, 예매율, 참여명수  파일만들기
import pandas as pd
dict_dat = { "영화제목" : list_title,
             "평점" : list_rate,
             #"예매율" : list_rate_book,
             "참여 명수" : list_staff }
dat = pd.DataFrame(dict_dat)
print(dat)
dat.to_csv('naver_movie_info.csv', index=False)
dat.to_excel('naver_movie_info.xlsx', index=False)

