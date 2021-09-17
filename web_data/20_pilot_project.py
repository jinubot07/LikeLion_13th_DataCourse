# CV crawling from "https://jasoseol.com/example/"
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from matplotlib import rc
import time
####################################################################################
# 0. 합격 자기소개서를 확인할 기업체 리스트에 담기
# 1-0. 잡코리아 ID와 비번 입력받기
# 1-1.       잡코리아 메인 사이트 접속 : https://www.jobkorea.co.kr/
# 1-2.                   로그인 과정 : 탭 클릭 -> ID 및 비밀번호 입력 -> 버튼 클릭
# 1-3. 잡코리아 합격 자소서 사이트 이동 : https://www.jobkorea.co.kr/starter/passassay/
# 1-4.                   팝업창 닫기 : 닫기 버튼 xpath로 찾아 클릭
# 2-1.                 검색조건 선택 : 지원분야(IT인터넷>전체), 근무형태(신입), 학력(4년제대졸) 체크 -> <선택 조건으로 검색> 버튼 클릭
# 2-2.                    기업 검색 : 검색창에 원하는 기업명 입력 -> 검색 버튼 클릭
# 3-1.                참고 가치 판단 : <전문가 분석 보기> 버튼 클릭
# 3-2.                             : <전문가 총평> 3점 이상인 합격자소서만 클릭
# 4-1.          합격자소서의 갯수 확인 : tag의 갯수
# 4-2. 순차적으로 합격 자기 소개서 접속 : xpath 클릭
# 4-3.              합격자소서 크롤링 : 답변만 크롤링
# 5-1.                csv형태로 저장 :
# 5-2.                      시각화  : 크롤링한 답변을 wordcloud로 가시화
####################################################################################

# 0. 정보입력(로그인정보, 검색 기업정보)
jobkoreaID = input("잡코리아 ID 입력 : ")
jobkoreaPW = input("잡코리아 Password 입력 : ")
companyName = input("검색하려는 기업명 입력 : ")
# jobkoreaID = '****'
# jobkoreaPW = '****'
# companyName = 'SK하이닉스'


# 1-1. 잡코리아 메인 사이트 접속: 웹사이트 HTML SOURCE CODE가져오기 (방법 1: BeautifulSoup)
url_main = "https://www.jobkorea.co.kr/"
page = urlopen(url_main)
soup = BeautifulSoup(page, 'html.parser')
# 이후 find 및 find_all 로 원하는 정보에 접근

# 1-1. 웹사이트 HTML SOURCE CODE가져오기 (방법 2: Selenium)
driver = webdriver.Chrome('./data/chromedriver')
url_main = "https://www.jobkorea.co.kr/"
driver.get(url_main)
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
# 이후 xpath 및 find(.명령어)로 원하는 정보에 접근
time.sleep(1)

# 1-2. 로그인 과정
signinStart = driver.find_element_by_xpath('//*[@id="point"]/div/div[1]/div[1]/ul/li[1]/button')
signinStart.click()
time.sleep(1)
signinID = driver.find_element_by_xpath('//*[@id="lb_id"]')
signinPW = driver.find_element_by_xpath('//*[@id="lb_pw"]')
signinButton = driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/div[1]/button')
signinID.send_keys(jobkoreaID)
signinPW.send_keys(jobkoreaPW)
signinButton.click()
time.sleep(1)

# 1-3. 잡코리아 합격 자소서 사이트 이동
url_cv = "https://www.jobkorea.co.kr/starter/passassay/"
driver.get(url_cv)
# page = driver.page_source
# soup = BeautifulSoup(page, 'html.parser')

# 1-4. 팝업창 닫기
#close_button = driver.find_element_by_xpath('/html/body/div[8]')
close_button = driver.find_element_by_xpath('/html/body/div[7]/div/button')
close_button.click()


# 2-1. 검색조건 선택 : 지원분야(IT인터넷>전체), 근무형태(신입), 학력(4년제대졸) 체크
sort_field_IT = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div/div[1]/div/dl[1]/dd[1]/div/div[1]/div/ul[1]/li[3]/label')
sort_field_IT.click()
sort_field = driver.find_element_by_xpath('//*[@id="g_10016"]/ul[1]/li[1]/label/i')
sort_field.click()
sort_type = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div/div[1]/div/dl[2]/dd/div/div[1]/div/ul/li[1]/label/i')
sort_type.click()
sort_acade = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div/div[1]/div/dl[3]/dd/div/div[1]/div/ul/li[3]/label/i')
sort_acade.click()
sort_button = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div/div[2]/button')
sort_button.click()
time.sleep(1)
# 한 방에 가는 방법이 잇었음;;
# url_sort = "https://www.jobkorea.co.kr/starter/PassAssay?schPart=10016&schWork=1&schEduLevel=3&schCType=&schGroup=&isSaved=0&isFilterChecked=&OrderBy=0&schTxt="
# driver.get(url_sort)

