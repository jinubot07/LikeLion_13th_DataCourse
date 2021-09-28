import wordcloud
from wordcloud import WordCloud
from matplotlib import rc # 폰트를 지정해주는 친구

print(wordcloud.__version__)

# 파일 오픈 모드 - r/w/a
# 파일 읽기 함수 - read(), readline(), readlines()
f = open("영화리뷰(1~5페이지).csv", encoding='utf-8')
text = f.read()
print(text)
f.close()


rc('font', family='NanumGothic')
wcloud = WordCloud('./data/D2Coding.ttf',
                   max_words= 1000,
                   relative_scaling=0.2).generate(text)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')    # 영상의 손실된 부분을 어떤 방식으로 처리하겠다.
plt.axis('off')
plt.savefig('movie_spdiderman_review.png')
plt.show()