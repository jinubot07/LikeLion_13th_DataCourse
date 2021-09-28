from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup.title)

comment_all = soup.find_all("td",class_='title')
#print(len(comment_all))
#print(comment_all[1])
#print(comment_all[1].text)

dat = list(comment_all[2].children) # 3번째 댓글 정보 중
print('댓글정보가 포함 된 리스트의 총 길이 :',len(dat))
print(dat)
#dat_comment = dat[6].replace('\r','').replace('\t','').replace('\n', '') #리뷰 내용만, 공백없이
dat_comment = dat[6].strip()
print('리스트의 7번째 요소 = 댓글 :',dat_comment,'\n\n')