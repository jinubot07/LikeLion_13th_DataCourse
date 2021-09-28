from bs4 import BeautifulSoup
from urllib.request import urlopen

page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
<p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
<p class="p3"> 강아지 사진과 네이버 링크 </p>
<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
<p class="p3"> 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''

soup = BeautifulSoup(page,'lxml') # html.parser 이나 html5lib도 있음.
# soup에는 html형식의 모든 코드가 담겨있음.

# 가져오고 싶은 text를 포함하는 요소(element) 정보 가져오기
# tag, class명 이나 id 명

# title요소 정보 가져오기
print(soup.title)
# html형식의 모든 코드중에서 title태그에 해당하는 값만 추출

# a 태그 요소 가져오기(1)
print("a태그 첫 번째꺼만 가져오기")
print(soup.a,'\n')
# a 태그 요소 가져오기(2)
print("a태그 전체 가져오기")
print(soup.find_all("a"),'\n')

#실습 : p태그 전체 가져오기
print("p태그 전체 가져오기")
print(soup.find_all("p"),'\n')

#실습 : p태그 중 id가 p4인 요소 가져오기
print("p태그 중 id가 p4인 요소 가져오기")
print(soup.find("p",id="p4"))