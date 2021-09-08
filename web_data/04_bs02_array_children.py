from bs4 import BeautifulSoup
from urllib.request import urlopen

page1 = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
</div>
<div>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역1] 필요없는 정보1 </p>
    <p class="p3"> [영역1] 필요없는 정보3 </p>
    <p id="p4"> [영역1] 필요없는 정보2 </p>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크 </p>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크222 </p>
    <p id="p4"> [영역2] 간단한 나의 홈페이지를 만들다.</p>
</div>
</body>
</html>
'''

#
soup1 = BeautifulSoup(page1, 'lxml')
# print( soup1.title )
#
# ##
one_info = soup1.find_all("div")
print("(1) div개수:",len(one_info))
print()

wanted_info = soup1.find_all('div')[3]
print("(2)4번째 div태그의 내용:\n",wanted_info)
print()

last_info_multi = wanted_info.find_all('p',class_="p3")
print("(3)4번째 div태그에서 클래스명이 'p3'인 요소의 내용(list형식으로 출력):\n",last_info_multi)
print()

print("(3-2) 4번째 div태그에서 클래스명이 'p3'인 요소의 내용(text부분만 출력):")
for one in last_info_multi:
    print(one.text)
print()

print("(4) 3번째 div태그에서 클래스명이 'p3'인 요소의 내용(list형식으로 출력):")
wanted_info = soup1.find_all('div')[2]
last_info_multi = wanted_info.find_all('p',class_='p3')
print(last_info_multi)
print()

print("(4-2) 3번째 div태그에서 클래스명이 'p3'인 요소의 내용(text부분만 출력):")
wanted_info = soup1.find_all('div')[2]
last_info_multi = wanted_info.find_all('p',class_='p3')
for one in last_info_multi:
    print(one.text)
print()

print("(4-3) 3번째 div태그에서 클래스명이 'p3'인 요소의 내용(text부분만 lsit에 담아 출력):")
wanted_info = soup1.find_all('div')[2]
last_info_multi = wanted_info.find_all('p',class_='p3')
a = []
for one in last_info_multi:
    a.append(one.text)
print(a)
print()

print("(5) 3번째 태그 내용을 enumerate로 인덱스와 내용을 함께 출력")
wanted_info = soup1.find_all('div')[2]       # wanted_info : 3번째 div태그의 내용
last_info_multi = wanted_info.find_all('p',class_='p3') # last_info_multi : 3번째 div 태그 내용에서 p3클래스명가진 요소
for idx, one in enumerate(wanted_info):
    print(idx, " : ", one)      # 줄바꿈도 하나의 원소임


# children
print("(6) children : 자기자신(div태그명)을 제외하고 개행문자 포함 모든 하위항목들을 가리킴")
print("                    저장된 위치 : ", wanted_info.children)
print("          childen 요소들(list) : ",list(wanted_info.children))
print("           10번째 childrem 요소 : ",list(wanted_info.children)[9])
print("10번째 childrem 요소(text정보만) : ",list(wanted_info.children)[9].text)