from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')
print(soup.title)


### 상영작/예정작 제목만 추출
soup_ul_li = soup.find("ul",class_="lst_detail_t1").find_all("li")
print("ul태그 > li태그의 요소 개수:",len(soup_ul_li))
soup_ul_li

# <확인단계>
# ul태그 > li태그(현위치) > div태그 > a태그 : 상세창 링크
# ul태그 > li태그(현위치) > dl태그 > dt태그 > a태그 : 제목
# 따라서, 그냥 a태그하면 위에 정보도 같이 크롤링 됨
print( soup_ul_li[0].find("dt",class_="tit").a.text)
print( soup_ul_li[3].find("dt",class_="tit").a.text)


### 평점 정보만 추출 <확인단계>
print( soup_ul_li[0].find("span",class_="num").text)
print( soup_ul_li[3].find("span",class_="num").text)


### 참여 명수만 추출 <확인단계>
print( soup_ul_li[0].find("em").text)
print( soup_ul_li[3].find("em").text)


### 예매율만 추출 <확인단계>
print( soup_ul_li[0].find("dl",class_="info_exp").span.text)    # span 태그로 바로 이동
print( soup_ul_li[3].find("dl",class_="info_exp").span.text)
temp = soup_ul_li[122].find("dl",class_="info_exp")
if temp is not None:          # 있으면 
    t = temp.span.text        # 출력한다
    print('예매율 정보가 있음',t)
else : 
    t = 0                     # 없으면
    print('예매울 정보가 없음')  # 출력안함.


### 개요만 추출 <확인단계>
txt = soup_ul_li[0].find("span",class_="link_txt").text
#print( txt )
txt_last =txt.replace("\n","")
txt_last =txt_last.replace("\t","")
txt_last =txt_last.replace("\r","")
print( txt_last )

print('\n\n\n\n')
### for문 한번에 돌리기
movie_title_list = []
movie_rate_list = []
movie_staff_list = []
movie_book_list = []
movie_genre_list = []

for one in soup_ul_li:
    movie_title_text_only = one.find("dt",class_="tit").a.text
    movie_rate_text_only = one.find("span",class_="num").text
    movie_staff_text_only = one.find("em").text
    movie_genre_text_only = one.find("span",class_="link_txt").text
    movie_genre_text_only_last = movie_genre_text_only.replace("\n", "")
    movie_genre_text_only_last = movie_genre_text_only_last.replace("\t", "")
    movie_genre_text_only_last = movie_genre_text_only_last.replace("\r", "")

    movie_title_list.append(movie_title_text_only)
    movie_rate_list.append(movie_rate_text_only)
    movie_staff_list.append(movie_staff_text_only)
    movie_genre_list.append(movie_genre_text_only_last)

# 확인 작업 <각 항목별 갯수 출력>
print(len(movie_title_list),len(movie_rate_list),len(movie_staff_list),len(movie_genre_list))


### 예매율 정보 for문 (뒷부분 영화는 예매율 정보가 없어서 에러남.)
for one in soup_ul_li:
    tmp = one.find("dl",class_="info_exp")
    if tmp is not None:
        movie_book_text_only = tmp.span.text
        #movie_book_text_only = one.find("dl", class_="info_exp").span.text
    else:
        movie_book_text_only = None
    movie_book_list.append(movie_book_text_only)

print(len(movie_book_list))


### 저장을 위한 csv, xlsx 파일 만들기
import pandas as pd
dat_dict = {
    "제목" : movie_title_list,
    "평점" : movie_rate_list,
    "참여명수" : movie_staff_list,
    "예매율" : movie_book_list,
    "장르" : movie_genre_list}
dat = pd.DataFrame(dat_dict)
dat.to_csv("네이버영화.csv", index=False)
dat.to_excel("네이버영화.xlsx", index=False)


### 추가 실습 : 기타 정보(감독, 출연, 상영시간) 추가 후 - 댓글 달기 (편집됨)
### 추가 실습 : 개봉 날짜 추가 - 댓글 달기
### 추가 실습 : 감독 인원 추가 - 댓글 달기

# 기타 정보(감독, 출연) 추출 <확인단계>
print( soup_ul_li[0].find_all("span",class_="link_txt")[1].text)
#print( soup_ul_li[1].find_all("span",class_="link_txt")[2].text)
txt = soup_ul_li[1].find_all("span",class_="link_txt")[2].text
txt_last = txt.replace("\n","")
txt_last = txt_last.replace("\t","")
txt_last = txt_last.replace("\r","")
print(txt_last)

# 기타정보(상영시간) 추출 <확인단계>
soup_ul_li_dd5 = soup_ul_li[0].find_all("dd")[4]
runtime = soup_ul_li_dd5.text[0]
print(runtime)
print(soup_ul_li_dd5.text[1])
print(soup_ul_li_dd5.text[2])
print(soup_ul_li_dd5.text[3])
print(soup_ul_li_dd5.text[4])
print(soup_ul_li_dd5.text[5])
print(soup_ul_li_dd5.text[6])
#print(soup_ul_li_dd2)
#print(soup_ul_li_dd2)
#soup_ul_li_dd2_dd1 = soup_ul_li_dd2.find_all("dd")[0]
#print(soup_ul_li_dd2_dd1)
#print(soup_ul_li_dd3)



dir_list = []
act_list = []
runtime_list = []
for one in soup_ul_li:
    dir_text_only = one.find_all("span",class_="link_txt")[1].text
    # act_text_only =
    dir_list.append(dir_text_only)


