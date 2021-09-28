from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise"
page = urlopen(url) # 웹 url로붙 페이지를 가져온다.
print(page)


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
''' #파일형태면 open명령어 사용

soup = BeautifulSoup(page,'lxml')
print(soup.title)

# 태그명 soup.태그명 -> 해당되는 요소의 정보를 가져옴
# print(soup.title)
# print(soup.body)
# print(soup.div)
# print(soup.img)
# print(soup.a)
# print(soup.a.text)
print(soup.p)                     #<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
print(soup.div.p)                 #<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
print(soup.div.p.text)            #내가 가장 좋아하는 동물은 강아지입니다.
print()
# id, class를 활용해서 정보가져오기 - 하나의 요소 가져오기(find)
# id, class를 활용해서 정보가져오기 - 모든 요소(find_all) list형태
print(soup.find("p",id = "p4"))             #<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
print(soup.find("p",id = "p4").text)        #<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
print(soup.find_all("p"))  #모든 p태그 가져오기 (list형태로)


# 실습 : find, find_all 사용해서 naver 정보와 모든 a태그 가져오기
print("(1) naver정보 가져오기\n",soup.div.a.text) # soup에서 div에서 a에서 text정보를 갖겠다~
print("(2) find사용해서 naver정보 가져오기\n",soup.find("a").text)
print("(3) find_all사용해서 모든 a태그 가져오기\n",soup.find_all("a")) # soup에서 모두 찾겟다~
#soup.find_all("a").text : text를 써주지 못한다 왜냐하면 list형태로 이미 담긴 상황이기 때문
#굳이 text만 가져오고 싶다면,
list_find_all_data = soup.find_all("a")
print("(3-2) find_all에서  모든 a태그의 text정보만 가져오기\n","자료형:",type(list_find_all_data),"\n 텍스트 값:",list_find_all_data[0].text,list_find_all_data[1].text)
print("(4) div요소정보를 가져온 후, p태그(id='p4')요소 가져오기\n",soup.div.find("p",id = "p4").text)
# soup에서 div에서 찾겟다~

# 실습 : 한줄코드로 class정보 이용해서 p3인 것을 가져와서 2번째 요소의 text 출력
print("(5) 한줄코드로 class정보 이용해서 p3인 것을 가져와서 2번째 요소의 text 출력")
print(soup.div.find("p", "p3").text)
print(soup.div.find_all("p", class_="p3")[0].text)
print(soup.div.find_all("p", class_="p3")[1].text)

# 실습 : a태그의 모든 텍스트 정보가져오기
print("(6) 한줄코드로 모든 a태그의 텍스트정보 가져오기")
print(soup.div.find_all("a")[0].text)
print(soup.div.find_all("a")[1].text)

# 실습(추가) : a태그의 link 정보 가져오기 (.attrs활용하기 / .없이 ['href']만 활용하기)
print("(7) 모든 a태그의 링크 정보 가져오기")
print(soup.div.find_all("a")[0].attrs['href'])
print(soup.div.find_all("a")[1].attrs['href'])
# linkㄴ = soup.div.find_all("a")
# cell_line = []
# for i in links:
#     href = i.attrs['href']
#     cell_line.append(href)
# print(cell_line)

print(soup.find_all('a')[0]['href'])
print(soup.find_all('a')[1]['href'])
# links = soup.find_all('a')
# for i in links:
#     print(i["href"])
