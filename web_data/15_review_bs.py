from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

html = """
<html>
 <head>
  <title> test site </title>
 </head>
 <body>
  <p align="left" class="class1">  test3  </p>
  <p class="class1">  test2  </p>
  <p id="p1">  오늘의 주가지수 1500  </p>
  <span class="class3">  span tag text  </span>
  <p class="class4">  test3  </p>
 </body>
</html>
"""
soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())
basic_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page="
page = urlopen(basic_url)
soup = BeautifulSoup(page, "html.parser")

comment_all = soup.find_all('td', class_='title')
comment_all
print(len( comment_all ))

temp = list(comment_all[5].children)
temp[6]

temp = list(comment_all[1].children)
result = temp[6].strip()
result

cnt = 0
comments = []
for comment in comment_all:
    temp= list(comment.children)
    if len(temp) < 5:
        cnt= cnt + 1
        continue
    else:
        try:
            cnt= cnt + 1
            result = temp[6].strip()
            comments.append(result)
        except:
            print("error cnt count", cnt)
comments
comments = [ ]
cnt = 0
for i in range(1,8):
    url = basic_url + str(i)
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    comment_all = soup.find_all('td', class_='title')
    for comment in comment_all:
        temp= list(comment.children)
        if len(temp) < 5:
            cnt= cnt + 1
            print("len<5 case :",cnt)
            continue
        else:
            try:
                cnt= cnt + 1
                result = temp[6].strip()
                comments.append(result)
            except:
                cnt= cnt + 1
                print("len>=5 case ",cnt)
                print(temp)
print(len(comments))
print(comments)
print(cnt)

dict_doc = {"text" : comments}
doc = pd.DataFrame(dict_doc)

doc.to_csv("스파이더맨리뷰.csv", index = False)

from wordcloud import WordCloud, STOPWORDS

import numpy as np
from PIL import Image

f = open("스파이더맨리뷰.csv", encoding="utf-8")
text = f.read()
f.close()

from matplotlib import rc
rc('font', family='NanumGothic')