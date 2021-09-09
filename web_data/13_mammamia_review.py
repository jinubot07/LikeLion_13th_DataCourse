from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import wordcloud
from wordcloud import WordCloud
from matplotlib import rc

basic_url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=66381&target=after&page='
page = urlopen(basic_url)
soup = BeautifulSoup(page,'html.parser')

### 한개의 댓글 시도
#comment_1st = soup.find_all('td','title')[0]
#print(len(list(comment_1st.children))) # 댓글 정보가 포함된 리스트에는 총 9개의 요소가 있다
#print(list(comment_1st.children))
#print(list(comment_1st.children)[6].strip())         # 그 중 7번째 요소가 댓글 내용

### 한 페이지의 모든 댓글(10개)
# soup_td = soup.find_all('td','title')
# comments_list =[]
# for one in soup_td:
#     comment = list(one.children)[6].strip()
#     print(comment)
#     comments_list.append(comment)


### 5 페이지를 반복하여 10개씩 총 50개의 댓글 가져오기
comments_list =[]
for i in range(1,6):
    url = basic_url + str(i)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    soup_td = soup.find_all('td', 'title')

    for one in soup_td:
        comment = list(one.children)[6].strip()
        comments_list.append(comment)

dict_dat = {"영화'맘마미아1' 감상평": comments_list}
dat = pd.DataFrame(dict_dat)
dat.to_csv("영화'맘마미아1'감상평.csv", index=True)

### 댓글 정보 시각화
f = open("영화'맘마미아1'감상평.csv",encoding='utf-8').read()
rc('font', family='NanumGothic')
wcloud = WordCloud('./data/D2Coding.ttf',
                   max_words= 1000,
                   relative_scaling=0.2).generate(f)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')    # 영상의 손실된 부분을 어떤 방식으로 처리하겠다.
plt.axis('off')
plt.savefig('movie_mammamia_review.png')
plt.show()