# 2-2.  기업 검색 : 검색창에 원하는 기업명 입력 -> 검색 버튼 클릭
company_name = driver.find_element_by_xpath('//*[@id="txtSearch"]')
company_name.send_keys(companyName)
company_search = driver.find_element_by_xpath('//*[@id="btnSraech"]')
company_search.click()
time.sleep(1)


# 3. (옵션) 전문가 분석 보기 -> 전문가 총평 3점 이상인 합격자기소개서만 보기



# 4-1. 합격자소서의 개수(->for문에 활용)
url_now  = driver.current_url
# driver.get(url_now) # 기존의 윈도우 창에 해당 url이동하기
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')   # 검증절차 : print(soup.title)
howmany_cv = len(soup.find_all('div',class_='txBx'))

# 4-1. (질문) BeautifulSoup 말고 Selenium 문법으로 코딩하기
# howmany_cv = driver.find_elements_by_class('txBx')

# 4-2. 순차적으로 합격 자기 소개서 접속 : xpath 클릭
# 바깥 for문은 자소서 개수 만큼 반복, 안쪽 for문은 한 자소서 내 문제 개수만큼 반복
# 전문가의 견해와 자기소개 답변이 같은 태그와 크래스명으로 묶여있어서 구분하는 작업 필요
# 다행히 지원자의 답변이 앞쪽에 전문가 평가는 뒷쪽에 정렬이 되어있어서
# 문제의 개수만큼 리스트의 앞부분만 크롤링하면, 합격 자소서의 답변만 크롤링 할 수 있었다.

#첫번째 합격자소서 xpath : //*[@id="container"]/div[2]/div[5]/ul/li[1]/div[1]/div/div[1]/a
#두번째 합격자소서 xpath : //*[@id="container"]/div[2]/div[5]/ul/li[2]/div[1]/div/div[1]/a
#세번째 합격자소서 xpath : //*[@id="container"]/div[2]/div[5]/ul/li[3]/div[1]/div/div[1]/a
#네번째 합격자소서 xpath : //*[@id="container"]/div[2]/div[5]/ul/li[4]/div[1]/div/div[1]/a

#               # 하나의 합격 자소서 크롤링
# passed_cv_xpath = '//*[@id="container"]/div[2]/div[5]/ul/li[1]/div[1]/div/div[1]/a'
# passed_cv_button = driver.find_element_by_xpath(passed_cv_xpath)
# passed_cv_button.click()
#
# page = driver.page_source
# soup = BeautifulSoup(page, 'html.parser')   # 검증절차 : print(soup.title)
# soup_q = soup.find('dl','qnaLists')
# howmany_q = len(soup_q.find_all('span',class_='num'))
# answer = soup.find_all('div', class_='tx')
#
# # 4-3. 합격자소서 크롤링 : 답변만 크롤링
# answer_list = []
# for i in range(howmany_q) :
#     answer_list.append(list(answer)[i].text)
# print(answer_list)

            # 여러 합격 자소서 크롤링
answer_list = []
for i in range(1,howmany_cv + 1):
    # 합격 자소서 페이지로 이동
    passed_cv_xpath = '//*[@id="container"]/div[2]/div[5]/ul/li['+str(i)+']/div[1]/div/div[1]/a'
    passed_cv_button = driver.find_element_by_xpath(passed_cv_xpath)
    passed_cv_button.click()

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    soup_q = soup.find('dl','qnaLists')
    howmany_q = len(soup_q.find_all('span',class_='num'))
    answer = soup.find_all('div', class_='tx')

    for i in range(howmany_q) :
        answer_list.append(list(answer)[i].text)

    driver.get(url_now)         # 목록 페이지로 이동
    time.sleep(1)

print(answer_list)


# 5-1. csv형태로 저장 (csv파일로 변환하기)
passed_cv_csv = pd.DataFrame({"SK하이닉스 합격자소서": answer_list})
# print(report_csv)
csv_name = companyName + "_합격자소서.csv"
passed_cv_csv.to_csv(csv_name, index=False)

# 5-2. wordcloud로 시각화 (제외할 단어)
f = open(csv_name, encoding='utf-8').read()
rc('font', family='NanumGothic')


stwords = set(STOPWORDS)    # 제외할 단어
stwords.add("위해")
stwords.add("저는")
stwords.add("아쉬운점")
stwords.add('통해')
stwords.add('글자수')
stwords.add('했습니다')
stwords.add('때문에')
stwords.add('것을')
stwords.add('였습니다')
stwords.add('싶습니다')
stwords.add('있습니다')
stwords.add("있었습니다")
stwords.add("수")
stwords.add("있는")
stwords.add("0000")


wcloud = WordCloud('./data/D2Coding.ttf',
                   stopwords = stwords,
                   max_words=1000,
                   relative_scaling=0.2,
                   background_color='#FFFFFF').generate(f)

import matplotlib.pyplot as plt

png_name = companyName + "_합격자소서_worcloud.png"
plt.figure(figsize=(12, 12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig(png_name)
plt.show()


